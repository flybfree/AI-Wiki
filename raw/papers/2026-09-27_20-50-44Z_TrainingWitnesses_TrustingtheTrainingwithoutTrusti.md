---
title: Training Witnesses: Trusting the Training without Trusting the Trainer
published: 2026-09-27T20:50:44Z
authors: Houjun Liu, Pratyusha Sharma
url: http://arxiv.org/abs/2609.33915v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Witnesses: Trusting the Training without Trusting the Trainer

## Abstract
Progress in machine learning cannot outpace our ability to verify it. With an explosion in papers today, every scientific claim rests initially on trust in the trainer, leading to uneven evaluation, baselines, and forestalling of reliable progress. Traditionally, the burden of verification falls on the reader, who must reproduce expensive training runs. This strategy is impractical due to an explosion in slop contributions, diversity of methods, and the sheer compute required. We put the burden of proof where it belongs, on the trainer, and in the process also cut the overall cost of verification significantly. We introduce Witnesses, a method for certifying training, data usage and evaluation in a neural network training run. Our key insight is that fast behavioral fingerprints with occasional replay challenges are sufficient for auditing neural network training. Our method is applicable at scale with minimal overhead to the trainer, is cheap for the verifier, rejects bad training runs with amplifiable probability, and allows for exact queries of both data inclusion and exclusion. We test our method on language model training runs from 100M to 2B scales, across DDP and FSDP, and demonstrate this minimal overhead. We also introduce a self-regulating leaderboard of "auto-certified" training runs that enables shared baselines and progress. We invite the community to participate in the leaderboard to improve reproducibility in machine learning.

## Metadata
- **Published**: 2026-09-27T20:50:44Z
- **Authors**: Houjun Liu, Pratyusha Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33915v1)