---
title: Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory
url: http://arxiv.org/abs/2607.28437v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-13-02Z_Oracle_BudgetedMolecularOptimizationwithShort_Term.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a plug‑in module called short‑term graph memory that learns from previously evaluated molecules to guide the selection of oracle queries within a fixed budget. Applied to four fragment‑based generators on a molecular optimization benchmark, it improves the mean top‑10 score without using extra oracle calls and never underperforms the baseline.

## Key Takeaways
- The module maintains an online graph neural surrogate that pre‑screens candidate molecules each round, allowing the fixed oracle budget to be spent only on high‑predicted utility molecules. - It improves the mean top‑10 score at no extra oracle cost and never falls behind the base model across all four generators tested within a thousand calls. - The benefit persists even when the oracle budget is limited, indicating effective exploitation of prior feedback.

## Context
Molecular optimization problems often face severe constraints on evaluation resources, forcing algorithms to balance exploration and exploitation. Recent work has explored surrogate models that approximate expensive evaluations, but few integrate such surrogates directly into generator architectures without altering their native update rules.

## Implications
This approach offers a practical way for practitioners to allocate limited computational resources more efficiently in drug‑discovery pipelines where each oracle query is costly. By preserving the original generator design, it can be adopted across diverse optimization frameworks with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28437v1)
