---
title: "Hermes Agent Guide"
tags: ["agent-platform", "tooling", "workflow"]
created: 2026-07-06
updated: 2026-07-06
source: https://www.youtube.com/watch?v=_LYXbI6JY5M
---

# Hermes Agent Guide

**Source**: [Original Video](https://www.youtube.com/watch?v=_LYXbI6JY5M)

## Overview

Hermes Agent is a personal AI assistant that runs across CLI, TUI, messaging gateways, and desktop app. It learns across sessions via memory and skills, delegates to subagents, runs scheduled jobs, and drives real terminals and browsers. The July 2026 update introduced seven major features that significantly enhance its capabilities.

## Semantic links
- [[concepts/search-retrieval/search-retrieval-hub.md|Search and Retrieval Hub]] — 1 title term overlap; 332 backlinks; 2 summary/topic terms overlap
- [[concepts/embodied-ai/embodied-ai-hub.md|Embodied AI and Robotics Hub]] — 1 title term overlap; 40 backlinks; 2 summary/topic terms overlap
- [[concepts/ai-agents/ai-agents-lesson-03-planning-memory-and-state.md|AI Agents Lesson 4 - Planning, Memory, and State]] — 2 title terms overlap; 2 backlinks; 3 summary/topic terms overlap

## Key Features

### 1. Mixture of Agents (MA)

**What it does**: Sends your prompt to multiple reference models simultaneously, then synthesizes their responses into one answer.

- **Default configuration**: ChatGPT + DeepSeek v4 via OpenRouter
- **How to use**: Type `/ma` followed by your prompt, or select "MOA default" from the dropdown
- **Best for**: Complex questions that can go many directions; when you want diverse perspectives synthesized

**Example workflow**:
```
/ma What are five SaaS ideas I can build today based on my interests?
```

The aggregator model (your current primary model) sends the prompt to reference models, collects their responses, and produces a unified answer.

### 2. `/learn` — Auto-Create Skills & Memories

**What it does**: Automatically converts any URL, prompt, or completed task into a reusable skill and associated memories.

**Use cases**:
- Save helpful tweets, articles, or tutorials you find online
- Capture workflows your agent executes successfully
- Turn repeated processes into permanent skills without manual creation

**How to use**:
```
/learn [URL or text]
```

**Example**: Paste a tweet URL about coding loops → Hermes creates a skill from it instantly.

### 3. `/journey` — Visual Learning Map

**What it does**: Displays all your agent's skills and memories in an interconnected chart, showing how concepts relate to each other.

**Purpose**:
- See everything your agent has learned about you across all conversations
- Understand connections between different skills and memories
- Verify that the agent is actually learning and improving over time

### 4. Cheaper Self-Improvement

**Change**: Background learning tasks (creating skills/memories) now delegate to cheaper models instead of expensive ones like Opus or ChatGPT.

**Impact**: Significant cost savings for regular users, especially those using premium models as their primary agent.

### 5. Vibe Coding Improvements

**What's new**: Full Git controls integrated into Hermes desktop app:
- View code diffs
- Make commits directly from the interface
- Open pull requests without leaving Hermes

**Result**: A viable alternative to Claude Code for building applications and games. The desktop app provides a complete development environment with version control built in.

### 6. Fable 5 Integration & Strategy

Fable 5 is now available as a model option in Hermes Agent. **Recommended usage strategy**:

- **Create a dedicated profile** specifically for Fable 5 (e.g., "Oracle" profile)
- **Do NOT use as daily driver** — it's too expensive for routine tasks
- **Use for**: 
  - Complex building tasks requiring perfect execution
  - Multi-step actions across different devices
  - When you need a perfectly built front-end or system

**Decision framework**:
- **Mixture of Agents** → complex questions needing multiple perspectives
- **Fable 5** → complex tasks requiring precise implementation

### 7. Bonus: Community & Learning Resources

Full boot camps on Hermes Agent are available through the Vibe Coding Academy, which hosts over 1,000 AI builders. This is positioned as a primary community for learning advanced techniques and building alongside others.

## Practical Recommendations

### For Daily Use
- Keep your primary model (e.g., Opus) for general tasks
- Use Mixture of Agents for complex questions requiring diverse viewpoints
- Leverage `/arn` to continuously improve your agent's capabilities

### For Building Projects
- Switch to Fable 5 profile when you need high-quality implementation
- Take advantage of built-in Git controls in the desktop app
- Consider Hermes as a complete vibe coding environment

### For Learning & Growth
- Use `/journey` regularly to see what your agent has learned
- Review connections between skills and memories
- Let the agent self-improve automatically with cheaper models

## Setup Notes

To use Mixture of Agents, ensure OpenRouter API keys are configured. Hermes can help set this up if needed via:
```
Hey, set up OpenRouter for me so I can use Mixture of Agents.
```

For Fable 5, create a new profile with a prompt like:
```
Please make a new Hermes profile called Oracle that uses Fable 5 model from Claude. Let me know when that's set up so I can use it in Telegram.
```

## Getting Started: Setup & Configuration

### Installation
- **Desktop app**: Download for macOS, drag to Applications folder (also available via CLI)
- **System prerequisites**: Auto-installs required dependencies

### Model Options

#### Local Models (Privacy-focused)
1. Install Ollama and pull a model (e.g., `ollama pull gemma4:latest`)
2. Connect via Settings → Custom Endpoint → Ollama URL (`http://localhost:11434/v1`)
3. **Important**: Hermes requires 64k context window for full tool access
   - If your model has smaller context (e.g., 32k), create a variant with increased context:
     ```bash
     hermes config set model.provider.base_url http://localhost:11434/v1
     hermes config set model.default_model gemma4-64k
     ```
   - Or ask Hermes to create the variant automatically

#### Cloud Models (Power-focused)
1. Add provider in Settings → Providers (OpenAI, Anthropic, etc.)
2. Link API keys through the provided setup flow
3. Switch between local and cloud models via profile selector

### Profiles: Isolated Environments
Each profile has completely separate configuration, skills, memory, and session history:
- **Use case**: One profile for local/private work, another for cloud/powerful tasks
- **Setup**: Ask Hermes to create profiles automatically, or configure manually
- **Switching**: Click profile in bottom bar to change context instantly

### Skills & Tools
- **71 built-in skills**: Reusable workflows that ensure consistency and quality
- **Explore**: Review existing skills (e.g., Obsidian integration) before building new ones
- **Tool sets**: Enable/disable functions like code execution, computer control, browsing
- **Keep memory ON**: Enables persistent learning across sessions

### Memory System
Hermes maintains two persistent files outside session context:
- `user.md`: Your preferences and personal details
- `memory.md`: Solutions and patterns learned over time

**Example**: Telling Hermes "I'm technical and prefer straight-to-the-point explanations" automatically updates `user.md`.

### Advanced Configuration
- **Execution backend**: Run code locally, in Docker containers, via VPS, or SSH across multiple computers
- **Sandboxing**: Use Docker to protect your system from experimental code
- **Working directory**: Configure per-profile (e.g., separate folders for local vs cloud)
- **Memory budget**: Control size of injected memory; outdated info is pruned automatically

### Messaging Gateways
Connect Hermes to any messaging platform:
- **Supported**: Telegram, Discord, Slack, Google Chat, WhatsApp, Signal, email, SMS
- **Setup**: Each gateway has dedicated documentation (e.g., create Telegram bot via BotFather)
- **Conversations**: All messages stored locally on backend, accessible from any connected device

### Remote Gateways
Keep one backend with shared memory, access from multiple devices:
- Run Hermes desktop on main machine as backend
- Connect laptop/phone as remote gateway
- Single "brain" that matures across all your devices

## Practical Example: Daily AI Briefing Bot

This workflow demonstrates the self-improving automation loop:

1. **Define goal** in chat: "Create a daily AI briefing delivered to Telegram"
2. **Agent creates skill** (`AI Daily Intel`) and implementation plan
3. **Dry run** in chat to test output before scheduling
4. **Schedule cron job** to run daily at specified time
5. **Give feedback** on received reports → agent updates memory/skill
6. **Next report improves** based on your preferences

**Key insight**: The automation becomes more personalized over time through continuous feedback, without manual reconfiguration.

## Important Notes

- **Before automating**: Always test workflows in chat first to verify output quality
- **Docs integration**: Agent can read Hermes documentation to understand its own capabilities and limitations
- **Self-evolution**: Every interaction teaches the agent; skills and memories compound over time
- **Not static**: Unlike tools that remain at day-one capability, Hermes gets smarter with use

## Conclusion

The July 2026 update transforms Hermes Agent into a more powerful, cost-efficient, and versatile tool. The combination of Mixture of Agents for complex reasoning, `/learn` for automatic skill creation, `/journey` for visibility into learning, cheaper self-improvement, enhanced vibe coding with Git integration, and Fable 5 for precise implementation makes it a comprehensive AI assistant platform.

---

*This article will be updated as new features are released.*