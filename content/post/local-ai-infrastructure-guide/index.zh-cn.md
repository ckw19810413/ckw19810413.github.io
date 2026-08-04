---
title: "本地 AI 基础设施搭建指南：从 0 到 vLLM + ComfyUI 完整部署"
description: "2026 年如何在一台机器上搭建完整的本地 AI 基础设施。从 vLLM 大型语言模型到 ComfyUI 图像生成，手把手教程涵盖安装、优化、自动化部署，以及与 Cowork MCP 整合。"
slug: "local-ai-infrastructure-guide"
layout: "single"
summary: "完整实操指南：使用 DGX GB10 或单 GPU 机器搭建本地 AI 基础设施。涵盖 vLLM 部署、ComfyUI 安装、内存管理、自动化服务以及与多 Agent 框架整合的步骤。"
publishDate: 2026-07-27
updatedDate: 2026-07-27
categories:
  - "AI 基础设施"
  - "实操教程"
tags:
  - "本地 AI"
  - "vLLM"
  - "ComfyUI"
  - "AI 部署"
  - "GPU 优化"
  - "AI 基础设施"
  - "机器学习"
  - "AI 工具链"
draft: false
---

## 为什么要搭建本地 AI 基础设施？

2026 年，AI 工具已经成为数字创作者、开发者和企业的基础设施。但大多数人仍然依赖云端 API — 每次呼叫花钱、每次传输冒隐私风险、每次被速率限制卡住脖子。

本地 AI 基础设施给你三样东西：**完全的控制权、无限制的使用量、零边际成本**。

一旦搭建完成，你可以：
- 无限制使用 LLM，不用担心 API 费用
- 处理敏感数据，不用离开你的机器
- 同时运行多个服务，没有速率限制
- 与 Cowork MCP 等框架整合，打造真正的 AI 代理团队

这份指南假设你已经有一台带有 GPU 的机器（推荐 DGX GB10、RTX 4090 或更好）。我会从零开始，一步步带你搭建完整的本地 AI 环境。

**你今天会学到：**

- 安装和配置本地 LLM 服务（vLLM）
- 部署 ComfyUI 图像生成管线
- 管理 GPU 内存和服务启动顺序
- 自动化服务管理（systemd）
- 与 Cowork MCP 整合，打造多 Agent 系统

我们开始吧。

---

## 前置需求

开始之前，请确认你已准备好：

| 项目 | 版本需求 | 检查指令 |
|------|---------|---------|
| **Linux** | Ubuntu 22.04+ 或 Arch | `uname -a` |
| **GPU** | NVIDIA RTX 3090+/4090/GB10 | `nvidia-smi` |
| **CUDA** | ≥ 12.4 | `nvcc --version` |
| **Docker** | ≥ 24.0 | `docker --version` |
| **Node.js** | ≥ 20 | `node --version` |
| **Python** | ≥ 3.10 | `python3 --version` |

如果你的 GPU 内存不足 24GB，建议关闭不必要的图形界面或服务再开始。

---

## 步骤 1：安装 Docker 和 NVIDIA Container Toolkit

Docker 是部署本地 AI 服务的推荐方式，因为它能隔离依赖、版本冲突和系统污染。

```bash
# 安装 Docker
sudo apt update
sudo apt install -y docker.io docker-compose-v2

# 安装 NVIDIA Container Toolkit（让 Docker 可以使用 GPU）
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

验证 GPU 可用性：

```bash
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

如果看到 GPU 信息和内存使用率，就代表环境设定正确。

---

## 步骤 2：部署 vLLM 本地语言模型

vLLM 是当前最高效的本地 LLM 推理框架，支持多种模型格式（GGUF、GPTQ、AWQ）。

### 2.1 使用 Docker 部署

```bash
docker run -d \
  --name vllm-server \
  --gpus all \
  -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:latest \
  --model "nvidia/Llama-3.1-Nemotron-70B-Instruct" \
  --gpu-memory-utilization 0.9 \
  --max-model-len 8192
```

**参数说明：**
- `--model`: 要部署的模型（可替换为任何 HuggingFace 模型）
- `--gpu-memory-utilization`: 使用 GPU 内存的比例（0.9 表示 90%）
- `--max-model-len`: 最大上下文长度

> **注意：** 如果你的 GPU 内存小于 80GB，建议从较小的模型开始（7B 或 13B），然后再尝试更大的模型。

### 2.2 测试 API 端点

```bash
curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nvidia/Llama-3.1-Nemotron-70B-Instruct",
    "prompt": "解释什么是多 Agent AI 系统",
    "max_tokens": 200
  }'
```

如果收到回应，vLLM 已经成功部署。

### 2.3 设定为系统服务（自动启动）

创建 systemd 服务文件：

```bash
sudo tee /etc/systemd/system/vllm.service << 'EOF'
[Unit]
Description=vLLM Local LLM Server
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/docker start vllm-server
ExecStop=/usr/bin/docker stop vllm-server

[Install]
WantedBy=multi-user.target
EOF
```

启用并启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable vllm.service
sudo systemctl start vllm.service
```

---

## 步骤 3：部署 ComfyUI 图像生成

ComfyUI 是当前最强大的本地图像生成工具，支持 Flux、Stable Diffusion、LTX 等各种模型。

### 3.1 使用 Docker 部署

```bash
docker run -d \
  --name comfyui \
  --gpus all \
  -p 8188:8188 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -v ~/comfyui-output:/output \
  ghcr.io/ai-forest/comfyui:latest
```

这会在 `http://localhost:8188` 启动 ComfyUI。

### 3.2 手动安装（进阶选项）

如果你需要更多控制，可以选择手动安装：

```bash
# 克隆 ComfyUI 仓库
cd ~/comfyui
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# 安装依赖
pip install -r requirements.txt

# 安装自定义节点（可选）
git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation.git custom_nodes/
git clone https://github.com/laksjdjoy/deforum-comfy.git custom_nodes/

# 启动服务
python main.py --listen 0.0.0.0 --port 8188
```

### 3.3 常用模型下载

```bash
# 使用 HuggingFace CLI 下载模型
pip install huggingface_hub
huggingface-cli download stabilityai/stable-diffusion-xl-base-1.0 --local-dir ~/models/sdxl
huggingface-cli download stabilityai/stable-diffusion-3.5-large --local-dir ~/models/sd3.5
```

---

## 步骤 4：GPU 内存管理策略

在本地部署 AI 服务时，GPU 内存是最大的瓶颈。以下是几个实战经验：

### 4.1 检查可用内存

```bash
free -h
nvidia-smi --query-gpu=memory.used,memory.free --format=csv
```

### 4.2 服务启动顺序建议

1. **先启动 vLLM**（语言模型通常内存需求较固定）
2. **后启动 ComfyUI**（图像生成可以动态调整内存使用）
3. **关闭不必要的图形应用**（浏览器、Discord 等）

### 4.3 内存监控脚本

创建一个简单的监控脚本：

```bash
#!/bin/bash
# monitor-gpu.sh
while true; do
    echo "=== $(date) ==="
    nvidia-smi --query-gpu=memory.used,memory.free,temperature.gpu --format=csv
    docker ps --filter "name=vllm\|name=comfyui" --format "table {{.Names}}\t{{.Status}}"
    sleep 30
done
```

---

## 步骤 5：整合 Cowork MCP 多 Agent 框架

一旦本地 AI 基础设施就绪，就可以连接 Cowork MCP 打造多 Agent 系统。

### 5.1 注册 vLLM 作为大脑

```bash
# 如果使用 Hermes Agent
hermes register-cowork

# 或者手动设定 MCP 端点
# 在你的 Agent 设定档中添加：
{
  "mcpServers": {
    "cowork": {
      "url": "http://localhost:6868/mcp",
      "transport": "streamable-http"
    },
    "vllm": {
      "url": "http://localhost:8000/v1",
      "transport": "streamable-http"
    }
  }
}
```

### 5.2 实际应用：本地 AI 内容制作管线

```
本地 vLLM (内容生成) → ComfyUI (图像生成) → ffmpeg (后处理)
```

这个管线的每一个步骤都可以由不同的 AI 代理协调：

1. **研究代理**：使用 vLLM 生成内容大纲
2. **写作代理**：使用 vLLM 扩充为完整文章
3. **图像代理**：使用 ComfyUI 生成对应插图
4. **整合代理**：将内容和图像组合成最终输出

---

## 步骤 6：自动化与备份

### 6.1 容器备份

```bash
# 备份 ComfyUI 容器状态
docker commit comfyui comfyui-backup:$(date +%Y%m%d)

# 导出镜像
docker save comfyui:latest | gzip > ~/backups/comfyui-$(date +%Y%m%d).tar.gz
```

### 6.2 模型备份

```bash
# 定期备份 HuggingFace 缓存
rsync -avh ~/.cache/huggingface ~/backups/huggingface-cache/

# 或使用 rclone 备份到云端
rclone sync ~/.cache/huggingface remote:backup-huggingface --progress
```

### 6.3 健康检查脚本

创建健康检查 cron job：

```bash
# 每 5 分钟检查一次服务状态
*/5 * * * * curl -f http://localhost:8000/v1/models || echo "vLLM is down at $(date)" | mail -s "vLLM Alert" admin@example.com
```

---

## 常见问题排查

### Q1: Docker 无法使用 GPU

```bash
# 检查 NVIDIA Container Toolkit 是否安装
nvidia-ctk runtime verify

# 重启 Docker 服务
sudo systemctl restart docker
```

### Q2: GPU 内存不足

```bash
# 降低 vLLM 内存使用率
# 在 docker run 指令中加入：
--gpu-memory-utilization 0.7

# 或关闭不必要的服务
sudo systemctl stop bluetooth
```

### Q3: ComfyUI 启动失败

```bash
# 检查 Docker 日志
docker logs comfyui

# 尝试重新启动
docker restart comfyui
```

### Q4: 模型下载太慢

```bash
# 使用 HuggingFace 镜像站（中国大陆用户）
export HF_ENDPOINT=https://hf-mirror.com
```

---

## 下一步

你现在拥有了一套完整的本地 AI 基础设施：

**今天：**
- 确认 vLLM 和 ComfyUI 都能正常运行
- 测试 API 端点，确认可以生成内容和图像

**本周：**
- 设定 systemd 服务确保开机自动启动
- 建立备份和监控机制
- 连接至少一个 LLM 后端到 Cowork MCP

**本月：**
- 探索 [Cowork MCP 框架](https://github.com/slashman413/cowork)，打造更多 AI 代理团队
- 尝试不同的模型，找出最适合你需求的配置
- 建立自己的 AI 内容制作管线

---

## 常见问题解答

**Q：我需要什么等级的 GPU 才能运行这些服务？**
A：建议至少 24GB 内存（RTX 3090/4090）。如果内存较小，可以运行较小的模型（7B-13B）或使用 Docker 的内存限制。

**Q：可以在没有 GPU 的机器上运行吗？**
A：可以，但速度会很慢。CPU 推理是可行的，但对于大型模型（70B+）不实际。

**Q：如何更新模型？**
A：使用 HuggingFace CLI：`huggingface-cli download <model-name> --local-dir <path>`。Docker 容器会自动使用更新的本地模型。

**Q：vLLM 和 Ollama 有什么不同？**
A：vLLM 是针对高吞吐量推理优化的框架，支持更多模型格式和进阶功能。Ollama 更轻量、易于使用，但功能较少。对于本地 AI 基础设施，建议使用 vLLM。

**Q：ComfyUI 和 Automatic1111 有什么区别？**
A：ComfyUI 采用节点式工作流程，更灵活、更高效。Automatic1111 有图形界面，对初学者更友好。两个都可以很好地工作，但 ComfyUI 在生产环境中更受欢迎。

---

*阅读时间：约 15 分钟 | 发布日期：2026-07-27*

*觉得这份指南有帮助？探索 [Slashman Tools](/) 上的更多指南。如果你想快速部署 AI 基础设施，查看我们的 [AI 工具链模板库](https://gumroad.com/l/diwoc) 获取即拿即用的设定档。*

[[- 返回首页](/)]