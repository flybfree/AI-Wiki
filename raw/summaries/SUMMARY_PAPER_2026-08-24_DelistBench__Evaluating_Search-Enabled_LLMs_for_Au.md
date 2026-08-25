---
title: DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion
url: http://arxiv.org/abs/2608.22770v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_03-46-20Z_DelistBench_EvaluatingSearch_EnabledLLMsforAuditab.md
generated_at: 2026-08-24 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Search-to-Record, a task where search-enabled LLMs reconstruct corporate event records from public sources within a security universe and historical cutoff. It presents DelistBench, a benchmark of 1,200 delisting announcements, and evaluates five models in closed‑book vs web‑enabled settings.

## Key Takeaways
- Web access improves announcement‑date accuracy by up to 48 percentage points compared with closed‑book conditions.
- The best system reaches 81.5% joint accuracy within seven days, while low‑cost systems achieve 75.9–78.3% at a fraction of the API cost.
- Risk‑based triage still routes about 27.3% of the test set to manual review.

## Context
This work addresses a critical gap in AI‑driven financial data verification, where autonomous LLMs must balance accuracy and cost for compliance‑sensitive tasks. The results demonstrate that retrieval capabilities can be leveraged to close timing gaps without sacrificing performance at scale.

## Implications
For banks and regulators, the findings suggest that search‑enabled models can provide near‑optimal audit trails while keeping operational expenses low. Practitioners should calibrate triage thresholds to local event frequencies and preserve recall of positive events for reliable risk management.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22770v1)
