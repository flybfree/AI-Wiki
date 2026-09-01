---
title: Learning Action Models with Conditional and Quantified Effects via Uncertainty-Guided Exploration
published: 2026-08-31T15:23:43Z
authors: Jeffrey Jewett, William Solow, Sandhya Saisubramanian
url: http://arxiv.org/abs/2608.30955v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Action Models with Conditional and Quantified Effects via Uncertainty-Guided Exploration

## Abstract
Accurate action models are critical for effective planning. Existing action-model learning methods largely assume simple action representations or become computationally intractable when learning conditional and quantified effects. We present Online Hypothesis-Driven Conditional Action Model Learning (OHCAM), an online approach for learning action models with conditional and quantified effects from limited interactions with the environment. OHCAM maintains a belief over hypothesized action models and actively selects informative actions to reduce uncertainty by maximizing disagreement among competing hypotheses, while being robust to noisy observations. To enable scalability, OHCAM begins with a small set of simple action model hypotheses and expands to more complex conditions only when the current hypotheses become inconsistent with the data. Experiments on six benchmark planning domains demonstrate that OHCAM is sample efficient in learning action models that solve substantially more tasks than baselines, even with observation noise. We validate OHCAM on two tasks using a Kinova Gen3 robot, demonstrating the real-world applicability of our approach.

## Metadata
- **Published**: 2026-08-31T15:23:43Z
- **Authors**: Jeffrey Jewett, William Solow, Sandhya Saisubramanian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30955v1)