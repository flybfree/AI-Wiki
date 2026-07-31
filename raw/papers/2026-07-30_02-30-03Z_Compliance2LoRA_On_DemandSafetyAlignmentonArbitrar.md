---
title: Compliance2LoRA: On-Demand Safety Alignment on Arbitrary Policy Subsets via Hypernetwork-Generated LoRA Adapters
published: 2026-07-30T02:30:03Z
authors: Pankayaraj Pathmanathan, Furong Huang
url: http://arxiv.org/abs/2607.27594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compliance2LoRA: On-Demand Safety Alignment on Arbitrary Policy Subsets via Hypernetwork-Generated LoRA Adapters

## Abstract
Post-training alignment in large reasoning models (LRMs) has significantly improved their adaptability to diverse safety compliance settings. However, as LRMs personalization for downstream users takes center stage, the demand for varying levels of policy compliance grows as different user-specific LRMs must adhere to distinct subsets of safety policies. Training a separate LRM for each policy subset introduces severe combinatorial overhead. While in context learning methods overcome this combinatorial overhead, they introduce additional computational challenges associated with long context generation. To address this challenge, we propose \ours, a unified adaptive hypernetwork-based framework for multi-policy compliance. In our framework, safety policies serve as customizable inputs to a LoRA adapter generator, which learns to produce policy compliant LoRA weights for downstream LRM. When added to the LRM these weights enable the generation of responses compliant with the specified policy subsets. In this work, we demonstrate that training such a hypernetwork enables on-demand policy adjustments on a single LRM without sacrificing task performance across reasoning models of different sized and different evaluation datasets. This highlights the effectiveness and practicality of adaptive hypernetwork based alignment in LRMs.

## Metadata
- **Published**: 2026-07-30T02:30:03Z
- **Authors**: Pankayaraj Pathmanathan, Furong Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27594v1)