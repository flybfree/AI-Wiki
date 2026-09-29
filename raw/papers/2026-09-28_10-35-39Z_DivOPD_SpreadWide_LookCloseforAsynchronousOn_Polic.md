---
title: DivOPD: Spread Wide, Look Close for Asynchronous On-Policy Distillation of Multi-turn Agents
published: 2026-09-28T10:35:39Z
authors: Hanyang Wang, Zeyuan Liu, Zhengyu Chen, Jingqing Ruan, Chaoxu Pang, Zhongda Su, Wulin Xie, Zhizhao Zeng, Ke Zeng, Tianxiang Zhao
url: http://arxiv.org/abs/2609.34838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DivOPD: Spread Wide, Look Close for Asynchronous On-Policy Distillation of Multi-turn Agents

## Abstract
On-policy distillation (OPD) trains student agents through teacher supervision on their own interactions with an environment. However, in asynchronous multi-turn training, arrival-order batching can allow a few early or long rollouts to dominate learner updates while other valid rollouts become stale before being used, wasting already-generated experience. To address this problem, we introduce DivOPD, a simple learner-side batch-selection method that spreads a fixed turn budget across more rollouts and, within each rollout, prioritizes turns with larger cumulative teacher-student disagreement. Turns without usable teacher feedback are excluded. The per-turn loss and optimizer remain fixed; selection only changes which student-visited turns receive training weight. For no-progress rollouts, an optional extension briefly hands control to the teacher before returning it to the student. Across six teacher-student settings on the simulated ALFWorld, ScienceWorld, and WebShop benchmarks, with 1.5B-7B students, DivOPD raises cross-setting mean peak success rate from 77.4 to 84.4 and mean success over the last five evaluations from 71.5 to 78.6. It reaches all reported setting-specific targets with geometric-mean speedups of 1.84x in training tokens and 1.87x in learner GPU time relative to vanilla OPD. Teacher intervention further raises this last-five mean to 82.4 while retaining about 1.7x learner-GPU speedup over vanilla OPD. Code will be released at https://github.com/HanyangWang0418-oss/DivOPD.

## Metadata
- **Published**: 2026-09-28T10:35:39Z
- **Authors**: Hanyang Wang, Zeyuan Liu, Zhengyu Chen, Jingqing Ruan, Chaoxu Pang, Zhongda Su, Wulin Xie, Zhizhao Zeng, Ke Zeng, Tianxiang Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34838v1)