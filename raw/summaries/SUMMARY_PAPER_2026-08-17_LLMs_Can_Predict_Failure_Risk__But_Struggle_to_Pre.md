---
title: LLMs Can Predict Failure Risk, But Struggle to Predict Which Collaboration Protocol Pays Off: Cost-Aware Protocol Routing Across Reasoning Tasks
url: http://arxiv.org/abs/2608.14927v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_22-35-37Z_LLMsCanPredictFailureRisk_ButStruggletoPredictWhic.md
generated_at: 2026-08-17 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how multi‑agent large language models decide when to collaborate and what protocol yields the best trade‑off between accuracy and cost. Across four collaboration protocols, only a few router configurations achieve reliable failure prediction, while others over‑escalate or under‑escalate. A probe model can reliably flag failures with high AUROC but cannot identify PER or Broadcast value, yielding low AUPRC scores of 0.1674 and 0.1041.

## Key Takeaways
- Conservative policies often under‑escalate, missing solvable problems.
- Higher‑solve frozen routers can over‑escalate, incurring unnecessary cost.
- Post‑answer probes rank failures well (AUROC 0.8847) but cannot identify PER or Broadcast value, yielding low AUPRC scores of 0.1674 and 0.1041.

## Context
This work addresses a core challenge in deploying scalable LLM systems: balancing computational effort with solution quality. Understanding protocol‑specific benefits helps researchers design cost‑aware routing strategies.

## Implications
Practitioners can use confidence gates for initial escalation decisions. The need for protocol‑aware routing remains an open research problem. Future work should combine confidence thresholds with protocol‑specific cost models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14927v1)
