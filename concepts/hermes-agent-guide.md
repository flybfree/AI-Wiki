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

## Conclusion

The July 2026 update transforms Hermes Agent into a more powerful, cost-efficient, and versatile tool. The combination of Mixture of Agents for complex reasoning, `/arn` for automatic skill creation, `/journey` for visibility into learning, cheaper self-improvement, enhanced vibe coding with Git integration, and Fable 5 for precise implementation makes it a comprehensive AI assistant platform.

---

*This article will be updated as new features are released.*