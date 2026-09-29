---
title: RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning
published: 2026-09-26T07:42:16Z
authors: Ziqiao Shang, Zian Xu, Ji-Chen Yan, Weiming Wu, Ziyi Jia, Jie Meng, Tao Huang, Shan Huang, Lan-Zhe Guo
url: http://arxiv.org/abs/2609.32326v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning

## Abstract
Multimodal reasoning requires models to preserve visual evidence through long decision chains while selecting appropriate procedures across diverse scenarios and rules. When learning is guided only by terminal verifiers, reinforcement learning (RL) reveals whether a final answer is correct but not how it should be produced. The policy must therefore discover reusable reasoning procedures while learning to execute them, creating a program cold-start problem. Skills can externalize successful procedures, reduce repeated exploration, and provide inspectable guidance. However, a fixed Skill Bank assumes that this guidance remains compatible with an evolving policy, while updating Skills alone can leave their triggers, execution protocols, and demonstrations stale or mutually inconsistent. We introduce RLHARNESS, which organizes Skills, selection and execution protocols, few-shot demonstrations, and task contracts into a unified, versioned Harness and alternates Harness evolution with policy learning. An Exploration-Distillation Harness builds the initial Harness and version-aligned verified traces for SFT and DAPO I. After the first RL block, a Post-RL Reconstruction Harness rebuilds Skills, protocols, and demonstrations from fresh success-failure rollouts, and DAPO II adapts the policy to the reconstructed program. RLHARNESS improves Accuracy from 16.25%/27.50% to 62.00%/50.00% on MetroMap/TravelMap and raises F1 score from 37.13%/45.50% to 65.81%/65.51% on Fee-VL/Cancel-VL. All four tasks achieve their best results only after reconstruction and DAPO II, showing that an evolving Harness complements RL by continually updating the external program that the policy learns to execute.

## Metadata
- **Published**: 2026-09-26T07:42:16Z
- **Authors**: Ziqiao Shang, Zian Xu, Ji-Chen Yan, Weiming Wu, Ziyi Jia, Jie Meng, Tao Huang, Shan Huang, Lan-Zhe Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32326v1)