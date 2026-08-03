---
title: MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation
published: 2026-07-31T11:51:04Z
authors: Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng
url: http://arxiv.org/abs/2607.29320v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation

## Abstract
Graphical user interface (GUI) agents based on large language models are increasingly deployed across mobile, web, and desktop environments. However, existing agents are typically domain-specific, limiting the deployment and user experience. This motivates the consolidation of specialized models into a single cross-environment policy. Weight merging directly merges domain-specific experts but can corrupt executable actions under expert disagreement, while on-policy distillation (OPD) avoids conflicting teacher supervision yet still treats all response tokens equally during distillation, ignoring that action tokens are the only interface between the environment and the agent. To address this, We introduce MAGA that re-allocates training signal according to the structured action. Based on the correctness of the generated action, it suppresses unnecessary or invalid distillation signals and focuses learning on erroneous actions. Besides, a training-only hint optimizes the supervision signal provided by domain-specific teachers without changing the student input. Across two model scales, MAGA achieves the highest mean success rate, outperforming the strongest baseline by 2.0% at 8B and achieves almost the same average performance with teachers.

## Metadata
- **Published**: 2026-07-31T11:51:04Z
- **Authors**: Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29320v1)