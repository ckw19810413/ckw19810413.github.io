---
title: "Build Your First AI Agent Team: A Hands-On Tutorial with Cowork MCP Framework"
description: "Build your first multi-agent AI team step by step. Master the Cowork MCP framework to orchestrate agents for code review, content creation, and automation."
slug: "build-ai-agent-team"
layout: "single"
summary: "Build your first AI agent team in 20 minutes. Complete hands-on tutorial covering the Cowork MCP framework — agent setup, task dispatch, multi-platform orchestration, and real project templates."
publishDate: 2026-07-26
updatedDate: 2026-07-26
categories:
  - "AI Frameworks"
  - "Tutorials"
tags:
  - "multi-agent AI"
  - "AI orchestration"
  - "MCP framework"
  - "AI agent team"
  - "build AI agent"
  - "Cowork"
  - "AI automation"
  - "developer tutorial"
draft: false
---

## Build Your First AI Agent Team in Under 20 Minutes

If you've been following the AI landscape in 2026, you've heard the promise: multi-agent AI systems work like a team of specialists, each handling what they do best. But most tutorials stop at theory. They explain *what* multi-agent orchestration is, without showing you *how* to actually build one.

This guide changes that.

By the end of this tutorial, you'll have a running multi-agent AI system — complete with registered agents, a task queue, and a real dashboard — that you can use to automate code reviews, content production, market research, and more.

**What you'll build today:**

- A Cowork MCP Server running on your machine
- An agent roster with 285+ pre-configured specialist agents
- A dispatched multi-agent task that produces a structured report
- A connected LLM backend executing real work

Let's get started.

---

## Prerequisites: What You Need

Before we dive in, make sure you have:

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| **Node.js** | ≥ 20 (v22 recommended) | `node --version` |
| **npm** | ≥ 10 | `npm --version` |
| **Git** | Any recent version | `git --version` |
| **LLM backend** | At least one (Claude, GPT, Gemini, or local) | — |

That's it. No cloud account required. No Docker. No complex infrastructure. Everything runs locally on your machine.

If you're new to AI agents entirely, I recommend first reading the [Multi-Agent AI Orchestration Complete Guide](/multi-agent-coworking-platform/) for the foundational concepts. This tutorial builds on that with hands-on execution.

---

## Step 1: Install and Launch Cowork

The Cowork MCP framework is open-source and installs in two commands.

```bash
# Clone the repository with all agent definitions
git clone --recurse-submodules https://github.com/slashman413/cowork
cd cowork/server

# Install dependencies
npm install
```

The `--recurse-submodules` flag is critical — it pulls in the `agency-agents` submodule containing 285+ pre-written agent definitions. Each agent is a `.md` file with YAML frontmatter describing its role, skills, and execution parameters.

### Start the Server

```bash
npm run dev
```

You should see output confirmation:

```
🤝 Cowork MCP Server running at http://0.0.0.0:6868
   MCP endpoint: http://0.0.0.0:6868/mcp
   Web Dashboard: http://0.0.0.0:6868/
   REST API: http://0.0.0.0:6868/api/
   Roster loaded: 285 agents across 19 divisions
```

**Open your browser to `http://localhost:6868/`.** You'll see the Cowork dashboard — agent roster, task inbox, and system status at a glance.

{{< figure src="cowork-dashboard.png" alt="Cowork MCP Framework Dashboard showing agent roster and task management interface" caption="The Cowork Web UI dashboard — your command center for multi-agent orchestration." >}}

---

## Step 2: Understand the Agent Roster

Cowork ships with **285+ expert agents** organized into **19 divisions**. Each division corresponds to a professional domain:

| Division | Agent Count | Sample Agents |
|----------|-------------|---------------|
| Engineering | 45+ | Code Reviewer, System Architect, DevOps Engineer |
| Marketing | 30+ | SEO Specialist, Content Strategist, Social Media Manager |
| Testing | 25+ | QA Engineer, Penetration Tester, Performance Auditor |
| Data Science | 20+ | Data Analyst, ML Engineer, Visualization Expert |
| Design | 15+ | UI Designer, UX Researcher, Brand Designer |
| Legal | 12+ | Contract Reviewer, Compliance Specialist |
| Finance | 18+ | Financial Analyst, Risk Assessor, Tax Specialist |
| Product | 10+ | Product Manager, Growth Hacker, PMM |
| *14 more divisions...* | | |

Each agent has a clearly defined role. For example, the **SEO Specialist** agent includes:

```yaml
---
name: "SEO Specialist"
description: "Expert in search engine optimization — technical SEO, keyword research, content strategy, and link building."
skills:
  - "Technical SEO audits (crawlability, indexation, structured data)"
  - "Keyword research and competitive analysis"
  - "On-page optimization (title tags, meta descriptions, content structure)"
  - "Link building strategy and outreach"
  - "Search Console and analytics interpretation"
---
```

You can browse the full roster from the dashboard or by looking at `cowork/agency-agents/agents/` on your filesystem.

---

## Step 3: Connect an LLM Backend

Cowork is a task orchestrator — it routes work but doesn't execute LLM calls itself. You need to connect at least one "brain" (an LLM-capable platform) to run the agents.

### Option A: Hermes Agent (Recommended for Beginners)

If you already have [Hermes Agent](https://hermes-agent.nousresearch.com) installed, it integrates natively:

```bash
hermes register-cowork
```

This registers Hermes as a Cowork worker with access to its 39+ skills and built-in tool set.

### Option B: Claude Code

Add the following to your Claude Code MCP configuration (`~/.claude.json` or project-level `claude.json`):

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

### Option C: Any MCP-Compatible Client

Any client that speaks the Model Context Protocol (MCP) — including Cursor, VS Code extensions, Gemini CLI, and custom scripts — can connect to Cowork's `/mcp` endpoint.

Once connected, agents appear as available workers. Cowork's orchestrator handles the rest.

---

## Step 4: Dispatch Your First Multi-Agent Task

Now for the fun part — running actual work through your agent team.

### Task: Multi-Agent Code Audit

Let's run a three-agent parallel audit on a GitHub repository. From the Cowork dashboard or via API:

```json
{
  "title": "Full Code Audit - agents-coworking",
  "description": "Run a comprehensive audit on the agents-coworking GitHub repo: assess code quality (Tech Lead), evaluate UX/SEO (Growth Hacker), and build an action roadmap (Product Manager).",
  "skill": "engineering",
  "tags": ["code-review", "security", "performance"],
  "to_agent": "tech-lead",
  "priority": "high"
}
```

Cowork's orchestrator processes this in three stages:

**Stage 1 — Classification:** The classifier brain reads the task description and determines the division. "Code Audit" with tags `engineering`, `code-review` → Division: Engineering.

**Stage 2 — Agent Selection:** Within Engineering, the orchestrator evaluates available agents. For a code audit task, it selects the most appropriate agent based on skill matches, expertise depth, and current load.

**Stage 3 — Execution:** The selected agent runs on your connected LLM backend, receives the full task description as context, and produces a structured output — typically saved as a markdown report in `cowork/reports/`.

You can monitor real-time progress from the dashboard:

```
━━ Task: Full Code Audit ━━
  Agent: Tech Lead (via Hermes Agent)
  Status: Working... (3 minutes elapsed)
  Progress: Analyzing code structure → Running dependency audit
```

### Chaining Tasks for Complex Workflows

For production use, you can chain tasks so one agent's output feeds another's input:

```
Research Agent → Content Writer → SEO Optimizer → Social Publisher
```

Each agent receives the previous output as context. This is how you build autonomous content pipelines, automated QA systems, and AI-driven product launch sequences.

---

## Step 5: View Results and Reports

Every completed task files a report. You can access them:

- **From the dashboard**: Navigate to Reports → list recent with titles, authors, and timestamps
- **From the filesystem**: `cowork/reports/` contains markdown files with full output
- **From the API**: `GET /api/reports` returns a JSON list

A typical code audit report includes:

```markdown
# Code Audit Report: agents-coworking
**Author**: Tech Lead (via Hermes)  
**Date**: 2026-07-26  
**Status**: Final

## Executive Summary
- Repo health: 8.2/10
- Critical issues: 2 (one security, one performance)
- High priority: 5
- Medium priority: 12

## Security Audit
### Critical: Unvalidated Input in taskHandler.js (line 142)
The `create_task` endpoint accepts user-supplied parameters without schema validation. ...
```

For a real-world example of what multi-agent audits look like, check out the [AI Dashboard Guide](/etf-ai-dashboard/) which covers automated reporting workflows.

---

## Pattern 1: Automated Code Review Pipeline

Here's a production-ready workflow pattern you can implement in 15 minutes:

**Goal**: Every time you push to GitHub, Cowork automatically reviews your code.

**Setup**:
1. Create a Cowork task template for code review
2. Use a GitHub Action to POST to Cowork's API on each push
3. Cowork dispatches to the Tech Lead and Security agents
4. Results come back as a PR comment

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

## Pattern 2: Content Production Team

For creators and marketers, a multi-agent content pipeline eliminates bottlenecks:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Research   │ ──► │  Writer     │ ──► │  SEO        │ ──► │  Publisher  │
│  Agent      │     │  Agent      │     │  Agent      │     │  Agent      │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     │                    │                    │                    │
     │ Topic analysis     │ Blog post draft    │ Meta tags,         │ Platform-specific
     │ Competitor intel   │ 2000+ words        │ schema markup,     │ posts, scheduling
     │ Keyword research   │ Tone-matched       │ internal links     │ analytics setup
```

Each agent passes its output as context to the next. The result: from topic selection to published content in one coordinated workflow.

To learn more about AI-powered content strategy and prompts, see my [AI Prompts Guide](/ai-prompts-guide/) for actionable template patterns.

---

## Pattern 3: Product Launch Orchestration

Launching a digital product requires coordinating research, content, technical setup, and analytics. A multi-agent team handles this end-to-end:

1. **Market Research Agent** — Analyzes competitors, identifies pricing gaps, generates competitive intelligence
2. **Content Strategist** — Writes landing page copy, creates promotional materials, drafts email sequences
3. **Technical Specialist** — Handles deployment, payment integration, analytics configuration
4. **PM Agent** — Integrates all outputs into a launch timeline with milestones

This is the exact pattern I use when launching new products on [Slashman Tools](/). The multi-agent approach cuts preparation time from weeks to hours.

---

## Understanding MCP: The Protocol Powering This

All of this works because of the **Model Context Protocol (MCP)** — an open standard that defines how AI agents communicate with tools, servers, and each other.

**MCP in simple terms:** Think of it as USB-C for AI agents. Just as USB-C standardized how devices connect to peripherals, MCP standardizes how AI models connect to tools, data sources, and other agents.

Here's what MCP provides in a multi-agent system:

| MCP Feature | What It Does | Why It Matters |
|-------------|--------------|----------------|
| **Tool Registry** | Agents declare what they can do | The orchestrator knows every capability |
| **Resource Access** | Agents read/write structured data | Reports, files, and context are shareable |
| **Prompt Templates** | Standardized agent instructions | Every agent starts with the right persona |
| **Transport Layer** | HTTP/SSE for remote agents | Agents can run on different machines |

Cowork implements MCP over **Streamable HTTP** — a lightweight transport that works with any HTTP client without requiring persistent WebSocket connections. This makes it trivial to integrate with CI/CD pipelines, serverless functions, and edge computing environments.

For developers who want to build custom integrations, the [Cowork repository](https://github.com/slashman413/cowork) documents the full MCP tool surface — `create_task`, `register_agent`, `get_roster`, `claim_task`, `complete_task`, `file_report`, `heartbeat`, and more.

---

## Choosing the Right Agent Architecture

Not every project needs 285 agents. Here's a decision framework:

### Single-Project Teams (1-3 agents)
- **Best for**: Small repos, personal projects, individual creators
- **Setup**: Connect one LLM backend, use 3-5 agent personas
- **Example**: Code reviewer + Writer + Researcher

### Departmental Teams (5-20 agents)
- **Best for**: Small teams, startups, agencies
- **Setup**: Multiple LLM backends, division-specific agents
- **Example**: Full engineering division + Marketing team + Data analyst

### Enterprise Teams (50+ agents)
- **Best for**: Product companies, large content operations
- **Setup**: Remote brain registration, custom agent authoring, API automation
- **Example**: All 19 divisions, multi-platform LLM routing, CI/CD integration

Cowork scales across all three tiers — you start small and add agents as your needs grow.

---

## Common Pitfalls to Avoid

After using multi-agent systems in production for months, here are the mistakes I see most often:

### 1. Too Many Agents, Too Little Context
Don't throw 20 agents at a simple task. Each agent adds latency and context overhead. Start with 2-3 agents and add only when you identify a clear need.

### 2. Ignoring Agent Persona Quality
A poorly written agent definition produces poor results. Invest time in crafting precise role descriptions, skill lists, and instruction prompts for each agent. The existing 285 agents in Cowork are carefully designed — use them as templates.

### 3. Orphaned Tasks Without Completion Tracking
Always set up completion tracking. Cowork's dashboard shows task status at a glance, but you should also configure notifications for long-running workflows.

### 4. Single-Provider Dependency
Connect at least two LLM backends. If one platform is down or rate-limited, your agent team switches to the other. Cowork handles multi-platform routing automatically.

### 5. Missing Human-in-the-Loop for Critical Decisions
For security audits, financial analysis, or legal review — always have a human review AI-generated outputs before acting on them. Agents are powerful assistants, not autonomous decision-makers for high-stakes work.

---

## Your Next Steps

You now have a running multi-agent AI system. Here's what to do next:

**Immediately (today):**
- Explore the dashboard at `http://localhost:6868/`
- Dispatch 3 different tasks to different agents
- Read through the agent roster and find specialists you didn't expect

**This week:**
- Connect a second LLM backend for redundancy
- Create one custom agent definition (copy an existing `.md` file and modify it)
- Set up a recurring task for daily market research or code review

**This month:**
- Integrate Cowork with your CI/CD pipeline
- Build a multi-step workflow (3+ agents in sequence)
- Explore the [Cowork documentation](https://github.com/slashman413/cowork) for advanced features like remote brain registration and custom executors

The complete [Multi-Agent AI Orchestration Guide](/multi-agent-coworking-platform/) covers architecture, use cases, and comparison with other frameworks — read it next for the strategic overview.

---

## FAQ: Building AI Agent Teams

**Q: Do I need to know Python or AI engineering to use Cowork?**
A: No. If you can run `git clone` and `npm install`, you can set up Cowork. The agent roster is pre-configured. You don't need to write any AI code.

**Q: Can I run Cowork on a cloud server?**
A: Yes. Cowork runs on any machine with Node.js. Deploy it on a VPS, a cloud VM, or a Raspberry Pi. The dashboard and MCP endpoint are accessible over the network.

**Q: How many agents can I run simultaneously?**
A: Cowork doesn't limit concurrency — your LLM backend and hardware do. A single machine with a modern GPU can run 5-10 agents in parallel. Enterprise setups with multiple backends scale much higher.

**Q: Is Cowork free and open-source?**
A: Yes. Cowork is MIT-licensed and available on [GitHub](https://github.com/slashman413/cowork). There's no paid tier, no hidden restrictions — everything is in the repository.

**Q: What's the difference between Cowork and CrewAI/AutoGen?**
A: Cowork focuses on breadth — 285+ pre-configured agents across 19 divisions, multi-platform LLM support, and a filesystem-first architecture. CrewAI excels at sequential agent chains; AutoGen at conversational multi-agent patterns. Cowork's strength is instant access to a curated expert roster without writing agent definitions from scratch.

---

## Conclusion: Your AI Agent Team Is Ready

Multi-agent AI orchestration isn't a future technology — it's a tool you can use today. In 20 minutes, you've gone from zero to a running multi-agent system with 285 specialists at your disposal.

The key insight is this: **one AI model is a generalist. A team of AI agents is an expert organization.** By orchestrating specialist agents through the MCP protocol, you automate complex workflows that would require a team of humans — code auditing, content production, market research, product launches — in minutes instead of days.

The Cowork MCP framework makes this practical. It's open-source, self-hosted, and ready to run on any machine with Node.js. No vendor lock-in. No cloud dependency. Just a clean, modular system that grows with your needs.

**[Clone Cowork on GitHub](https://github.com/slashman413/cowork) and build your first AI agent team today.**

---

*Reading time: 12 minutes | Published: July 26, 2026 | Last updated: July 26, 2026*

*If you found this tutorial helpful, explore more guides at [Slashman Tools](/). For ready-to-use AI prompt templates covering development, content creation, and business automation, check out the [AI Prompt Library](https://gumroad.com/l/diwoc).*

[[Back to Home](/)]
