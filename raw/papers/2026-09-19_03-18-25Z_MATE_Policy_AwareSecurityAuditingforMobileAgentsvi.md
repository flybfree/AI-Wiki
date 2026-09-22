---
title: MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning
published: 2026-09-19T03:18:25Z
authors: Changyue Jiang, Jiayi Wang, Xin Wen, Jiarun Dai, Geng Hong, Xudong Pan
url: http://arxiv.org/abs/2609.22724v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning

## Abstract
Mobile agents powered by foundation models now automate complex, multi-step workflows on real devices, but their trajectories can violate app-specific security policies. Existing trajectory-level defenses rely on LLM prompting or rigid rules, and thus fail to support fine-grained, natural-language policies that generalize across apps and tasks. In this work, we introduce MATE, a lightweight, policy-conditioned auditor that encodes both agent trajectories and natural-language security policies to determine whether a trajectory violates a given policy and to explain why. Treating policies as editable text rather than fixed model parameters allows MATE to handle user-defined and evolving requirements without retraining. To construct MATE, we build a knowledge base by extracting app descriptions, workflows, and policies from hundreds of popular mobile apps worldwide, and synthesizing over 140K semantically realistic, policy-conditioned trajectories with a multi-stage pipeline. We further release MATEBench, a trajectory-level auditing benchmark with two synthetic subsets and one real-world subset of manually collected trajectories. Models trained with our synthesis-driven trajectory learning achieve over 95% accuracy on MATEBench, retain strong performance on external safety benchmarks, and audit trajectories from Zhipu's AutoGLM and Alibaba's Mobile-Agent on real devices with over 95% accuracy, outperforming prior methods by over 20%. MATE shows that practical, fine-grained security auditing for heterogeneous mobile agents is both feasible and effective.

## Metadata
- **Published**: 2026-09-19T03:18:25Z
- **Authors**: Changyue Jiang, Jiayi Wang, Xin Wen, Jiarun Dai, Geng Hong, Xudong Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22724v1)