---
title: Toward SLM-based agentic task-tool intent matching
published: 2026-10-02T12:31:01Z
authors: Chiara Troiani, Arash Salarian, Majed El Helou, Benjamin Ryder, Jean Diaconu, Hervé Muyal, Marcelo Yannuzzi
url: http://arxiv.org/abs/2610.03213v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward SLM-based agentic task-tool intent matching

## Abstract
Tool-equipped AI agents use tool calls to access data and act on external systems. Horizontal growth of agentic systems increases the number of these interactions, and further motivates the need for automated, per-call oversight that can operate at low latency and/or on-prem. Conventional authorization schemes can determine whether an agent is allowed to invoke a tool, but cannot assess the agent's underlying cognition, specifically, whether the tool selection represents a logical, relevant step toward satisfying the intent of the task or not. Consequently, an allowed call may still deviate from the task's intent: a rogue agent might deviate the calls or nudge other agents to make a combination of calls that would not align with the intent of the task. Therefore, every call needs to be verified. In this study we investigate the applicability of Small Language Models (SLMs) to this purpose: an SLM functions as a task-tool relevance classifier that evaluates every selected tool independently against the assigned task and returns a relevance signal for downstream enforcement. Equipped with a novel dataset with multi-tool tasks whose required tools span distinct Model Context Protocol (MCP) servers, we used prompt-optimization, supervised fine-tuning, and reinforcement learning through GRPO to optimize and specialize SLMs.

## Metadata
- **Published**: 2026-10-02T12:31:01Z
- **Authors**: Chiara Troiani, Arash Salarian, Majed El Helou, Benjamin Ryder, Jean Diaconu, Hervé Muyal, Marcelo Yannuzzi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03213v1)