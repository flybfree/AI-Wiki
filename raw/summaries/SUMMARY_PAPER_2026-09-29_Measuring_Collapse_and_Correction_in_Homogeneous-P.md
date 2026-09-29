---
title: Measuring Collapse and Correction in Homogeneous-Panel LLM Debate
url: http://arxiv.org/abs/2609.35279v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_14-31-19Z_MeasuringCollapseandCorrectioninHomogeneous_PanelL.md
generated_at: 2026-09-29 02:03
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces an auditable protocol for evaluating homogeneous-panel LLM debates on multiple-choice questions by distinguishing between answer collapse and correction, rather than relying solely on final accuracy improvements. Analysis of 6,925 MMLU-Pro debates reveals that interventions often involve a tradeoff where preventing collapses may inadvertently eliminate beneficial corrections, suggesting that standard evaluation metrics can misguide policy decisions regarding debate mechanisms.

## Key Takeaways
- The authors propose a transition ledger framework that categorizes debate dynamics into collapse, correction, onset, and signed intervention utility, enabling auditable tracking of how model interactions alter answer trajectories rather than just measuring final correctness.
- Replay experiments on MMLU-Pro data demonstrate a critical tradeoff: implementing a leave-one-model

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35279v1)
