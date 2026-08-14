---
title: AQuA: Recursively Self-Improving Quantitative Trading Research Agents
url: http://arxiv.org/abs/2608.12841v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_05-25-42Z_AQuA_RecursivelySelf_ImprovingQuantitativeTradingR.md
generated_at: 2026-08-13 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
AQuA investigates recursive self‑improvement within quantitative investment research by creating two independent language‑model driven systems that each close their own loop using validated evidence. The factor system discovers and combines factors to achieve an information coefficient of about 0.190 on a crypto universe, while the model system produces a per‑stock IC of +0.0843 and a strategy with a held‑out Sharpe up to 2.5 across 2021–2025.

## Key Takeaways
- The factor discovery pipeline, managed through a multi‑agent process, reaches an information coefficient of roughly 0.190 on the crypto universe, indicating strong predictive power from combined factors.  
- The model system’s config‑driven loop converts this signal into a long/short strategy that consistently outperforms with a Sharpe ratio up to +2.5 and remains positive every year from 2021 to 2025.  
- Both systems operate within sealed sandboxes that fix data splits, feature definitions, and evaluators, ensuring reproducibility while allowing only constrained factor expressions or configuration diffs.

## Context
This work aligns with the broader AI trend toward autonomous research loops where models generate hypotheses, test them, and refine their own strategies. By bounding self‑improvement to a single research loop and using sandboxed environments, AQuA demonstrates how language models can be harnessed for systematic investment without unbounded recursion or data leakage.

## Implications
The results suggest that automated, self‑optimizing trading agents could reduce reliance on human judgment and accelerate the development of robust quantitative strategies. Practitioners may adopt such bounded recursive frameworks to improve model robustness while maintaining regulatory compliance through fixed evaluation criteria.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12841v1)
