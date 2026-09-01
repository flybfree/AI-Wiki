---
title: Learning Action Models with Conditional and Quantified Effects via Uncertainty-Guided Exploration
url: http://arxiv.org/abs/2608.30955v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-23-43Z_LearningActionModelswithConditionalandQuantifiedEf.md
generated_at: 2026-08-31 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
Accurate action models are essential for effective planning, yet existing methods struggle with complex conditional and quantified effects. The paper introduces Online Hypothesis-Driven Conditional Action Model Learning (OHCAM), an online algorithm that learns such models from limited environment interactions. Experiments show OHCAM is sample efficient and outperforms baselines on six benchmark domains.

## Key Takeaways
- OHCAM maintains a belief over hypothesized action models and selects actions to maximize disagreement among competing hypotheses, reducing uncertainty despite noisy observations.
- The method starts with simple action model hypotheses and only expands to more complex conditions when current ones become inconsistent with data.
- On Kinova Gen3 robot tasks, OHCAM achieves real-world performance that surpasses baselines.

## Context
Learning models that can condition on multiple factors and quantify their effects remains a bottleneck in planning AI. Current approaches either simplify representations or require prohibitive computational resources, limiting practical deployment.

## Implications
This work demonstrates that uncertainty-guided exploration can yield scalable action learning solutions for complex robotics and autonomous systems. Practitioners can adopt OHCAM to build more robust planners without sacrificing sample efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30955v1)
