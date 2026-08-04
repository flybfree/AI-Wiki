---
title: QWRF-Net: A Quantum-Wavelet Framework with Rectified Flow for Short-Term Precipitation Nowcasting
published: 2026-08-03T02:58:49Z
authors: Zhuo Wang, Chaorong Li, Wenjie Luo, Chuanhu Deng
url: http://arxiv.org/abs/2608.01626v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QWRF-Net: A Quantum-Wavelet Framework with Rectified Flow for Short-Term Precipitation Nowcasting

## Abstract
Short-term precipitation nowcasting is important for hydrometeorological early warning, especially when intense convective rainfall may trigger urban flooding, flash floods, and other high-impact hazards. A key challenge in warning-oriented nowcasting is that radar precipitation fields contain strongly coupled multi-scale structures, while forecast quality often degrades at later lead times, making it difficult to preserve intense precipitation cores and their spatial organization over the full warning-relevant horizon. To address this problem, we propose QWRF-Net, a quantum-wavelet framework with rectified flow for short-term precipitation nowcasting. The core idea is to improve the conditional representation of precipitation by explicitly decomposing latent features into wavelet sub-bands and then performing differentiated quantum-inspired modulation in the decomposed latent space, before generating future sequences through a rectified-flow-based non-autoregressive decoder. Experiments on the KNMI radar and SEVIR benchmarks under a unified evaluation protocol show that QWRF-Net achieves favorable overall performance, with relatively consistent gains at medium-to-high precipitation thresholds, on an extreme-event subset, and in preserving intense precipitation cores and fine-scale structures. Ablation results further indicate that wavelet-based scale disentanglement, differentiated sub-band modulation, and flow-based generation provide complementary benefits within the proposed framework. Overall, these results suggest that jointly enhancing multi-scale precipitation representation and stable multi-step generation is a promising direction for warning-oriented short-term precipitation nowcasting. The observed improvements may also provide a more useful precipitation basis for downstream hydrological and warning-related applications.

## Metadata
- **Published**: 2026-08-03T02:58:49Z
- **Authors**: Zhuo Wang, Chaorong Li, Wenjie Luo, Chuanhu Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01626v1)