---
title: One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence
url: http://arxiv.org/abs/2607.28317v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-52-36Z_OneHuman__N_Agents_Audit_BudgetAllocationforLLMAge.md
generated_at: 2026-07-30 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how a single human auditor can select which of many language model agents to inspect when only a few audits are available, under conditions where the models' confidence scores are miscalibrated and their errors tend to be correlated. It finds that there exists a threshold beyond which confidence‑based selection performs worse than random sampling, and this threshold grows as the audit budget shrinks.

## Key Takeaways
- The miscalibration threshold δ* increases when the number of audits per round B is reduced, making confidence ranking less reliable.
- Correlated errors across agents mean that shared difficulty dominates lineage rather than low cross‑family correlation.
- Open‑weight models produce near‑constant confidence scores that are operationally useless, while a proprietary model remains informative and falls below δ*.

## Context
The study addresses a recurring challenge in AI governance: ensuring oversight of large language model deployments when resources are limited. By modeling audits as noisy inspections with a Gaussian copula, the authors provide a theoretical framework for budgeted inspection problems.

## Implications
For practitioners, the findings warn against relying on confidence signals to prioritize audits without accounting for miscalibration and correlation. The paper suggests developing alternative selection criteria that do not depend on these flawed metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28317v1)
