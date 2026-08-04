---
title: Fairness Auditing: Lower Bounds on Company Manipulation
url: http://arxiv.org/abs/2608.00568v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_10-11-20Z_FairnessAuditing_LowerBoundsonCompanyManipulation.md
generated_at: 2026-08-03 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of fairness auditing in high‑stakes AI systems by establishing lower bounds on how much demographic parity deviation can remain after an audit, given limited resources and a tolerant auditor. It shows that while more data reduces manipulation, it never fully eliminates it, highlighting inherent trade‑offs between budget constraints and certification certainty.

## Key Takeaways
- The worst‑case post‑audit demographic parity deviation depends on the size of the audit set, the imbalance among groups, and the allowed fairness tolerance α.  
- Even with a large budget, some manipulation can persist because the auditor’s estimate is only an approximation rather than exact measurement.  
- Theoretical lower bounds prove that no finite‑budget auditing strategy can guarantee zero deviation under arbitrary company behavior.

## Context
Fairness auditing has become essential as organizations deploy automated decision systems in hiring and lending. Recent impossibility theorems show that expressive models can circumvent any audit, yet practitioners still need practical methods to assess fairness within budget limits. This work bridges the gap between theoretical limits and empirical feasibility by quantifying what can be achieved with real‑world data.

## Implications
For AI developers, these bounds suggest realistic expectations: increasing audit size improves but never perfectifies fairness certification. Companies must balance resource allocation with acceptable risk, while regulators should consider the inherent impossibility of zero deviation in finite audits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00568v1)
