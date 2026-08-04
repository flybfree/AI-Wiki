---
title: Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale
published: 2026-07-30T20:51:51Z
authors: Banruo Liu, Haoran Qiu, Íñigo Goiri, Rodrigo Fonseca, Ricardo Bianchini, Esha Choukse
url: http://arxiv.org/abs/2608.00101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale

## Abstract
AI coding agents like GitHub Copilot, Claude Code, and Codex interleave multi-step LLM inference with tool execution, creating a workload different from chatbots. We present the first production-scale characterization of this workload using sampled GitHub Copilot traces from June 2026, comprising 3.2M users, 13M sessions, 761M LLM calls, and 95T tokens.   Our analysis reveals distinctive workload properties with important systems implications. For example, agentic coding sessions consist of sparse user-initiated turns, each unfolding into an autonomous agent loop of LLM calls almost always coupled with tool execution. This structure yields KV cache hit rates averaging 90% within a turn, but falling to 55\% across turn boundaries and drastically invalidated after events like model switches or context compaction. Diverse workflows and user behaviors are observed with variable and long-tailed token consumption, time span, and tool calls. We highlight the difference between quick agentic turnaround times and the minutes-long user idle periods at turn boundaries, and design a lightweight idle-time predictor that captures 86-90\% of total idle time, enabling proactive decisions for efficient resource orchestration. These findings challenge assumptions underlying current LLM-serving systems and provide an empirical foundation for agent-native infrastructure.

## Metadata
- **Published**: 2026-07-30T20:51:51Z
- **Authors**: Banruo Liu, Haoran Qiu, Íñigo Goiri, Rodrigo Fonseca, Ricardo Bianchini, Esha Choukse
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00101v1)