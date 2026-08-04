---
title: Question Begets Question: Self-Evolving Curriculum for Reinforcement Fine-Tuning on Competition Mathematics
published: 2026-08-02T22:19:01Z
authors: Longtian Bao, Jianyou Wang, Yang Zhang, Youze Zheng, Ramamohan Paturi
url: http://arxiv.org/abs/2608.01522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Question Begets Question: Self-Evolving Curriculum for Reinforcement Fine-Tuning on Competition Mathematics

## Abstract
Teaching a language model a skill it has not mastered is obstructed by three recurring difficulties: training data is scarce, ground-truth reasoning traces are usually unavailable, and models often exhibit an apparent ceiling beyond which additional data yields no further improvement. We study these difficulties in a controlled setting, fine-tuning Qwen2.5-Math-7B on competition mathematics (AIME), a task on which it initially solves only 5.6\% of problems (pass@1). To address data scarcity, we introduce Question-begets-Question (QbQ), a scalable procedure in which a teacher transforms existing problems into diverse variants that probe the same underlying skills; to model the absence of oracle reasoning, we train exclusively via reinforcement learning on problem statements and final answers, never on teacher reasoning traces. Static training on such data, however, plateaus well short of the task: real-plus-synthetic augmentation and non-curriculum QbQ generated synthetic data training cap pass@1 at 12.5\% and 14.5\% respectively, despite large increases in data. Our central finding is that this ceiling is not intrinsic to the model. We propose a self-evolving curriculum that, each round, evaluates the current checkpoint, seeds QbQ from the problems it can mostly get right, and trains on the resulting variants; under an identical data budget, this breaks the ceiling and lifts pass@1 to 16.5\% with no sign of saturation after 20 rounds. Counterintuitively, we find that models improve when trained on variants of problems they can mostly get right, and that models trained this way go on to solve harder problems never seen during training.

## Metadata
- **Published**: 2026-08-02T22:19:01Z
- **Authors**: Longtian Bao, Jianyou Wang, Yang Zhang, Youze Zheng, Ramamohan Paturi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01522v1)