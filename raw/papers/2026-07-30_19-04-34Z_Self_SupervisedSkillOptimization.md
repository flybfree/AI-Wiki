---
title: Self-Supervised Skill Optimization
published: 2026-07-30T19:04:34Z
authors: Siran Peng, Cuiyu Yang, Tianyu Fu, Tianshuo Zhang, Haoyuan Zhang, Weisong Zhao, Anyang Su, Minghui Wu, Huiying Li, Xiangyu Zhu, Chenxu Zhao, Zhen Lei
url: http://arxiv.org/abs/2607.28777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Supervised Skill Optimization

## Abstract
Agent skills provide frozen large language model (LLM) agents with reusable procedural guidance, and recent work shows that such skills can be optimized with ground-truth (GT) feedback. Many applications, however, lack GT labels, task scores, rewards, or reliable task-specific evaluators. We therefore introduce Self-Supervised Skill Optimization (SSO), a comparative framework that learns a reusable skill from unlabeled task instances alone. At each step, SSO runs the current skill on an unlabeled batch, uses a subset of the resulting executions to generate complete skill probes, and runs the probes on the same batch. An LLM judge compares the resulting answers, trajectories, artifacts, or terminal states. A separate behavior extractor identifies behavioral differences without seeing the judge's decisions. SSO uses these decisions to aggregate evidence for and against the observed behaviors across instances. It then ranks the behaviors by the resulting evidence and renders a new complete skill from the highest-ranked behaviors. The update is accepted only if the new skill outperforms the current one on an unlabeled validation set. SSO outperforms existing GT-free prompt optimizers on both closed-ended and open-ended tasks. On closed-ended benchmarks, it approaches and sometimes exceeds the strongest GT-based skill optimizer without using any GT feedback.

## Metadata
- **Published**: 2026-07-30T19:04:34Z
- **Authors**: Siran Peng, Cuiyu Yang, Tianyu Fu, Tianshuo Zhang, Haoyuan Zhang, Weisong Zhao, Anyang Su, Minghui Wu, Huiying Li, Xiangyu Zhu, Chenxu Zhao, Zhen Lei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28777v1)