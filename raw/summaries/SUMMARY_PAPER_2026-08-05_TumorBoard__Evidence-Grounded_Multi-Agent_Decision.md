---
title: TumorBoard: Evidence-Grounded Multi-Agent Decision Support for Longitudinal Neuro-Oncology
url: http://arxiv.org/abs/2608.03190v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-32-25Z_TumorBoard_Evidence_GroundedMulti_AgentDecisionSup.md
generated_at: 2026-08-05 01:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TumorBoard, a multi‑agent decision‑support system for neuro‑oncology that integrates serial MRI, pathology, molecular markers, treatment history, performance status and evolving guidelines into a shared longitudinal case state. By using an auditable claim‑evidence ledger, adversarial critic and safety governor, the system produces atomic claims with provenance and delivers recommendations only when evidence is sufficient and temporally valid.

## Key Takeaways
- TumorBoard achieved an action F1 of 0.772 on a hidden benchmark of 360 cases, exceeding typed‑council baselines by 3.1 percentage points (95% CI: 1.6 to 4.7).  
- The evidence entailment score is 0.914, meaning that 92.7 % of recommendations are fully supported by the evidence in the ledger.  
- When evidence is deleted, the system defers 84.2 % of unsafe cases and limits harmful releases to 5.8 %; the safety governor reduces harmful release by 7.8 points at a false‑deferral cost of 4.3 points.

## Context
This work advances AI for longitudinal medical decision‑making by combining specialized agents with an auditable claim‑evidence ledger, illustrating how structured coordination can improve diagnostic accuracy and workflow efficiency in complex clinical settings such as neuro‑oncology.

## Implications
The approach offers a scalable framework that balances evidence sufficiency with timely recommendations while minimizing risk, potentially enhancing patient outcomes and supporting regulatory compliance across the neuro‑oncology field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03190v1)
