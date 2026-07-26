---
title: "第一個 AI 代理團隊建置教學：使用 Cowork MCP 框架逐步實作"
description: "20 分鐘內建置你的第一個多 Agent AI 團隊。完整實作教學涵蓋 Cowork MCP 框架 — 代理設定、任務分派、多平台協作以及真實專案範本。"
slug: "build-ai-agent-team"
layout: "single"
summary: "20 分鐘內建置你的第一個 AI 代理團隊。完整實作教學 — Cowork MCP 框架設定、285+ 專家代理人、任務分派、多平台協作，以及可直接使用的專案範本。"
publishDate: 2026-07-26
updatedDate: 2026-07-26
categories:
  - "AI 框架"
  - "實作教學"
tags:
  - "多 Agent AI"
  - "AI 協調平台"
  - "MCP 框架"
  - "AI 代理團隊"
  - "建置 AI 代理"
  - "Cowork"
  - "AI 自動化"
  - "開發者教學"
draft: false
---

## 20 分鐘內建置你的第一個 AI 代理團隊

如果你在 2026 年關注過 AI 領域，你一定聽過這個承諾：多 Agent AI 系統就像一支專家團隊，各自處理最擅長的工作。但大多數教學停留在理論層面 — 它們解釋了什麼是多 Agent 協調，卻沒有告訴你如何實際建置一個。

這份教學改變這一點。

完成本教學後，你將擁有一個實際運行的多 Agent AI 系統 — 包含已註冊的代理人、任務佇列和真正的儀表板 — 可以用來自動化程式碼審查、內容製作、市場研究等各種工作。

**你今天會學到：**

- 在機器上運行 Cowork MCP Server
- 擁有 285+ 預設專家代理人的陣容
- 分派真正產出結構化報告的多 Agent 任務
- 連接 LLM 後端執行真實工作

我們開始吧。

---

## 前置需求

開始之前，請確認你已準備好：

| 項目 | 版本需求 | 檢查指令 |
|------|---------|---------|
| **Node.js** | ≥ 20（建議 v22） | `node --version` |
| **npm** | ≥ 10 | `npm --version` |
| **Git** | 任何版本 | `git --version` |
| **LLM 後端** | 至少一個（Claude、GPT、Gemini 或本地） | — |

就是這樣。不需要雲端帳號、不需要 Docker、不需要複雜的基礎設施。一切都在你的機器上運行。

如果你是 AI 代理的新手，建議先閱讀[多 Agent AI 協調平台完整指南](/multi-agent-coworking-platform/)了解基礎概念。這份教學會在此基礎上進行實作。

---

## 步驟 1：安裝並啟動 Cowork

Cowork MCP 框架是開源的，只需兩個指令即可安裝。

```bash
# 複製倉庫及所有代理定義
git clone --recurse-submodules https://github.com/slashman413/cowork
cd cowork/server

# 安裝依賴
npm install
```

`--recurse-submodules` 參數至關重要 — 它會拉入 `agency-agents` 子模組，其中包含 285+ 個預先編寫的代理定義。每個代理都是一個帶有 YAML frontmatter 的 `.md` 檔案，描述其角色、技能和執行參數。

### 啟動伺服器

```bash
npm run dev
```

你應該會看到類似以下的輸出：

```
🤝 Cowork MCP Server running at http://0.0.0.0:6868
   MCP endpoint: http://0.0.0.0:6868/mcp
   Web Dashboard: http://0.0.0.0:6868/
   REST API: http://0.0.0.0:6868/api/
   Roster loaded: 285 agents across 19 divisions
```

**在瀏覽器中開啟 `http://localhost:6868/`。** 你會看到 Cowork 儀表板 — 代理陣容、任務收件匣和系統狀態一目了然。

---

## 步驟 2：了解代理陣容

Cowork 附帶 **285+ 專家代理人**，組織成 **19 個部門**。每個部門對應一個專業領域：

| 部門 | 代理數量 | 範例代理人 |
|------|---------|-----------|
| 工程 | 45+ | 程式碼審查員、系統架構師、DevOps 工程師 |
| 行銷 | 30+ | SEO 專員、內容策略師、社群媒體經理 |
| 測試 | 25+ | QA 工程師、滲透測試員、效能審計員 |
| 資料科學 | 20+ | 資料分析師、ML 工程師、視覺化專家 |
| 設計 | 15+ | UI 設計師、UX 研究員、品牌設計師 |
| 法務 | 12+ | 合約審查員、合規專員 |
| 財務 | 18+ | 財務分析師、風險評估師、稅務專員 |
| 產品 | 10+ | 產品經理、成長駭客、產品行銷 |
| *還有 14 個部門...* | | |

每個代理都有明確定義的角色。你可以在儀表板上或透過 `cowork/agency-agents/agents/` 路徑瀏覽完整陣容。

---

## 步驟 3：連接 LLM 後端

Cowork 是一個任務協調器 — 它負責路由工作，但本身不執行 LLM 呼叫。你需要連接至少一個「大腦」（具備 LLM 能力的平台）來執行代理。

### 選項 A：Hermes Agent（初學者推薦）

如果你已經安裝 [Hermes Agent](https://hermes-agent.nousresearch.com)，它可以原生整合：

```bash
hermes register-cowork
```

這會將 Hermes 註冊為 Cowork 工作節點，並開放其 39+ 技能和內建工具組。

### 選項 B：Claude Code

將以下設定加入你的 Claude Code MCP 設定檔（`~/.claude.json` 或專案層級的 `claude.json`）：

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

### 選項 C：任何 MCP 相容用戶端

任何支援 Model Context Protocol (MCP) 的用戶端 — 包括 Cursor、VS Code 擴充功能、Gemini CLI 和自訂腳本 — 都可以連接 Cowork 的 `/mcp` 端點。

連接完成後，代理就會顯示為可用的工作節點。Cowork 的協調器會處理後續所有工作。

---

## 步驟 4：分派你的第一個多 Agent 任務

現在是重頭戲 — 透過你的代理團隊執行實際工作。

### 任務：多 Agent 程式碼審計

讓我們對一個 GitHub 倉庫進行三位代理平行審計。從 Cowork 儀表板或透過 API：

```json
{
  "title": "全方位程式碼審計 - agents-coworking",
  "description": "對 agents-coworking GitHub 倉庫進行全面審計：評估程式碼品質（技術主管）、評估 UX/SEO（成長駭客）、建立行動路線圖（產品經理）。",
  "skill": "engineering",
  "tags": ["code-review", "security", "performance"],
  "to_agent": "tech-lead",
  "priority": "high"
}
```

Cowork 的協調器會分三個階段處理：

**階段 1 — 分類：** 分類器大腦閱讀任務描述並判斷所屬部門。「程式碼審計」加上 engineering、code-review 標籤 → 工程部門。

**階段 2 — 代理選擇：** 在工程部門內，協調器根據技能匹配、專業深度和當前負載評估可用代理人，選擇最適合的代理。

**階段 3 — 執行：** 選定的代理在你的 LLM 後端上執行，接收完整的任務描述作為上下文，產出結構化輸出 — 通常儲存為 `cowork/reports/` 中的 markdown 報告。

你可以從儀表板監控即時進度：

```
━━ 任務：全方位程式碼審計 ━━
  代理：技術主管 (透過 Hermes Agent)
  狀態：工作中...（已運行 3 分鐘）
  進度：分析程式碼結構 → 執行依賴審計
```

### 鏈式任務：複雜工作流程

在生產環境中，你可以將任務鏈接起來，讓一個代理的輸出成為下一個代理的輸入：

```
研究代理 → 內容寫手 → SEO 優化師 → 社群發布者
```

每個代理都會收到前一代理的輸出作為上下文。這就是建立自主內容管線、自動化 QA 系統和 AI 驅動產品發布流程的方法。

---

## 步驟 5：查看結果和報告

每個完成的任務都會產生報告。你可以從以下方式存取：

- **從儀表板**：導航到報告 → 列出最近的報告，包含標題、作者和時間戳
- **從檔案系統**：`cowork/reports/` 包含完整輸出的 markdown 檔案
- **從 API**：`GET /api/reports` 回傳 JSON 列表

---

## 實用模式 1：自動化程式碼審查管線

**目標**：每次推送程式碼到 GitHub 時，Cowork 自動審查你的程式碼。

**設定**：
1. 建立 Cowork 任務範本
2. 使用 GitHub Action 在每次推送時 POST 到 Cowork 的 API
3. Cowork 分派任務給技術主管和安全代理
4. 結果以 PR 評論形式回傳

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

## 實用模式 2：內容製作團隊

對創作者和行銷人員來說，多 Agent 內容管線消除了所有瓶頸：

```
研究代理 → 寫手代理 → SEO 代理 → 發布代理
    │           │           │           │
    ├ 主題分析   ├ 部落格草稿 ├ Meta 標籤  ├ 平台貼文
    ├ 競爭情報   ├ 2000+ 字  ├ Schema    ├ 排程
    └ 關鍵字研究 └ 語調匹配   └ 內部連結   └ 分析設定
```

每個代理將其輸出作為上下文傳遞給下一個。結果：從主題選擇到發布內容，一次協調完成。

想了解更多 AI 驅動的內容策略和提示詞，請參考我的 [AI 提示詞技巧指南](/ai-prompts-guide/)獲取可立即套用的範本。

---

## 實用模式 3：產品上市協調

發布數位產品需要協調研究、內容、技術設定和分析。多 Agent 團隊端到端處理這一切：

1. **市場研究代理** — 分析競爭對手、找出定價缺口、生成競爭情報
2. **內容策略師** — 編寫登陸頁面文案、建立推廣素材、設計電子郵件序列
3. **技術專員** — 處理部署、付款整合、分析設定
4. **產品經理代理** — 將所有輸出整合為上市時間表

這正是我在 [Slashman Tools](/zh-tw/) 上推出新產品時使用的模式。多 Agent 的方法將準備時間從數週縮短到數小時。

---

## 了解 MCP：驅動一切的協定

這一切之所以能夠實現，都歸功於 **Model Context Protocol (MCP)** — 一個定義 AI 代理如何與工具、伺服器和彼此通訊的開放標準。

**簡單來說：** MCP 就像 AI 代理的 USB-C。就像 USB-C 標準化了裝置連接周邊的方式，MCP 標準化了 AI 模型連接工具、資料來源和其他代理的方式。

Cowork 透過 **Streamable HTTP** 實現 MCP — 一種輕量傳輸方式，無需持續的 WebSocket 連線就能與任何 HTTP 用戶端配合使用。這讓它能夠輕鬆整合到 CI/CD 管線、無伺服器函式和邊緣運算環境中。

對想建立自訂整合的開發者，[Cowork 倉庫](https://github.com/slashman413/cowork)記錄了完整的 MCP 工具列表 — 包括 `create_task`、`register_agent`、`get_roster`、`claim_task`、`complete_task`、`file_report`、`heartbeat` 等。

---

## 選擇正確的代理架構

並非每個專案都需要 285 個代理。以下是決策框架：

### 單一專案團隊（1-3 個代理）
- **適合**：小型儲存庫、個人專案、個人創作者
- **設定**：連接一個 LLM 後端，使用 3-5 個代理角色
- **範例**：程式碼審查員 + 寫手 + 研究員

### 部門級團隊（5-20 個代理）
- **適合**：小團隊、新創公司、代理商
- **設定**：多個 LLM 後端、部門專屬代理
- **範例**：完整工程部門 + 行銷團隊 + 資料分析師

### 企業級團隊（50+ 個代理）
- **適合**：產品公司、大型內容營運
- **設定**：遠端大腦註冊、自訂代理編寫、API 自動化
- **範例**：全部 19 個部門、多平台 LLM 路由、CI/CD 整合

Cowork 可擴展到所有三個層級 — 從小規模開始，隨著需求成長增加代理。

---

## 常見陷阱

在生產環境中使用多 Agent 系統數月後，以下是我最常見的錯誤：

### 1. 代理太多，上下文太少
不要讓 20 個代理處理簡單任務。每個代理都會增加延遲和上下文開銷。從 2-3 個代理開始，只有在確定需要時才增加。

### 2. 忽略代理角色品質
編寫不良的代理定義會產生不良結果。投入時間精心設計精確的角色描述、技能清單和指令提示。Cowork 現有的 285 個代理都是經過精心設計的 — 把它們當作範本。

### 3. 任務遺失完成追蹤
始終設定完成追蹤。Cowork 的儀表板一目了然，但對於長時間運行的工作流程也應設定通知。

### 4. 單一供應商依賴
至少連接兩個 LLM 後端。如果一個平台故障或受到速率限制，你的代理團隊會切換到另一個。Cowork 會自動處理多平台路由。

### 5. 關鍵決策缺少人機協作
對於安全審計、財務分析或法律審查 — 在根據 AI 輸出採取行動前，務必讓人類審查。代理是強大的助手，但不是高風險工作領域的自主決策者。

---

## 下一步

你現在有了一個運行中的多 Agent AI 系統。以下是下一步：

**今天：**
- 探索 `http://localhost:6868/` 的儀表板
- 分派 3 個不同任務給不同代理
- 瀏覽代理陣容，找出你沒預料到的專家

**本週：**
- 連接第二個 LLM 後端以備冗餘
- 建立一個自訂代理定義（複製現有 `.md` 檔案並修改）
- 設定一個每日市場研究或程式碼審查的定期任務

**本月：**
- 將 Cowork 整合到你的 CI/CD 管線中
- 建立一個多步驟工作流程（3+ 個代理依序執行）
- 探索 [Cowork 文件](https://github.com/slashman413/cowork)了解進階功能，如遠端大腦註冊和自訂執行器

完整的[多 Agent AI 協調平台指南](/multi-agent-coworking-platform/)涵蓋架構、使用案例及與其他框架的比較 — 接下來閱讀它以獲得策略性概述。

---

## 常見問答

**Q：我需要會 Python 或 AI 工程才能使用 Cowork 嗎？**
A：不需要。如果你能執行 `git clone` 和 `npm install`，就能設定 Cowork。代理陣列是預先配置好的。

**Q：我可以在雲端伺服器上運行 Cowork 嗎？**
A：可以。Cowork 可以在任何安裝 Node.js 的機器上運行。部署到 VPS、雲端 VM 或樹莓派。儀表板和 MCP 端點可透過網路存取。

**Q：可以同時運行多少個代理？**
A：Cowork 不限制並發數 — 限制來自你的 LLM 後端和硬體。配備現代 GPU 的單一機器可以並行運行 5-10 個代理。配備多個後端的企業級設定可以擴展到更高。

**Q：Cowork 是免費開源的嗎？**
A：是的。Cowork 採用 MIT 授權，可在 [GitHub](https://github.com/slashman413/cowork) 上取得。沒有付費方案、沒有隱藏限制。

**Q：Cowork 和 CrewAI/AutoGen 有什麼不同？**
A：Cowork 專注於廣度 — 跨 19 個部門的 285+ 預配置代理、多平台 LLM 支援和檔案系統優先的架構。CrewAI 擅長順序代理鏈；AutoGen 擅長對話式多代理模式。Cowork 的優勢是即時存取精心策劃的專家陣容。

---

## 結論：你的 AI 代理團隊已經準備好了

多 Agent AI 協調不是未來技術 — 它是你今天就能使用的工具。在 20 分鐘內，你已經從零到一個運行中的多 Agent 系統，擁有 285 個專家可供調度。

關鍵洞察是：**一個 AI 模型是通才。一支 AI 代理團隊是專家組織。** 透過 MCP 協定協調專家代理，你可以自動化通常需要一整個人類團隊才能完成的複雜工作流程 — 程式碼審計、內容製作、市場研究、產品發布 — 在數分鐘內完成而非數天。

Cowork MCP 框架讓這一切變得實用。它是開源的、可自架、可在任何安裝 Node.js 的機器上運行。沒有供應商鎖定、沒有雲端依賴。只有一個乾淨、模組化的系統，隨著你的需求成長。

**[在 GitHub 上複製 Cowork](https://github.com/slashman413/cowork)，今天就建置你的第一個 AI 代理團隊。**

---

*閱讀時間：12 分鐘 | 發布日期：2026-07-26 | 最後更新：2026-07-26*

*覺得這份教學有幫助？探索 [Slashman Tools](/zh-tw/) 上的更多指南。如果你想要即拿即用的 AI 提示詞範本，涵蓋開發、內容創作和商業自動化，請查看 [AI Prompt Library](/zh-tw/products/ai-prompt-library/)。*

[[返回首頁](/zh-tw/)]
