---
title: ReCo: Reweighting GRPO Against Distributional Concentration
url: http://arxiv.org/abs/2607.26862v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_12-45-55Z_ReCo_ReweightingGRPOAgainstDistributionalConcentra.md
generated_at: 2026-07-29 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why Group Relative Policy Optimization (GRPO) can degrade large language model reasoning when applied to mathematical tasks, showing that the method concentrates on responses already likely produced by the base model. It identifies two mechanisms: response-level dominance due to repeated high-probability outputs and token-level reinforcement via importance ratios. The authors propose ReCo, a reweighting technique that normalizes response contributions and replaces the importance ratio with a variance‑based metric, improving Pass@k for large k.

## Key Takeaways
- Response contributions are normalized by their expected occurrence within the rollout group to prevent overemphasis on frequent responses.
- The token-level importance ratio is replaced with a variance‑based ratio that scales updates more when alternative tokens remain plausible.
- ReCo improves Pass@k on mathematical reasoning benchmarks for large k and matches GRPO performance for small k.

## Context
Recent advances in reinforcement learning for language models have highlighted trade‑offs between efficiency and reasoning capability. While methods like GRPO reduce computational cost, they may inadvertently narrow the search space of possible answer paths, limiting performance on complex tasks such as math solving.

## Implications
For practitioners developing RL‑based policy fine‑tuning pipelines, ReCo offers a practical way to preserve diverse reasoning strategies without sacrificing speed. This could lead to more robust AI assistants that handle varied problem types and maintain high accuracy across large prompt sets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26862v1)
