---
title: SAFE-CHEM: Uncertainty-Aware Policy Switching for Robust Robotic Chemistry
published: 2026-08-10T08:51:43Z
authors: Laura Jones, Shazil Shahzad, Ayesha Sana, Gabriella Pizzuto
url: http://arxiv.org/abs/2608.09303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAFE-CHEM: Uncertainty-Aware Policy Switching for Robust Robotic Chemistry

## Abstract
The deployment of autonomous robotic systems in chemistry laboratories is accelerating experimental workflows and providing the foundational data for AI-driven scientific discovery. However, despite the success of data-driven methods in acquiring dexterous skills, safety remains a primary barrier to their deployment in high-risk domains, such as early-stage materials chemistry experiments. Specifically, learning-based policies frequently struggle to distinguish between safe and unsafe actions, leading to overconfident extrapolation and potentially catastrophic failures. To mitigate these safety risks, we propose SAFE-CHEM, an uncertainty-aware framework designed for robust, learning-based robotic chemists. Our approach leverages an ensemble of recurrent neural network-based imitation learning policies to quantify epistemic uncertainty online through the variance of action predictions. By characterising the success-conditioned density of this variance using kernel density estimation, we introduce a hybrid control architecture that autonomously switches from the learned policy to a deterministic, rule-based backup controller when uncertainty exceeds a calibrated safety threshold. We evaluate SAFE-CHEM across three fundamental laboratory manipulation tasks, where our empirical results demonstrate that this hybrid strategy improves overall task success rates and reduces critical safety violations compared to traditional single-policy baselines. Finally, we demonstrate the practical viability of the framework through zero-shot sim-to-real transfer onto a physical Franka Production 3 robot manipulator.

## Metadata
- **Published**: 2026-08-10T08:51:43Z
- **Authors**: Laura Jones, Shazil Shahzad, Ayesha Sana, Gabriella Pizzuto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09303v1)