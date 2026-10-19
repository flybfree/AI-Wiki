---
title: Ori: Drift-Aware Streaming $k$-PCA for Very Low-Rank LLM Training
published: 2026-10-16T01:13:12Z
authors: Xinyu Luo, Jincheng Zhou, Mengbo Wang, Zilin Shen, Nadia Atallah Lanman, Petros Drineas, Bruno Ribeiro, Brian Bullins
url: http://arxiv.org/abs/2610.22794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ori: Drift-Aware Streaming $k$-PCA for Very Low-Rank LLM Training

## Abstract
A prominent family of low-rank LLM optimizers, pioneered by GaLore, performs gradient-subspace projection: at each step, they project the gradient into a low-dimensional subspace and map the update back to the full model. Most existing work either recomputes the gradient subspace at certain intervals, or performs post-hoc adaptation to catch up to the moving subspace. In this work, we explicitly identify in practice the slow, stable manner in which LLM gradient subspaces drift across time. To this end, we propose Ori, a novel low-rank optimizer for training LLMs that captures the shifting principal gradient directions over time to achieve state-of-the-art accuracy under stringent low-rank constraints. Ori employs a streaming $k$-PCA algorithm inspired by Oja++, whose low per-step cost enables high-frequency, on-the-fly subspace tracking. In practice, Ori reduces the performance gap of the state-of-the-art low-rank optimizers to full-rank optimizers by up to 69.3\% on a 1B LLaMA pretraining task, and achieves the best performance on 10 out of 16 task scenarios in Roberta-Base fine-tuning. Together, these contributions allow Ori to further push the performance and efficiency frontiers of gradient-projecting optimizers, narrowing the gap to full-rank training for LLMs. Code can be found at https://anonymous.4open.science/r/Ori-Submission-2132.

## Metadata
- **Published**: 2026-10-16T01:13:12Z
- **Authors**: Xinyu Luo, Jincheng Zhou, Mengbo Wang, Zilin Shen, Nadia Atallah Lanman, Petros Drineas, Bruno Ribeiro, Brian Bullins
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22794v1)