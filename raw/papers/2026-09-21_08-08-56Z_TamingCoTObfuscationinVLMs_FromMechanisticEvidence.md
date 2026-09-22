---
title: Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement
published: 2026-09-21T08:08:56Z
authors: Xutao Mao, Jianing Zhu, Jinman Zhao, Tongliang Liu, Xiaowen Chu, Cong Wang, Bo Han
url: http://arxiv.org/abs/2609.24243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement

## Abstract
Reinforcement learning (RL) improves reasoning in vision-language models (VLMs) but can induce chain-of-thought (CoT) obfuscation: an operational, non-intentional outcome where task reward or accuracy rises while traces become less grounded and monitorable. Prior work largely documents this decay behaviorally, leaving its representation-level correlates and actionable controls unclear. We find that template- and ground-associated activations become less separable during RL; matched interventions support the contribution of selected features to monitorability degradation. Guided by this evidence, we propose Targeted Anti-obfuscation with Mechanistic Enforcement (TAME), which uses Sparse Autoencoders (SAEs) to combine behavioral feedback with targeted suppression of template-associated activations during RL. Its asymmetric constraint penalizes template activations only above their pre-RL baseline, anchoring the localized features while behavioral feedback promotes grounded refinements. Across VIRL-39k, SPA-VL, and two model families, TAME improves CoT monitorability by up to 30.9 and 16.7 percentage points over Group Relative Policy Optimization (GRPO), respectively. Blinded human evaluation finds higher human monitorability on both datasets, and two held-out monitor families reproduce the monitorability gains. Task accuracy changes are small and mixed, and general-capability benchmarks show task-specific trade-offs. These results provide a path from behavioral monitoring to representation-level oversight for more auditable RL-trained multimodal systems.

## Metadata
- **Published**: 2026-09-21T08:08:56Z
- **Authors**: Xutao Mao, Jianing Zhu, Jinman Zhao, Tongliang Liu, Xiaowen Chu, Cong Wang, Bo Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24243v1)