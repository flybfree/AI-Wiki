---
title: When Consent Outlives Context: Residual Authority Replay in Long-Lived Agents
published: 2026-09-27T20:43:53Z
authors: Zhihao Zhang, Chao Wang, Rujia Li, Qingze Wang, Xiaoyan Sun, Jun Dai
url: http://arxiv.org/abs/2609.33910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Consent Outlives Context: Residual Authority Replay in Long-Lived Agents

## Abstract
LLM agents increasingly rely on user approval to authorize security-sensitive actions at runtime. Such approvals are granted within a specific task and execution context. In long-lived agents, authorization decisions may need to persist across tasks or sessions. We find that this continuity can outlive the context that originally justified the approval, creating residual authority reusable without renewed consent. We expose this failure mode through a longitudinal attack that starts from a target security-sensitive action, identifies the authority required to execute it, induces benign interactions that legitimately obtain that authority, and later replays the residual authority during adversarial execution. Across controlled and live settings, we demonstrate that residual-authority replay arises in practice and substantially increases the success of prompt-injection and context-rebinding attacks. We evaluate 508 AgentDojo attack cases across six LLM families using production-derived authorization semantics. With residual authority, attack success rate (ASR) increases by up to 35.1 percentage points compared with a fresh authorization state. In live context-rebinding attacks on 55 Terminal-Bench cases across three real-world production coding agents, residual-authority replay increases ASR by 24.9 percentage points on average. These findings expose a fundamental mismatch between persistent authorization and the contextual nature of user consent in long-lived LLM agents.

## Metadata
- **Published**: 2026-09-27T20:43:53Z
- **Authors**: Zhihao Zhang, Chao Wang, Rujia Li, Qingze Wang, Xiaoyan Sun, Jun Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33910v1)