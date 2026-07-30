---
title: Lottery Tickets Are Not Deployment Tickets
url: http://arxiv.org/abs/2607.27031v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_15-25-19Z_LotteryTicketsAreNotDeploymentTickets.md
generated_at: 2026-07-29 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether sparse models created with lottery tickets can replace dense reference models in real deployment without altering downstream decision logic, focusing on behavior beyond raw accuracy. It audits calibration, out‑of‑distribution response, class reliability, representations and policy decisions across a protocol panel, measuring deviations via a behavioral‑compatibility distance. Experiments show that even when sparse candidates match dense accuracy, they differ behaviorally, causing churn in accept‑review decisions.

## Key Takeaways
- Sparse lottery tickets can achieve the same pointwise top‑1 accuracy as dense models but produce measurable changes in calibration and OOD handling.
- In settings where downstream policies use fixed thresholds, a 7–10 % shift in accept‑review outcomes occurs, indicating churn that drop‑in replacement aims to avoid.
- The paper argues that clean‑accuracy certification is insufficient; compatibility with the incumbent decision logic must be evaluated separately.

## Context
Current AI deployment pipelines often assume that improving model efficiency will not affect real‑world behavior, yet sparse models can alter calibration and OOD performance. This work highlights a gap between theoretical accuracy gains and practical impact on downstream systems.

## Implications
Practitioners should prioritize behavioral compatibility when evaluating model replacements to prevent hidden costs in decision logic reconfiguration. The findings caution against treating any deviation from dense accuracy as purely beneficial or harmful, urging more holistic evaluation of deployment outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27031v1)
