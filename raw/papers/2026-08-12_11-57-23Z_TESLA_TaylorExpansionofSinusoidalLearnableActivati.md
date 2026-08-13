---
title: TESLA: Taylor Expansion of Sinusoidal Learnable Activations
published: 2026-08-12T11:57:23Z
authors: Daehwa Ko, Jaehyeon Kim, Seunghyun Ham, Jay Hoon Jung
url: http://arxiv.org/abs/2608.11970v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TESLA: Taylor Expansion of Sinusoidal Learnable Activations

## Abstract
The parity problem--deciding whether the number of ones in a binary vector is odd or even--remains challenging for standard neural networks due to linear inseparability and the need for global interactions. We propose TESLA, an activation defined as a learnable combination of sine and cosine terms, enabling explicit control over polynomial degree and selective amplification of high-order components. Theoretically, we show that constraining TESLA's coefficients yields Lipschitz/Rademacher complexity bounds and shapes the training dynamics to emphasize higher-frequency structure. Empirically, on parity with input length n = 32, TESLA attains strong generalization with 100K training samples (approximately 0.002% of the 2^32 input space) and remains robust under heavy corruption, retaining high accuracy with up to 30% label noise. We also compare against periodic and frequency-based baselines (SIREN, SNAKE, and Fourier feature embeddings) on parity and Forrelation. Beyond synthetic structure, TESLA delivers comparable performance on ImageNet-100, indicating that activation-level degree control transfers to more general vision workloads. Code: https://github.com/KAU-QuantumAILab/TESLA

## Metadata
- **Published**: 2026-08-12T11:57:23Z
- **Authors**: Daehwa Ko, Jaehyeon Kim, Seunghyun Ham, Jay Hoon Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11970v1)