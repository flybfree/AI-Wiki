---
title: Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation
url: http://arxiv.org/abs/2608.20797v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_07-16-36Z_AutomatedTrajectoryEvaluationforMobileAgentsviaSte.md
generated_at: 2026-08-23 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CRATE, a two‑stage visual language model framework that evaluates mobile agents by reasoning at each step and then aggregating evidence for task completion. The two‑stage design also reduces computational load compared with holistic models. Experiments show CRATE reaches an F1 score of 0.833 on AndroidWorld, surpassing SPA‑Bench, while its safety extension CRATE‑S scores 0.697 on MobileRisk.

## Key Takeaways
- CRATE separates step‑level consequence reasoning from trajectory aggregation to avoid context overload.
- The framework works with both open and closed source language models by using a VLM as judge.
- Safety assessment is added via CRATE‑S, which evaluates operational safety in addition to task completion. CRATE’s step‑level reasoning isolates visual clues and action‑conditioned state changes, enabling precise evidence extraction.

## Context
Automated evaluation of mobile agents has moved beyond rule‑based methods toward model‑driven approaches that require scalable, context‑aware reasoning. Existing holistic evaluations often ignore intermediate steps and safety concerns, limiting reliability in real‑world deployment. This work addresses those gaps by introducing a step‑level mechanism.

## Implications
The CRATE framework enables developers to obtain quantitative evidence for both task success and operational safety without manual inspection. As mobile agents become more autonomous, such automated evaluation tools will be essential for trustworthy AI systems across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20797v1)
