---
title: HeAD-CP: Heterophily-Aware Diffused Conformal Prediction Sets for Graph Neural Networks
published: 2026-07-28T04:20:34Z
authors: Phan Binh Nguyen Lam, Nguyen Thai Anh
url: http://arxiv.org/abs/2607.25273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HeAD-CP: Heterophily-Aware Diffused Conformal Prediction Sets for Graph Neural Networks

## Abstract
Conformal prediction (CP) provides distribution-free uncertainty quantification, and its extension to graphs is an active research direction. Diffused Adaptive Prediction Sets (DAPS) is a widely used graph-aware diffusion baseline, propagating Adaptive Prediction Sets (APS) non-conformity scores along edges with a uniform coefficient $λ$. We identify a fundamental shortcoming of this design: the uniform low-pass diffusion presupposes graph homophily and proves detrimental on heterophilic graphs, enlarging the mean prediction-set size by up to 10.6% relative to plain APS. To mitigate this, we propose HeAD-CP, a family of node-wise diffusion variants whose coefficients are determined by a label-free local-homophily estimate derived from the GNN softmax. Three variants, namely signed-$γ$, edge-compatibility, and a DAPS-baseline-with-correction, are most effective at extreme heterophily, intermediate heterophily, and moderate-to-high homophily, respectively, and all preserve the marginal coverage guarantee. On ten benchmarks, the HeAD-CP family stays at or below plain APS on every dataset, while DAPS exceeds APS on six. The post-hoc oracle over the family improves over DAPS on 8/10 datasets at $p<0.01$ (paired Wilcoxon), with the largest gains on heterophilic graphs (10.3% on Texas); on the two homophilic datasets where DAPS still wins (CiteSeer, PubMed), it retains a marginal advantage of at most 0.002, statistically insignificant on CiteSeer ($p=0.23$). Designing a calibrated label-free selector that approaches this oracle is the main outstanding empirical question.

## Metadata
- **Published**: 2026-07-28T04:20:34Z
- **Authors**: Phan Binh Nguyen Lam, Nguyen Thai Anh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25273v1)