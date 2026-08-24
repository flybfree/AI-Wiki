---
title: ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models
published: 2026-08-21T13:47:21Z
authors: Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai, Dawei Feng, Huaimin Wang
url: http://arxiv.org/abs/2608.21100v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models

## Abstract
While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two key obstacles, utility dominance and reasoning inertia, which cause models to overlook latent risks or follow malicious reasoning trajectories. Guided by these insights, we propose ReFrame, a training-free multimodal input reframing framework where two agents share a lightweight locally deployed MLLM: the evidence-generation agent constructs complementary risk and utility evidence, and the rewrite-and-routing agent converts it into a safe proxy prompt and image-routing decision before calling the downstream MLLM, without modifying it or accessing its internal information. Experiments across multiple MLLMs and benchmarks show that ReFrame improves jailbreak defense, safety awareness, and oversensitivity reduction while preserving multimodal utility.

## Metadata
- **Published**: 2026-08-21T13:47:21Z
- **Authors**: Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai, Dawei Feng, Huaimin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21100v1)