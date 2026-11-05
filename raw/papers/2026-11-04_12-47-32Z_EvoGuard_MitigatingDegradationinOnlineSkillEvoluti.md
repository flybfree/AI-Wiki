---
title: EvoGuard: Mitigating Degradation in Online Skill Evolution
published: 2026-11-04T12:47:32Z
authors: Yanli Wang, Zichen Bai, Tianyue Jiang, Kunming Shao, Junhao Shi, Xueqin Liu, Jinguo Sun, Muye Li, Tingting Bi, Yanlin Wang, Shaoqiang Zheng, Xuefei Diao, Zhuwei Zeng, Nan Duan, Peng Cao
url: http://arxiv.org/abs/2611.06444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoGuard: Mitigating Degradation in Online Skill Evolution

## Abstract
Skills let language agents reuse experience across tasks as natural-language documents. Recent work evolves skills from interaction, but existing methods have limitations when skills evolve online. Prior methods update a skill offline from a batch of trajectories collected over many tasks. Some then adopt the new skill without any check, which can degrade the skill over time. Others keep it only if it improves performance on a held-out validation set, which is too slow and costly to run after every update. We introduce EvoGuard, a pairwise skill selector that mitigates skill degradation at low latency and cost. We first run the agent iteratively to build pools of skills and score each skill on a private test set to obtain utility labels. We pair the skills and use rejection sampling to keep only pairs with a clear utility gap. The selector is trained on the logits of two label tokens to pick the better skill. At deployment it decides in a single forward pass, which is significantly faster than evaluation on the private test set. Compared with adopting every new skill, EvoGuard improves success by 11.0% on ALFWorld, 5.9% on ScienceWorld, and 2.7% on LiveCodeBench.

## Metadata
- **Published**: 2026-11-04T12:47:32Z
- **Authors**: Yanli Wang, Zichen Bai, Tianyue Jiang, Kunming Shao, Junhao Shi, Xueqin Liu, Jinguo Sun, Muye Li, Tingting Bi, Yanlin Wang, Shaoqiang Zheng, Xuefei Diao, Zhuwei Zeng, Nan Duan, Peng Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.06444v1)