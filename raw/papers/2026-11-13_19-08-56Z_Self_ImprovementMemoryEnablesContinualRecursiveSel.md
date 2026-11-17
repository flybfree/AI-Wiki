---
title: Self-Improvement Memory Enables Continual Recursive Self-Improvement
published: 2026-11-13T19:08:56Z
authors: Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu
url: http://arxiv.org/abs/2611.18856v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Improvement Memory Enables Continual Recursive Self-Improvement

## Abstract
Harness optimization is often studied with a fixed policy model and benchmark. When either changes, the optimizer must decide which parts of an evolved harness to reuse or revise, but the harness alone may not explain why earlier edits were made or how they performed. In this work, we study Continual Recursive Self-Improvement (CRSI), a setting for continuing existing harness-optimization methods across compatible benchmarks or policy models. We propose Self-Improvement Memory (SIM) for the harness optimizer, rather than the task-solving policy. SIM groups edits by recurring harness problem and records their rationale, predicted and observed outcomes, and evaluation context. New attempts extend this history as optimization continues. In our experiments across four domains, SIM achieves higher final scores than harness-only and root-cause-only continuation in cross-dataset and pairwise cross-model comparisons. Across ten independent source runs in coding, paired continuations with SIM improve final scores by an average of 2.36 points over harness-only continuation ($p=0.003$).

## Metadata
- **Published**: 2026-11-13T19:08:56Z
- **Authors**: Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.18856v1)