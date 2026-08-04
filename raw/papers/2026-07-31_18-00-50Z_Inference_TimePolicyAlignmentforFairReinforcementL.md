---
title: Inference-Time Policy Alignment for Fair Reinforcement Learning
published: 2026-07-31T18:00:50Z
authors: Umer Siddique, Peilang Li, Conor Wallace, Yongcan Cao
url: http://arxiv.org/abs/2608.00175v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inference-Time Policy Alignment for Fair Reinforcement Learning

## Abstract
Deep reinforcement learning (RL) agents achieve strong performance by optimizing scalar reward functions. However, once deployed, the policies of these RL agents are often rigid and costly to adapt to new performance criteria. For instance, an agent trained to maximize expected cumulative reward may not accommodate previously unknown stakeholder preferences. Existing approaches to achieve fairness, a type of preference, in RL typically assume that such preferences are known a priori and require complete retraining of the policy under a fairness-oriented metric. Inspired by inference-time alignment in large language models, we investigate the problem of steering a pretrained RL policy toward welfare-based fairness objectives at inference time without updating the base policy's parameters. We formalize inference-time fairness alignment as a policy shaping problem and propose a multiplicative policy shaping framework that adjusts action probabilities using action-dependent welfare scores, thus requiring no modification to the base policy. Our framework is general and compatible with any deep RL agent. Through extensive experiments across multiple domains, we demonstrate that inference-time policy shaping substantially improves welfare-based fairness objectives while preserving core task performance.

## Metadata
- **Published**: 2026-07-31T18:00:50Z
- **Authors**: Umer Siddique, Peilang Li, Conor Wallace, Yongcan Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00175v1)