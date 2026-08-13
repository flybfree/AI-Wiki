---
title: Language-Structured Relational Q-Learning for Threat-Aware Control in Safety-Critical Driving
published: 2026-08-11T23:24:01Z
authors: Aditya Humnabadkar, Huaizhong Zhang, Ardhendu Behera
url: http://arxiv.org/abs/2608.11498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language-Structured Relational Q-Learning for Threat-Aware Control in Safety-Critical Driving

## Abstract
Natural-language-based scenario generation offers an intuitive means of describing rare and complex driving interactions, yet it is still uncertain whether training with language-structured data leads to truly adaptive control policies. We propose Language-Structured Relational Q-Learning, instantiated through an Ego-Centric Relational Q-Network (ERQ-Net), which jointly learns inter-vehicle relevance and action values from dynamic traffic graphs. Language descriptions define surrounding-vehicle behaviours during training, while prompts and semantic actor roles are hidden from the policy. ERQ-Net must therefore infer threat relevance solely from observable kinematics and interactions. Across 2,500 safety-critical scenarios, language-structured training improves test success from 49-52% to 55-58% and increases adversary-focused attention from 1.2x to 2.1x, demonstrating emergent threat awareness. However, this representational gain does not consistently translate into adaptive control: trained policies perform similarly to the best constant action, while a portfolio of simple policies solves 76% of scenarios. We formalise this discrepancy as a recognition-control gap and show that reward reweighting and margin shaping do not eliminate the resulting policy collapse. Evaluations of realism, criticality, semantic accuracy, and transfer of state-interface representations to CARLA further highlight both the strengths and the constraints of language-structured relational policy learning in safety-critical driving scenarios.

## Metadata
- **Published**: 2026-08-11T23:24:01Z
- **Authors**: Aditya Humnabadkar, Huaizhong Zhang, Ardhendu Behera
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11498v1)