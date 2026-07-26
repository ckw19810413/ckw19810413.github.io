---
title: "第一个 AI 代理团队构建教程：使用 Cowork MCP 框架逐步实现"
description: "20 分钟内构建你的第一个多 Agent AI 团队。完整实现教程涵盖 Cowork MCP 框架 — 代理配置、任务派发、多平台协作以及真实项目模板。"
slug: "build-ai-agent-team"
layout: "single"
summary: "20 分钟内构建你的第一个 AI 代理团队。完整实现教程 — Cowork MCP 框架配置、285+ 专家代理、任务派发、多平台协作，以及可直接使用的项目模板。"
publishDate: 2026-07-26
updatedDate: 2026-07-26
categories:
  - "AI 框架"
  - "实现教程"
tags:
  - "多 Agent AI"
  - "AI 协调平台"
  - "MCP 框架"
  - "AI 代理团队"
  - "构建 AI 代理"
  - "Cowork"
  - "AI 自动化"
  - "开发者教程"
draft: false
---

## 20 分钟内构建你的第一个 AI 代理团队

如果你在 2026 年关注过 AI 领域，你一定听过这个承诺：多 Agent AI 系统就像一支专家团队，各自处理最擅长的任务。但大多数教程停留在理论层面 — 它们解释了什么是多 Agent 协调，却没有告诉你如何实际构建一个。

这份教程改变这一点。

完成本教程后，你将拥有一个实际运行的多 Agent AI 系统 — 包含已注册的代理、任务队列和真正的仪表板 — 可以用来自动化代码审查、内容制作、市场研究等各种工作。

**你今天会学到：**

- 在机器上运行 Cowork MCP Server
- 拥有 285+ 预设专家代理的阵容
- 派发真正产出结构化报告的多 Agent 任务
- 连接 LLM 后端执行真实工作

我们开始吧。

---

## 前置需求

开始之前，请确认你已准备好：

| 项目 | 版本需求 | 检查指令 |
|------|---------|---------|
| **Node.js** | ≥ 20（建议 v22） | `node --version` |
| **npm** | ≥ 10 | `npm --version` |
| **Git** | 任何版本 | `git --version` |
| **LLM 后端** | 至少一个（Claude、GPT、Gemini 或本地） | — |

就是这样。不需要云端账号、不需要 Docker、不需要复杂的架构。一切都在你的机器上运行。

如果你是 AI 代理的新手，建议先阅读[多 Agent AI 协调平台完整指南](/multi-agent-coworking-platform/)了解基础概念。这份教程会在此基础上进行实现。

---

## 步骤 1：安装并启动 Cowork

Cowork MCP 框架是开源的，只需两个命令即可安装。

```bash
# 克隆仓库及所有代理定义
git clone --recurse-submodules https://github.com/slashman413/cowork
cd cowork/server

# 安装依赖
npm install
```

`--recurse-submodules` 参数至关重要 — 它会拉入 `agency-agents` 子模块，其中包含 285+ 个预编写的代理定义。每个代理都是一个带有 YAML frontmatter 的 `.md` 文件，描述其角色、技能和执行参数。

### 启动服务器

```bash
npm run dev
```

你应该会看到类似以下的输出：

```
🤝 Cowork MCP Server running at http://0.0.0.0:6868
   MCP endpoint: http://0.0.0.0:6868/mcp
   Web Dashboard: http://0.0.0.0:6868/
   REST API: http://0.0.0.0:6868/api/
   Roster loaded: 285 agents across 19 divisions
```

**在浏览器中打开 `http://localhost:6868/`。** 你会看到 Cowork 仪表板 — 代理阵容、任务收件匣和系统状态一目了然。

---

## 步骤 2：了解代理阵容

Cowork 附带 **285+ 专家代理**，组织成 **19 个部门**。每个部门对应一个专业领域：

| 部门 | 代理数量 | 示例代理 |
|------|---------|---------|
| 工程 | 45+ | 代码审查员、系统架构师、DevOps 工程师 |
| 市场 | 30+ | SEO 专员、内容策略师、社交媒体经理 |
| 测试 | 25+ | QA 工程师、渗透测试员、性能审计员 |
| 数据科学 | 20+ | 数据分析师、ML 工程师、可视化专家 |
| 设计 | 15+ | UI 设计师、UX 研究员、品牌设计师 |
| 法务 | 12+ | 合约审查员、合规专员 |
| 财务 | 18+ | 财务分析师、风险评估师、税务专员 |
| 产品 | 10+ | 产品经理、增长黑客、产品营销 |
| *还有 14 个部门...* | | |

每个代理都有明确定义的角色。你可以在仪表板上或透过 `cowork/agency-agents/agents/` 路径浏览完整阵容。

---

## 步骤 3：连接 LLM 后端

Cowork 是一个任务协调器 — 它负责路由任务，但本身不执行 LLM 调用。你需要连接至少一个"大脑"（具备 LLM 能力的平台）来执行代理。

### 选项 A：Hermes Agent（初学者推荐）

如果你已经安装 [Hermes Agent](https://hermes-agent.nousresearch.com)，它可以原生整合：

```bash
hermes register-cowork
```

这会将 Hermes 注册为 Cowork 工作节点，并开放其 39+ 技能和内置工具集。

### 选项 B：Claude Code

将以下配置加入你的 Claude Code MCP 配置文件（`~/.claude.json` 或项目级别的 `claude.json`）：

```json
{
  "mcpServers": {
    "cowork": {
      "url": "http://localhost:6868/mcp",
      "transport": "streamable-http"
    }
  }
}
```

### 选项 C：任何 MCP 兼容客户端

任何支持 Model Context Protocol (MCP) 的客户端 — 包括 Cursor、VS Code 扩展、Gemini CLI 和自定义脚本 — 都可以连接 Cowork 的 `/mcp` 端点。

连接完成后，代理就会显示为可用的工作节点。Cowork 的协调器会处理后续所有工作。

---

## 步骤 4：派发你的第一个多 Agent 任务

现在重头戏来了 — 透过你的代理团队执行实际工作。

### 任务：多 Agent 代码审计

让我们对一个 GitHub 仓库进行三位代理并行审计。从 Cowork 仪表板或透过 API：

```json
{
  "title": "全方位代码审计 - agents-coworking",
  "description": "对 agents-coworking GitHub 仓库进行全面审计：评估代码质量（技术主管）、评估 UX/SEO（增长黑客）、制定行动路线图（产品经理）。",
  "skill": "engineering",
  "tags": ["code-review", "security", "performance"],
  "to_agent": "tech-lead",
  "priority": "high"
}
```

Cowork 的协调器会分三个阶段处理：

**阶段 1 — 分类：** 分类器大脑读取任务描述并判断所属部门。"代码审计"加上 engineering、code-review 标签 → 工程部门。

**阶段 2 — 代理选择：** 在工程部门内，协调器根据技能匹配、专业深度和当前负载评估可用代理，选择最适合的代理。

**阶段 3 — 执行：** 选定的代理在你的 LLM 后端上执行，接收完整的任务描述作为上下文，产出结构化输出 — 通常存储为 `cowork/reports/` 中的 markdown 报告。

你可以从仪表板监控实时进度：

```
━━ 任务：全方位代码审计 ━━
  代理：技术主管 (透过 Hermes Agent)
  状态：工作中...（已运行 3 分钟）
  进度：分析代码结构 → 执行依赖审计
```

### 链式任务：复杂工作流

在生产环境中，你可以将任务链接起来，让一个代理的输出成为下一个代理的输入：

```
研究代理 → 内容写手 → SEO 优化师 → 社群发布者
```

每个代理都会收到前一代理的输出作为上下文。这就是创建自主内容管线、自动化 QA 系统和 AI 驱动产品发布流程的方法。

---

## 步骤 5：查看结果和报告

每个完成的任务都会产生报告。你可以从以下方式存取：

- **从仪表板**：导航到报告 → 列出最近的报告，包含标题、作者和时间戳
- **从文件系统**：`cowork/reports/` 包含完整输出的 markdown 文件
- **从 API**：`GET /api/reports` 返回 JSON 列表

---

## 实用模式 1：自动化代码审查管线

**目标**：每次推送代码到 GitHub 时，Cowork 自动审查你的代码。

**配置：**
1. 创建 Cowork 任务模板
2. 使用 GitHub Action 在每次推送时 POST 到 Cowork 的 API
3. Cowork 分派任务给技术主管和安全代理
4. 结果以 PR 评论形式返回

```yaml
# .github/workflows/cowork-review.yml
on: [pull_request]
jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - name: Dispatch Cowork Review
        run: |
          curl -X POST http://your-server:6868/api/tasks \
            -H "Content-Type: application/json" \
            -d '{
              "title": "PR Review: ${{ github.event.pull_request.title }}",
              "description": "Review PR for security, performance, and code quality",
              "skill": "engineering",
              "tags": ["code-review", "ci-cd"]
            }'
```

---

## 实用模式 2：内容制作团队

对于创作者和营销人员来说，多 Agent 内容管线消除了所有瓶颈：

```
研究代理 → 写手代理 → SEO 代理 → 发布代理
    │           │           │           │
    ├ 主题分析   ├ 博客草稿 ├ Meta 标签  ├ 平台贴文
    ├ 竞争情报   ├ 2000+ 字 ├ Schema    ├ 排程
    └ 关键字研究 └ 语调匹配   └ 内部链接   └ 分析设置
```

每个代理将其输出作为上下文传递给下一个。结果：从主题选择到发布内容，一次协调完成。

想了解更多 AI 驱动的内容策略和提示词，请参考我的 [AI 提示词技巧指南](/ai-prompts-guide/)获取可立即套用的模板。

---

## 实用模式 3：产品上线协调

发布数字产品需要协调研究、内容、技术设置和分析。多 Agent 团队端到端处理这一切：

1. **市场研究代理** — 分析竞争对手、寻找定价缺口、生成竞争情报
2. **内容策略师** — 编写落地页文案、创建推广素材、设计电子邮件序列
3. **技术专员** — 处理部署、支付整合、分析设置
4. **产品经理代理** — 将所有输出整合为上线时间表

这正是我在 [Slashman Tools](/zh-cn/) 上推出新产品时使用的模式。多 Agent 的方法将准备时间从数周缩短到数小时。

---

## 了解 MCP：驱动一切的协议

这一切之所以能够实现，都归功于 **Model Context Protocol (MCP)** — 一个定义 AI 代理如何与工具、服务器和彼此通信的开放标准。

**简单来说：** MCP 就像 AI 代理的 USB-C。就像 USB-C 标准化了设备连接外设的方式，MCP 标准化了 AI 模型连接工具、数据来源和其他代理的方式。

Cowork 透过 **Streamable HTTP** 实现 MCP — 一种轻量传输方式，无需持续的 WebSocket 连接就能与任何 HTTP 客户端配合使用。这让它可以轻松整合到 CI/CD 管线、无服务器函数和边缘计算环境中。

想构建自定义集成的开发者，[Cowork 仓库](https://github.com/slashman413/cowork)记录了完整的 MCP 工具列表 — 包括 `create_task`、`register_agent`、`get_roster`、`claim_task`、`complete_task`、`file_report`、`heartbeat` 等。

---

## 选择正确的代理架构

并非每个项目都需要 285 个代理。以下是决策框架：

### 单一项目团队（1-3 个代理）
- **适合**：小型仓库、个人项目、个人创作者
- **配置**：连接一个 LLM 后端，使用 3-5 个代理角色
- **示例**：代码审查员 + 写手 + 研究员

### 部门级团队（5-20 个代理）
- **适合**：小团队、创业公司、代理商
- **配置**：多个 LLM 后端、部门专属代理
- **示例**：完整工程部门 + 市场团队 + 数据分析师

### 企业级团队（50+ 个代理）
- **适合**：产品公司、大型内容运营
- **配置**：远程大脑注册、自定义代理编写、API 自动化
- **示例**：全部 19 个部门、多平台 LLM 路由、CI/CD 整合

Cowork 可扩展到所有三个层级 — 从规模开始，随着需求增长增加代理。

---

## 常见陷阱

在生产环境中使用多 Agent 系统数月后，以下是我最常见的错误：

### 1. 代理太多，上下文太少
不要让 20 个代理处理简单任务。每个代理都会增加延迟和上下文开销。从 2-3 个代理开始，只有在确定需要时才增加。

### 2. 忽略代理角色质量
编写不良的代理定义会产生不良结果。投入时间精心设计精确的角色描述、技能列表和指令提示。Cowork 现有的 285 个代理都是经过精心设计的 — 把它们当作模板。

### 3. 任务丢失完成追踪
始终设置完成追踪。Cowork 的仪表板一目了然，但对于长时间运行的工作流程也应设置通知。

### 4. 单一供应商依赖
至少连接两个 LLM 后端。如果一个平台故障或受到速率限制，你的代理团队会切换到另一个。Cowork 会自动处理多平台路由。

### 5. 关键决策缺少人机协作
对于安全审计、财务分析或法律审查 — 在根据 AI 输出采取行动前，务必让人类审查。代理是强大的助手，但不是高风险工作领域的自主决策者。

---

## 下一步

你现在有了一个运行中的多 Agent AI 系统。以下是下一步：

**今天：**
- 探索 `http://localhost:6868/` 的仪表板
- 派发 3 个不同任务给不同代理
- 浏览代理阵容，找出你没预料到的专家

**本周：**
- 连接第二个 LLM 后端以备冗余
- 创建一个自定义代理定义（复制现有 `.md` 文件并修改）
- 设置一个每日市场研究或代码审查的定期任务

**本月：**
- 将 Cowork 整合到你的 CI/CD 管线中
- 创建一个多步骤工作流（3+ 个代理依次执行）
- 探索 [Cowork 文档](https://github.com/slashman413/cowork)了解高级功能，如远程大脑注册和自定义执行器

完整的[多 Agent AI 协调平台指南](/multi-agent-coworking-platform/)涵盖架构、使用案例及与其他框架的比较 — 接下来阅读它以获得策略性概述。

---

## 常见问题

**Q：我需要会 Python 或 AI 工程才能使用 Cowork 吗？**
A：不需要。如果你能执行 `git clone` 和 `npm install`，就能配置 Cowork。代理阵列是预配置的。

**Q：我可以在云端服务器上运行 Cowork 吗？**
A：可以。Cowork 可以在任何安装 Node.js 的机器上运行。部署到 VPS、云端 VM 或树莓派。仪表板和 MCP 端点可通过网络存取。

**Q：可以同时运行多少个代理？**
A：Cowork 不限制并发数 — 限制来自你的 LLM 后端和硬件。配备现代 GPU 的单一机器可以并行运行 5-10 个代理。配备多个后端的企业级配置可以扩展到更高。

**Q：Cowork 是免费开源的吗？**
A：是的。Cowork 采用 MIT 授权，可在 [GitHub](https://github.com/slashman413/cowork) 上取得。没有付费方案、没有隐藏限制。

**Q：Cowork 和 CrewAI/AutoGen 有什么不同？**
A：Cowork 专注于广度 — 跨 19 个部门的 285+ 预配置代理、多平台 LLM 支持和文件系统优先的架构。CrewAI 擅长顺序代理链；AutoGen 擅长对话式多代理模式。Cowork 的优势是即时存取精心策划的专家阵容。

---

## 结论：你的 AI 代理团队已经准备好了

多 Agent AI 协调不是未来技术 — 它是你今天就能使用的工具。在 20 分钟内，你已经从零到运行中的多 Agent 系统，拥有 285 个专家可供调度。

关键洞察是：**一个 AI 模型是通才。一支 AI 代理团队是专家组织。** 透过 MCP 协议协调专家代理，你可以自动化通常需要一整支人类团队才能完成的复杂工作流 — 代码审计、内容制作、市场研究、产品发布 — 在数分钟内完成而非数天。

Cowork MCP 框架让这一切变得实用。它是开源的、可自架、可在任何安装 Node.js 的机器上运行。没有供应商锁定、没有云端依赖。只有一个干净、模块化的系统，随着你的需求成长。

**[在 GitHub 上克隆 Cowork](https://github.com/slashman413/cowork)，今天就构建你的第一个 AI 代理团队。**

---

*阅读时间：12 分钟 | 发布日期：2026-07-26 | 最后更新：2026-07-26*

*觉得这份教程有帮助？探索 [Slashman Tools](/zh-cn/) 上的更多指南。如果你想要即拿即用的 AI 提示词模板，涵盖开发、内容创作和商业自动化，请查看 [AI Prompt Library](/zh-cn/products/ai-prompt-library/)。*

[[返回首页](/zh-cn/)]