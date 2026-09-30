---
title: Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden?
published: 2026-09-27T20:56:26Z
authors: Haomin Luo
url: http://arxiv.org/abs/2609.35897v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden?

## Abstract
The pursuit of recursive self-improvement (RSI) toward general intelligence is divided between macro-level language model scaling and the interaction-driven principles of "Era of Experience". Yet, any self-improving architecture ultimately rests upon its underlying optimization engine: if general intelligence requires learning from grounded interaction, the reinforcement learning (RL) update rule itself must be capable of cumulative adaptation. While algorithm self-discovery has produced Disco103 that surpassed PPO to achieve SOTA benchmark performance -- its internal update machinery remains an uninspected black box. We present the first causal mechanistic audit of a self-discovered RL rule, structured directly around the five pillars of the Era of Experience: extended horizon, grounded reward scales, continuing streams, within-lifetime change, and exploration depth. By surgically pinning, freezing, and transplanting recurrent states while holding meta-parameters fixed, we test when learning history acts as an asset or a burden. Three findings organize the audit: (1) Recurrent history actively expands usable reward scales, sustaining a six-decade window versus three under zero-pinning. (2) Decoupling historical content from its maintenance reveals that the penalty of mismatched history stems from perpetual clamping; allowing imported state to evolve naturally attenuates this burden. (3) Under environmental change, controlling replay retention reverses the apparent adaptation advantage over DQN, demonstrating that external data turnover can confound internal plasticity. Validated through capability thresholds and ported to a second rule (OPEN), this work grounds macro-RSI ambitions in micro-level learning dynamics, establishing a foundational audit standard for next-generation, self-evolving RL algorithms.

## Metadata
- **Published**: 2026-09-27T20:56:26Z
- **Authors**: Haomin Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35897v1)