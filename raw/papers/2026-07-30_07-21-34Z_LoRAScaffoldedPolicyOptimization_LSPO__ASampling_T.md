---
title: LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts
published: 2026-07-30T07:21:34Z
authors: Ken Ding
url: http://arxiv.org/abs/2607.27787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts

## Abstract
Reinforcement learning from verifiable rewards (RLVR) for mathematical reasoning suffers from a structural blind spot: on "cliff" prompts-those on which every sampled rollout in a group fails-the group-normalized advantage is identically zero, so GRPO produces no gradient on precisely the prompts at the frontier of the model's capability. We introduce LoRA Scaffolded Policy Optimization (LSPO), a sampling-time mechanism that recovers this lost gradient. Each RL step, LSPO detects cliff prompts, fits a small low-rank (LoRA) adapter by a brief supervised step on their ground-truth solutions, re-rolls the cliffs with the base-plus-adapter model, splices the now-successful completions back into the RL batch with an importance-sampling correction, and takes a GRPO step on the base alone; the adapter receives only the supervised gradient and is discarded at checkpoint, yielding a base-only model. On DeepMath-103K with DeepSeek-R1-Distill-Qwen-1.5B, evaluated over n=5 paired seeds per arm at a matched 1000-step reporting horizon, LSPO's 5-seed mean matches or beats a DAPO baseline on all 16 (benchmark, pass@k) cells (15 strict wins and one exact tie), with gains of up to +10.7 points on AIME24/pass@4, +6.7 points on AIME24 and AIME26 at pass@16, and +2.4 points on MATH500/pass@1; averaged over the 16 cells the improvement is +3.8 points.

## Metadata
- **Published**: 2026-07-30T07:21:34Z
- **Authors**: Ken Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27787v1)