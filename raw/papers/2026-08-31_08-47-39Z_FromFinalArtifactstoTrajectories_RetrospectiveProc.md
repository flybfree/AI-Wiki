---
title: From Final Artifacts to Trajectories: Retrospective Process Supervision for Evidence-Grounded Long-Form Generation
published: 2026-08-31T08:47:39Z
authors: Junjie Huang, Jiarui Qin, Di Yin, Weiwen Liu, Yong Yu, Xing Sun, Weinan Zhang
url: http://arxiv.org/abs/2608.30461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Final Artifacts to Trajectories: Retrospective Process Supervision for Evidence-Grounded Long-Form Generation

## Abstract
Trajectory data is getting more vital for training large language models for boosting the agentic abilities. Unlike the verifiable domains such as coding or mathematics, scaling trajectory data for open-ended tasks is much more difficult because these tasks lack singular ground truth and are costly to annotate or verify. In this paper, we propose RetroGen, a self-improving framework of retrospective process supervision. Our key observation is that although expert trajectories are scarce, high-quality final artifacts such as literature reviews, analyst reports and legal judgments, are abundant in pre-training data and can be viewed as compressed traces of the evidence-seeking processes that produced them. RetroGen reconstructs candidate latent trajectories from expert artifacts, verifies them against both the artifact and supporting evidence, and trains models on their own successful reconstruction data, without requiring trajectory data from stronger models. Experiments show that RetroGen improves grounding, faithful synthesis, and long-form evidence-seeking agent tasks.

## Metadata
- **Published**: 2026-08-31T08:47:39Z
- **Authors**: Junjie Huang, Jiarui Qin, Di Yin, Weiwen Liu, Yong Yu, Xing Sun, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30461v1)