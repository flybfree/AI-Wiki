---
title: Augmenting Human Performance with an XR Agent Learning from Online Behavior and BCI Evidence
url: http://arxiv.org/abs/2608.30369v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_07-25-51Z_AugmentingHumanPerformancewithanXRAgentLearningfro.md
generated_at: 2026-08-31 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OLIVE, a framework that adapts a frozen vision-language model to guide users in real-time XR tasks by fusing passive EEG and online behavioral signals. Experiments show OLIVE outperforms prior test‑time adaptation methods, delivering the highest convergence rate while maintaining fast adaptation when target switches occur.

## Key Takeaways
- OLIVE combines explicit behavioral targets from an XR shooter with implicit physiological fixation‑locked EEG to estimate per‑source reliability without manual labels or offline training. - The fusion enables the agent to extend users’ detection bandwidth beyond unaided performance, achieving a larger and more reliable within‑session improvement independent of user skill. - When target switches silently, OLIVE reconverges 1.27 times faster than behavior‑only agents (p = .008), restoring trustworthy guidance precisely when it matters.

## Context
Current assistive AI systems rely on either offline training or manual labeling to personalize performance, limiting real‑time responsiveness in dynamic environments like virtual reality. Integrating continuous physiological and behavioral data offers a path toward truly adaptive agents that can react instantly to task changes without retraining.

## Implications
For industry practitioners, OLIVE demonstrates that lightweight, trustworthy guidance can be delivered on‑device using only passive EEG and observable actions, reducing reliance on expensive hardware or cloud services. This approach could accelerate adoption of AI‑enhanced XR experiences across gaming, training, and rehabilitation domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30369v1)
