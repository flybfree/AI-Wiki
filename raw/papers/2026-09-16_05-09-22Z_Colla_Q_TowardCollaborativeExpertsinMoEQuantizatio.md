---
title: Colla-Q: Toward Collaborative Experts in MoE Quantization via Minimax Precision Balancing
published: 2026-09-16T05:09:22Z
authors: Eunju Shin, Jongbin Ryu
url: http://arxiv.org/abs/2609.18131v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Colla-Q: Toward Collaborative Experts in MoE Quantization via Minimax Precision Balancing

## Abstract
In this paper, we present a Mixture-of-Experts (MoE) quantization method based on activation entropy. Although quantization reduces memory and computational costs, it can substantially degrade performance. In particular, performance decline is pronounced in quantized MoE models, where individual experts have a small number of parameters that are sensitive to low-bit representation. Considering that MoE operates as an ensemble model with collaborative contributions from routed experts, a significant performance decline of a particular expert due to quantization can harm model performance. Therefore, we propose Colla-Q, a bit-allocation framework to maintain balanced performance across experts through an activation-entropy-based bit-width allocation algorithm. This approach encourages each expert to operate collaboratively in the quantized model, thereby 1) improving the overall MoE performance and 2) reducing the dependence on the calibration dataset. Since uniformly adjusting each expert's performance facilitates robustness and stability of the MoE model, the proposed MoE quantization method can generalize more consistently across different calibration datasets. Our code is available at: https://github.com/mmai-laboratory/Colla_Q

## Metadata
- **Published**: 2026-09-16T05:09:22Z
- **Authors**: Eunju Shin, Jongbin Ryu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18131v1)