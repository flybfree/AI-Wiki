---
title: One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning
url: http://arxiv.org/abs/2608.30952v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-22-19Z_OnePolicyIsEnough_Single_AgentReinforcementLearnin.md
generated_at: 2026-08-31 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes CheMatAgent that uses a single policy to generate tool calls directly without separate search or evaluation models. Experiments on ChemToolBench show significant gains in Tool F1 and Return F1 over the best tree‑search baseline, with Qwen-2.5-7B improving by 9.6% and Llama-3.1-8B by 3.9%.

## Key Takeaways
- The model replaces hierarchical MCTS with a unified left‑to‑right generation that interleaves reasoning, tool calls, and returns.
- Training relies solely on outcome‑level reinforcement learning using the gold call chain as reward, eliminating learned critics or judges.
- Results show up to 9.6% absolute improvement in Return F1 for Qwen-2.5-7B while maintaining one model invocation per question.

## Context
This work addresses a core challenge in AI assistants that require external tools for accurate chemistry queries, highlighting the need for efficient tool‑use mechanisms beyond simple lookup. The shift from multi‑stage search to single‑agent generation simplifies deployment and reduces latency.

## Implications
By eliminating complex tree search components, CheMatAgent offers a more scalable solution for large language models, lowering computational cost per query and enabling real‑time responses. Practitioners can adopt this approach to improve tool utilization without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30952v1)
