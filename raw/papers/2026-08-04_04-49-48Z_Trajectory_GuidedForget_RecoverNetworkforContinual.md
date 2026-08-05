---
title: Trajectory-Guided Forget-Recover Network for Continual LLM Unlearning
published: 2026-08-04T04:49:48Z
authors: Zezheng Wu, Xinghe Cheng, Qinggang Zhang, Haoran Luo, Jiapu Wang, Qing Yang, Jingwei Zhang
url: http://arxiv.org/abs/2608.03123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory-Guided Forget-Recover Network for Continual LLM Unlearning

## Abstract
Machine unlearning aims to eliminate the influence of sensitive data on a model. In the real world, unlearning requests arrive continually, which gives rise to two challenges. First, an unlearning intervention may redistribute target-related computation across remaining pathways, allowing previously forgotten knowledge to re-emerge. Second, repeated unlearning interventions may progressively reduce the model capacity needed to preserve retained utility. To address these challenges, we propose the Trajectory-guided Forget-Recover Network (TFR-Net). TFR-Net tracks channel-level risk across requests. It separates persistent target-related channels from transient hotspots and suppresses only the persistent ones. TFR-Net also recovers model capacity by reactivating dormant channels. These channels make strong contributions to retained utility and show low current and historical forget risk. The recovery is accepted only when retained-utility degradation remains within a predefined tolerance. Experiments on four datasets show that TFR-Net consistently achieves a more favorable trade-off between unlearning effectiveness and retained utility than representative baselines.

## Metadata
- **Published**: 2026-08-04T04:49:48Z
- **Authors**: Zezheng Wu, Xinghe Cheng, Qinggang Zhang, Haoran Luo, Jiapu Wang, Qing Yang, Jingwei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03123v1)