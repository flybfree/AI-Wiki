---
title: OPDSearch+: On-Policy Distillation with RL Refinement for Search-Augmented Reasoning
published: 2026-08-25T09:39:16Z
authors: Qinglin Ye, Zhiyuan Gu, Jingjie Xia, Yiheng Zhang, Kaiyan Zhao, Shunchao Zheng, Yuhang Mu, Wenchao Du, Yiming Wang
url: http://arxiv.org/abs/2608.24310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OPDSearch+: On-Policy Distillation with RL Refinement for Search-Augmented Reasoning

## Abstract
Search-augmented reasoning remains difficult for small language models. On-policy distillation (OPD) from trained teachers offers a promising direction, but suffers from two issues: (1) high-quality multi-turn search trajectories depend on dynamic retriever responses, making SFT data prohibitively expensive to collect at scale; (2) task-specifically trained teachers incur substantial training cost, while directly applying OPD with an off-the-shelf teacher without task-specific fine-tuning constrains the student to the teacher's performance ceiling and suffers from severe training instability. We propose OPDSearch+, the first distillation paradigm that requires no teacher fine-tuning for search-augmented reasoning. We investigate the role of a frozen off-the-shelf instruct model as the teacher in on-policy distillation, and reveal a key insight: the teacher reshapes the student's policy distribution so that subsequent RL converges to a superior solution that RL alone cannot reach. In stage one, the student interacts with a live search engine and is distilled via a per-position forward KL objective, transferring reasoning decomposition and evidence integration skills without any task-specific teacher training. In stage two, RL refines the distilled student from a richer behavioral foundation, achieving performance that RL alone cannot reach from scratch. Across seven QA benchmarks, OPDSearch+ with a 3B model consistently outperforms all prior 3B RL baselines, achieving gains of 13.1% on HotpotQA and 8.5% on 2WikiMultihopQA.

## Metadata
- **Published**: 2026-08-25T09:39:16Z
- **Authors**: Qinglin Ye, Zhiyuan Gu, Jingjie Xia, Yiheng Zhang, Kaiyan Zhao, Shunchao Zheng, Yuhang Mu, Wenchao Du, Yiming Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24310v1)