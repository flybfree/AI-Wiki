---
title: ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning
url: http://arxiv.org/abs/2607.25369v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_07-25-04Z_ODYSSE_Episode_wisePolicyOptimizationforPersonaliz.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ODYSSE, a Reinforced Fine‑Tuning framework that tackles personalized agentic reasoning by extending Group Relative Policy Optimization to episode‑wise optimization. The novel ESPO method uses an episode‑level reward and advantage estimation to guide long‑horizon actions across multiple interaction steps. Experiments on realistic GUI reasoning tasks show that ODYSSE outperforms both specialist and general‑purpose language models.

## Key Takeaways
- ESPO introduces an episode‑level reward mechanism together with episodic advantage estimation, allowing upstream evidence to influence downstream personalized decisions.
- The framework groups actions from the same episode into unified training batches via an episodic batch sampler, promoting coherent optimization across long action horizons.
- ODYSSE consistently outperforms specialist and general‑purpose LVLMs on realistic long‑horizon personalized GUI reasoning tasks.

## Context
Personalized agentic systems must navigate ambiguous user requests by exploring large solution spaces while adapting to individual preferences. Traditional RL approaches often fail to capture cross‑step dependencies in such scenarios, limiting the quality of service delivery.

## Implications
This work advances the state of the art for personalization in AI agents, offering a scalable method that can be integrated into real‑world service platforms. Practitioners can leverage ODYSSE’s episode‑wise optimization to deliver more accurate and context‑aware responses without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25369v1)
