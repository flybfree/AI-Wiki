---
title: CrashDiffuser: VLM-Guided Collision Intent Reasoning for Fine-Grained Safety-Critical Traffic Scenario Generation
published: 2026-09-02T08:18:20Z
authors: Shucheng Zhang, Yuang Zhang, Bingzhang Wang, Muhammad Monjurul Karim, Kehua Chen, Yinhai Wang
url: http://arxiv.org/abs/2609.02270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CrashDiffuser: VLM-Guided Collision Intent Reasoning for Fine-Grained Safety-Critical Traffic Scenario Generation

## Abstract
Generating safety-critical scenarios is essential for evaluating autonomous driving systems. However, existing generators primarily focus on inducing collisions and offer limited control over where contact occurs on the target vehicle. In this paper, we study fine-grained safety-critical scenario generation, where success requires both a target collision and a specified head, rear, or side contact region. We propose CrashDiffuser, a closed-loop VLM-guided diffusion framework that decouples semantic collision reasoning from continuous trajectory synthesis through a hierarchical collision-intent interface derived from the requested target contact region. At initialization, the VLM extracts reusable scene-level context; at each replanning step, it predicts a structured action tuple describing speed change, turning behavior, and collision stage. This intent conditions a diffusion model to generate executable adversarial trajectories, while collision-guided sampling, candidate selection, and short-horizon replanning adapt generation to the target vehicle's evolving behavior. On WOMD-derived closed-loop scenarios, CrashDiffuser achieves a target-collision rate of 50.33% in a single attempt and 67.98% after three attempts, together with a contact-region control success rate of 40.05% and competitive trajectory naturalness. Component ablations further support the proposed design.

## Metadata
- **Published**: 2026-09-02T08:18:20Z
- **Authors**: Shucheng Zhang, Yuang Zhang, Bingzhang Wang, Muhammad Monjurul Karim, Kehua Chen, Yinhai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02270v1)