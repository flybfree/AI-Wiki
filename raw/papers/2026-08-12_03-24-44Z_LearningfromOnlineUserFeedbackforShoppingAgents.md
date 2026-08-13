---
title: Learning from Online User Feedback for Shopping Agents
published: 2026-08-12T03:24:44Z
authors: Haobo Zhang, Kelong Mao, Sulong Xu, Simiu Gu, Zhicheng Dou
url: http://arxiv.org/abs/2608.11604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Online User Feedback for Shopping Agents

## Abstract
Large language model-based shopping agents are increasingly deployed in real-world e-commerce platforms, generating massive amounts of user interaction logs that provide valuable supervision for improving these agents. However, existing approaches primarily rely on offline training signals, such as user-item interactions or synthetic preference data, while largely overlooking the rich supervision contained in users' natural conversational feedback. Moreover, the available online feedback is heterogeneous, sparse, and noisy, making it difficult to transform into reliable learning signals automatically. To address these challenges, we propose LOFA, a framework that enables shopping agents to learn directly from real online interaction logs without human annotation. LOFA combines reinforcement learning over verifiable purchase outcomes with feedback-aware on-policy distillation, which identifies users'in-dialogue directives and converts them into dense token-level supervision. These complementary objectives capture both collaborative behavioral patterns and user-specific preferences. Extensive experiments on real-world e-commerce logs demonstrate that LOFA consistently improves recommendation quality, response helpfulness, and user-satisfaction alignment over strong baselines, highlighting the effectiveness of learning shopping agents from real online user feedback.

## Metadata
- **Published**: 2026-08-12T03:24:44Z
- **Authors**: Haobo Zhang, Kelong Mao, Sulong Xu, Simiu Gu, Zhicheng Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11604v1)