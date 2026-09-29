---
title: PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning
url: http://arxiv.org/abs/2609.35158v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_13-35-47Z_PEARL_AdaptivePrefill_DecodeExecutionwithElasticit.md
generated_at: 2026-09-28 23:07
model: qwen3.6-35b-a3b
---

## Summary
PEARL is an asynchronous agentic reinforcement learning system designed to optimize multi-turn rollout costs by dynamically coordinating GPU elasticity, adaptive prefill-decode execution modes, and the temporary reuse of idle training GPUs. The system leverages runtime profiles to predict batch completion times and selects optimal configurations under budget constraints while minimizing transition overheads through cost-aware switching policies. Evaluations demonstrate significant throughput improvements, achieving 2.17–2.79x gains over fixed-resource baselines and outperforming RLBoost+ by up to 36.3% on various models.

## Key Takeaways
- Resource efficiency in agentic RL depends critically on the dynamic selection of prefill-decode configurations, as optimal modes (colocation vs. disaggregation

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35158v1)
