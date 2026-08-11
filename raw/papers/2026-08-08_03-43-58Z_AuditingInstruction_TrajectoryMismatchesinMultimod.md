---
title: Auditing Instruction-Trajectory Mismatches in Multimodal Robot Demonstrations
published: 2026-08-08T03:43:58Z
authors: Simon Holk, Ryosuke Takanami, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo, Yueh-Hua Wu, Kei Ota
url: http://arxiv.org/abs/2608.07895v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Instruction-Trajectory Mismatches in Multimodal Robot Demonstrations

## Abstract
Robot demonstration datasets used to train vision-language-action policies can contain a subtle but harmful failure mode: trajectories that are behaviorally correct but paired with the wrong language instruction. We study post-hoc auditing of these Instruction-Trajectory Mismatches (ITMs). Unlike failed rollouts, ITMs often look plausible, and can corrupt the language-behavior mapping learned by the policy. We propose Multimodal Probabilistic Fusion (MMPF), a training-free auditing framework that treats each modality as an expert, estimates a task-label distribution from local neighborhood agreement and global prototype similarity, and then fuses modalities with predictive-entropy weighting in a product of experts. Across LIBERO benchmarks with injected instruction mismatches and noisy real-robot data, MMPF achieves the strongest overall ITM detection and label correction accuracy. We also show that auditing improves most downstream policy learning in settings where language is needed to disambiguate the task. We demonstrate in real robot experiments that our method can achieve improved policy performance and show the trade-off of filtering demonstrations compared to relabeling.

## Metadata
- **Published**: 2026-08-08T03:43:58Z
- **Authors**: Simon Holk, Ryosuke Takanami, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo, Yueh-Hua Wu, Kei Ota
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07895v1)