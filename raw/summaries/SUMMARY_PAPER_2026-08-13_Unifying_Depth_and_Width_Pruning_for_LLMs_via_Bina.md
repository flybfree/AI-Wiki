---
title: Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization
url: http://arxiv.org/abs/2608.12953v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-32-18Z_UnifyingDepthandWidthPruningforLLMsviaBinaryKnapsa.md
generated_at: 2026-08-13 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SNIPER, a two‑stage structured pruning method that replaces greedy heuristics with binary knapsack optimization to allocate model parameters while respecting importance estimates and strict compression budgets. Experiments on four architectures across 18 tasks show SNIPER consistently retains higher performance than six state‑of‑the‑art pruners and achieves near‑exact adherence to target ratios.

## Key Takeaways
- SNIPER solves a knapsack problem at coarse granularity, producing conditionally optimal parameter allocations that align with importance estimates.  
- The Compression Ratio Adherence Factor (CRAFT) measures budget fidelity, revealing existing pruners deviate up to 33 % from targets while SNIPER reaches CRAFT = 0.98.  
- Across all configurations the mean rank is 1.25, indicating robust cross‑architectural generalizability and reliable performance.

## Context
Structured pruning remains a key technique for reducing model size without sacrificing accuracy, yet many approaches rely on myopic greedy strategies that ignore global budget constraints. This work advances the field by integrating optimization theory with practical LLM compression, offering a principled alternative to heuristic methods.

## Implications
For practitioners, SNIPER provides a reliable way to meet exact compression targets while preserving model utility, which can lower inference costs and improve deployment efficiency. The method’s cross‑architectural performance suggests it could become a standard tool in the pipeline for scalable LLM optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12953v1)
