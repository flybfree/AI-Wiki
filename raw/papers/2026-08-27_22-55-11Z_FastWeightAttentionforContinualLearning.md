---
title: Fast Weight Attention for Continual Learning
published: 2026-08-27T22:55:11Z
authors: Yifan Zhang, Steve Ta, Jasper Zhang, Jichen Feng, Shuzhen Li, Yongxin Zhang, Yifeng Liu, Huizhuo Yuan, Mengdi Wang, Quanquan Gu, Andrew Chi-Chih Yao
url: http://arxiv.org/abs/2608.27763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast Weight Attention for Continual Learning

## Abstract
Recurrent fast-weight memories and selective state-space models compress an expanding context into a fixed-size recurrent state, making the state transition an online learning rule. We study this rule under read-after-write autoregressive semantics. For the prefix-prediction objective considered here, the local fast-memory example revealed at step $t$ is the prefix-aligned pair $(\mathbf{x}_t,\mathbf{y}_t)=(φ(\mathbf{k}_{t-1}),\mathbf{v}_t)$. The common same-step association $(φ(\mathbf{k}_t),\mathbf{v}_t)$ remains causal, but optimizes a different internal objective. We derive normalized first-order updates for squared-error regression and negative inner-product objectives. The regression family comprises Falcon-1 (a scalar NLMS update), Falcon-2 (its per-column extension), and Falcon-3 (a sliding-window mini-batch update); Falcon-1A/Falcon-2A/Falcon-3A are the corresponding inner-product variants. We provide recurrent, masked-parallel, and chunk-parallel forms, together with numerically stable positive-decay renormalization. Representative variants remain competitive in language modeling and improve length extrapolation on variable-digit addition. This framework separates temporal alignment, plasticity, forgetting, and bounded rehearsal in recurrent sequence models.

## Metadata
- **Published**: 2026-08-27T22:55:11Z
- **Authors**: Yifan Zhang, Steve Ta, Jasper Zhang, Jichen Feng, Shuzhen Li, Yongxin Zhang, Yifeng Liu, Huizhuo Yuan, Mengdi Wang, Quanquan Gu, Andrew Chi-Chih Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27763v1)