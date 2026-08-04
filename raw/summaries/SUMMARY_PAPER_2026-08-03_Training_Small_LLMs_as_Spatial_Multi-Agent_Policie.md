---
title: Training Small LLMs as Spatial Multi-Agent Policies
url: http://arxiv.org/abs/2608.01425v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_18-14-40Z_TrainingSmallLLMsasSpatialMulti_AgentPolicies.md
generated_at: 2026-08-03 23:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of training small language models to act as spatial multi‑agent policies in cooperative games by treating each agent’s behavior as a selection among symbolic options. The authors demonstrate that frozen LLMs can achieve competent play across three games and four lightweight backbones when equipped with per‑agent LoRA adapters trained via PA‑MAGRPO, while reward signals remain misleading for cooperation.

## Key Takeaways
- Symbolic options are generated automatically from game code and filtered by random‑policy burn‑in rollouts to exclude false failures.  
- Each LLM operates as a policy over these options, with a private LoRA adapter fine‑tuned using multi‑agent GRPO to lift zero reward into functional behavior.  
- Behavioral audits show that rising rewards often indicate solo task execution rather than true cooperation.

## Context
The work builds on the growing interest in multi‑agent reinforcement learning and the need for interpretable, reward‑agnostic evaluation of cooperative AI systems. By integrating symbolic reasoning with data‑driven policy adaptation, it offers a bridge between human‑crafted game design and scalable model training.

## Implications
Practitioners can rely less on raw reward curves when assessing multi‑agent collaboration and instead evaluate behavior through option execution logs. This approach could improve system robustness in real‑world distributed tasks where cooperation is context‑dependent rather than uniformly rewarded.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01425v1)
