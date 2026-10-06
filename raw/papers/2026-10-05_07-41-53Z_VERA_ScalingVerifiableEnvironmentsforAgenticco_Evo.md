---
title: VERA: Scaling Verifiable Environments for Agentic co-Evolution
published: 2026-10-05T07:41:53Z
authors: Junqi Liu, Yongyang Pan, Zhuosong Jiang, Dongbai Li, Bo Zhang, Xitong Ling, Sheng Wang, Hanrong Ye, Yufan He, Can Zhao, Pengfei Guo, Dong Yang, Andriy Myronenko, Yuyin Zhou, Tianyu Liu, Daguang Xu, Yucheng Tang
url: http://arxiv.org/abs/2610.05923v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VERA: Scaling Verifiable Environments for Agentic co-Evolution

## Abstract
Competent agents need precise and verifiable environments, such as sandboxes that are resumable at any stage and evolve from observable evidence. However, most long-horizon work exposes how rare these are: for example, an agent in medical research must ground a finding, classify it, and write a report over dozens of dependent steps, yet recent environments score only the outcome. To address the challenges in stable training, we present VERA, which builds such environments at scale and lets agents evolve on them. VERA builds these environments from initial trajectories: an agent writes rubrics, executable checks, a judge verifies each sandbox, and only those that pass enter the training bank. On these environments, VERA alternates between two updates: train the model with rubric rewards, or edit the harness skills. We also create a verifier which gates model checkpoints and harness edits using explicit development-set acceptance criteria. This attribution distinguishes VERA's co-evolution from single-axis baselines: its updates target not only the cause but the outcome. With an open-source corpus of 9,000+ long-horizon verifiable environments, a 9B model paired with its co-evolved agent beats the strongest baseline by 10.3 and 13.0 points in the two domains. At 27B, it surpasses the baseline on AutoCoWorkBench (71.6) and AutoMedBench (80.7), transfers to unseen workflows, and retains general capabilities.

## Metadata
- **Published**: 2026-10-05T07:41:53Z
- **Authors**: Junqi Liu, Yongyang Pan, Zhuosong Jiang, Dongbai Li, Bo Zhang, Xitong Ling, Sheng Wang, Hanrong Ye, Yufan He, Can Zhao, Pengfei Guo, Dong Yang, Andriy Myronenko, Yuyin Zhou, Tianyu Liu, Daguang Xu, Yucheng Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05923v1)