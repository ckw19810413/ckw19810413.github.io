---
title: "本地 AI 基礎設施建置指南：從 0 到 vLLM + ComfyUI 完整部署"
description: "2026 年如何在一台機器上建置完整的本地 AI 基礎設施。從 vLLM 大型語言模型到 ComfyUI 圖像生成，手把手教學涵蓋安裝、優化、自動化部署，以及與 Cowork MCP 整合。"
slug: "local-ai-infrastructure-guide"
layout: "single"
summary: "完整實作指南：使用 DGX GB10 或單 GPU 機器建置本地 AI 基礎設施。涵蓋 vLLM 部署、ComfyUI 安裝、記憶體管理、自動化服務以及與多 Agent 框架整合的步驟。"
publishDate: 2026-07-27
updatedDate: 2026-07-27
categories:
  - "AI 基礎設施"
  - "實作教學"
tags:
  - "本地 AI"
  - "vLLM"
  - "ComfyUI"
  - "AI 部署"
  - "GPU 優化"
  - "AI 基礎設施"
  - "機器學習"
  - "AI 工具鏈"
draft: false
---

## 為什麼要建置本地 AI 基礎設施？

2026 年，AI 工具已經成為數位創作者、開發者和企業的基礎設施。但大多數人仍然依賴雲端 API — 每次呼叫花錢、每次傳輸冒隱私風險、每次被速率限制卡住脖子。

本地 AI 基礎設施給你三樣東西：**完全的控制權、無限制的用量、零边际成本**。

一旦建置完成，你可以：
- 無限制使用 LLM，不用擔心 API 費用
- 處理敏感資料，不用離開你的機器
- 同時運行多個服務，沒有速率限制
- 與 Cowork MCP 等框架整合，打造真正的 AI 代理團隊

這份指南假設你已經有一台帶有 GPU 的機器（推薦 DGX GB10、RTX 4090 或更好）。我會從零開始，一步步帶你建置完整的本地 AI 環境。

**你今天會學到：**

- 安裝和配置本地 LLM 服務（vLLM）
- 部署 ComfyUI 圖像生成管道
- 管理 GPU 記憶體和服務啟動順序
- 自動化服務管理（systemd）
- 與 Cowork MCP 整合，打造多 Agent 系統

我們開始吧。

---

## 前置需求

開始之前，請確認你已準備好：

| 項目 | 版本需求 | 檢查指令 |
|------|---------|---------|
| **Linux** | Ubuntu 22.04+ 或 Arch | `uname -a` |
| **GPU** | NVIDIA RTX 3090+/4090/GB10 | `nvidia-smi` |
| **CUDA** | ≥ 12.4 | `nvcc --version` |
| **Docker** | ≥ 24.0 | `docker --version` |
| **Node.js** | ≥ 20 | `node --version` |
| **Python** | ≥ 3.10 | `python3 --version` |

如果你的 GPU 記憶體不足 24GB，建議關閉不必要的圖形介面或服務再開始。

---

## 步驟 1：安裝 Docker 和 NVIDIA Container Toolkit

Docker 是部署本地 AI 服務的推薦方式，因為它能隔離依賴、版本衝突和系統污染。

```bash
# 安裝 Docker
sudo apt update
sudo apt install -y docker.io docker-compose-v2

# 安裝 NVIDIA Container Toolkit（讓 Docker 可以使用 GPU）
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

驗證 GPU 可用性：

```bash
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

如果看到 GPU 資訊和記憶體使用率，就代表環境設定正確。

---

## 步驟 2：部署 vLLM 本地語言模型

vLLM 是當前最高效的本地 LLM 推理框架，支援多種模型格式（GGUF、GPTQ、AWQ）。

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

**引數說明：**
- `--model`: 要部署的模型（可替換為任何 HuggingFace 模型）
- `--gpu-memory-utilization`: 使用 GPU 記憶體的比例（0.9 表示 90%）
- `--max-model-len`: 最大上下文長度

> **注意：** 如果你的 GPU 記憶體小於 80GB，建議從較小的模型開始（7B 或 13B），然後再嘗試更大的模型。

### 2.2 測試 API 端點

```bash
curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nvidia/Llama-3.1-Nemotron-70B-Instruct",
    "prompt": "解釋什麼是多 Agent AI 系統",
    "max_tokens": 200
  }'
```

如果收到回應，vLLM 已經成功部署。

### 2.3 設定為系統服務（自動啟動）

創建 systemd 服務檔案：

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

啟用並啟動服務：

```bash
sudo systemctl daemon-reload
sudo systemctl enable vllm.service
sudo systemctl start vllm.service
```

---

## 步驟 3：部署 ComfyUI 圖像生成

ComfyUI 是當前最強大的本地圖像生成工具，支援 Flux、Stable Diffusion、LTX 等各種模型。

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

這會在 `http://localhost:8188` 啟動 ComfyUI。

### 3.2 手動安裝（進階選項）

如果你需要更多控制，可以選擇手動安裝：

```bash
# 複製 ComfyUI 倉庫
cd ~/comfyui
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# 安裝依賴
pip install -r requirements.txt

# 安裝自訂節點（可選）
git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation.git custom_nodes/
git clone https://github.com/laksjdjoy/deforum-comfy.git custom_nodes/

# 啟動服務
python main.py --listen 0.0.0.0 --port 8188
```

### 3.3 常用模型下載

```bash
# 使用 HuggingFace CLI 下載模型
pip install huggingface_hub
huggingface-cli download stabilityai/stable-diffusion-xl-base-1.0 --local-dir ~/models/sdxl
huggingface-cli download stabilityai/stable-diffusion-3.5-large --local-dir ~/models/sd3.5
```

---

## 步驟 4：GPU 記憶體管理策略

在本地部署 AI 服務時，GPU 記憶體是最大的瓶頸。以下是幾個實戰經驗：

### 4.1 檢查可用記憶體

```bash
free -h
nvidia-smi --query-gpu=memory.used,memory.free --format=csv
```

### 4.2 服務啟動順序建議

1. **先啟動 vLLM**（語言模型通常記憶體需求較固定）
2. **後啟動 ComfyUI**（圖像生成可以動態調整記憶體使用）
3. **關閉不必要的圖形應用**（瀏覽器、Discord 等）

### 4.3 記憶體監控腳本

創建一個簡單的監控腳本：

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

## 步驟 5：整合 Cowork MCP 多 Agent 框架

一旦本地 AI 基礎設施就緒，就可以連接 Cowork MCP 打造多 Agent 系統。

### 5.1 註冊 vLLM 作為大腦

```bash
# 如果使用 Hermes Agent
hermes register-cowork

# 或者手動設定 MCP 端點
# 在你的 Agent 設定檔中添加：
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

### 5.2 實際應用：本地 AI 內容製作管道

```
本地 vLLM (內容生成) → ComfyUI (圖像生成) → ffmpeg (後處理)
```

這個管道的每一個步驟都可以由不同的 AI 代理協調：

1. **研究代理**：使用 vLLM 生內容內容大綱
2. **寫作代理**：使用 vLLM 擴充為完整文章
3. **圖像代理**：使用 ComfyUI 生成對應插圖
4. **整合代理**：將內容和圖像組合成最終輸出

---

## 步驟 6：自動化與備份

### 6.1 容器備份

```bash
# 備份 ComfyUI 容器狀態
docker commit comfyui comfyui-backup:$(date +%Y%m%d)

# 匯出映像
docker save comfyui:latest | gzip > ~/backups/comfyui-$(date +%Y%m%d).tar.gz
```

### 6.2 模型備份

```bash
# 定期備份 HuggingFace 快取
rsync -avh ~/.cache/huggingface ~/backups/huggingface-cache/

# 或使用 rclone 備份到雲端
rclone sync ~/.cache/huggingface remote:backup-huggingface --progress
```

### 6.3 健康檢查腳本

創建健康檢查 cron job：

```bash
# 每 5 分鐘檢查一次服務狀態
*/5 * * * * curl -f http://localhost:8000/v1/models || echo "vLLM is down at $(date)" | mail -s "vLLM Alert" admin@example.com
```

---

## 常見問題排查

### Q1: Docker 無法使用 GPU

```bash
# 檢查 NVIDIA Container Toolkit 是否安裝
nvidia-ctk runtime verify

# 重啟 Docker 服務
sudo systemctl restart docker
```

### Q2: GPU 記憶體不足

```bash
# 降低 vLLM 記憶體使用率
# 在 docker run 指令中加入：
--gpu-memory-utilization 0.7

# 或關閉不必要的服務
sudo systemctl stop bluetooth
```

### Q3: ComfyUI 啟動失敗

```bash
# 檢查 Docker 日誌
docker logs comfyui

# 嘗試重新啟動
docker restart comfyui
```

### Q4: 模型下載太慢

```bash
# 使用 HuggingFace 鏡像站（中国大陆用戶）
export HF_ENDPOINT=https://hf-mirror.com
```

---

## 下一步

你現在擁有一套完整的本地 AI 基礎設施：

**今天：**
- 確認 vLLM 和 ComfyUI 都能正常運作
- 測試 API 端點，確認可以生成內容和圖像

**本週：**
- 設定 systemd 服務確保開機自動啟動
- 建立備份和監控機制
- 連接至少一個 LLM 後端到 Cowork MCP

**本月：**
- 探索 [Cowork MCP 框架](https://github.com/slashman413/cowork)，打造更多 AI 代理團隊
- 嘗試不同的模型，找出最適合你需求的配置
- 建立自己的 AI 內容製作管道

---

## 常見問答

**Q：我需要什麼等級的 GPU 才能运行這些服務？**
A：建議至少 24GB 記憶體（RTX 3090/4090）。如果記憶體較小，可以運行較小的模型（7B-13B）或使用 Docker 的記憶體限制。

**Q：可以在沒有 GPU 的機器上運行嗎？**
A：可以，但速度會很慢。CPU 推理是可行的，但對於大型模型（70B+）不實際。

**Q：如何更新模型？**
A：使用 HuggingFace CLI：`huggingface-cli download <model-name> --local-dir <path>`。Docker 容器會自動使用更新的本地模型。

**Q：vLLM 和 Ollama 有什麼不同？**
A：vLLM 是針對高吞吐量推理優化的框架，支援更多模型格式和進階功能。Ollama 更輕量、易於使用，但功能較少。對於本地 AI 基礎設施，建議使用 vLLM。

**Q：ComfyUI 和 Automatic1111 有什麼區別？**
A：ComfyUI 採用節點式工作流程，更靈活、更高效。Automatic1111 有圖形介面，對初學者更友好。兩個都可以很好地工作，但 ComfyUI 在生產環境中更受歡迎。

---

*閱讀時間：約 15 分鐘 | 發布日期：2026-07-27*

*覺得這份指南有幫助？探索 [Slashman Tools](/zh-tw/) 上的更多指南。如果你想快速部署 AI 基礎設施，查看我們的 [AI 工具鏈模板庫](/zh-twhttps://gumroad.com/l/diwoc) 獲取即拿即用的設定檔。*

[[- 返回首頁](/zh-tw/)]