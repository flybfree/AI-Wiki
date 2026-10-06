---
title: Can LLM Agents Automate Reinforcement Learning for Text-to-Speech?
published: 2026-10-03T12:44:09Z
authors: Xuanjun Chen, Zixiong Su, Hao Shi, Chang Zeng, Kai Li, Jyh-Shing Roger Jang, Hung-yi Lee
url: http://arxiv.org/abs/2610.04488v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLM Agents Automate Reinforcement Learning for Text-to-Speech?

## Abstract
Although reinforcement learning (RL) post-training repairs the localized segmental errors of zero-shot text-to-speech (TTS), arriving at a working recipe still relies on tedious manual tuning, and whether LLM agents can take over this research pipeline is unclear. We investigate this question with AgenticTTS-Forge, a collaborative workflow that structures human guidance and agentic execution around a shared workspace, applied to CosyVoice2-0.5B. To measure what the agent automates, we audit its trajectory stage by stage against the published recipe. To measure what it exploits, we score its policies with held-out observers hidden from the agent. Our results show that the agent recovers an underspecified recipe, improves it, and, when gains stall, surveys the literature unprompted and pivots from the LM carrier to the flow carrier, halving Bad cases. However, its autonomy exposes three traps across the data, proxy, and algorithm axes: the held-out set leaks through a channel the contract never reads, a self-shaped reward inflates the proxy where it is scored, and separately tuned policies do not compose additively. These findings show that the binding constraint is measurement rather than reasoning, and can inform the design of harnesses whose contracts read every channel the agent does.

## Metadata
- **Published**: 2026-10-03T12:44:09Z
- **Authors**: Xuanjun Chen, Zixiong Su, Hao Shi, Chang Zeng, Kai Li, Jyh-Shing Roger Jang, Hung-yi Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04488v1)