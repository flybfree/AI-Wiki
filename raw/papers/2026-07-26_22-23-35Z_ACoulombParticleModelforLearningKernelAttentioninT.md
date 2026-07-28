---
title: A Coulomb Particle Model for Learning Kernel Attention in Transformers
published: 2026-07-26T22:23:35Z
authors: Masoud Badiei Khuzani, Sharath Honnaiah, Atiq Islam, Alex Cozzi, Abraham Bagherjeiran
url: http://arxiv.org/abs/2607.23869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Coulomb Particle Model for Learning Kernel Attention in Transformers

## Abstract
Randomized features provide a scalable approximation to kernel machines, but their performance depends strongly on the choice of feature distribution. We propose a particle-based method that learns this distribution by optimizing kernel-target alignment while regularizing particles with a Riesz/Coulomb repulsive potential. The resulting Hamiltonian yields diverse, task-adaptive random features and admits a mean-field description through a McKean--Vlasov equation. We instantiate the method in linearized Transformer attention by learning positive random-feature maps in a first alignment phase, then freezing the kernel and training the remaining network parameters with cross-entropy. Experiments on synthetic classification and sentence-level benchmarks show that learned kernelized attention can improve accuracy, calibration, and robustness for several feature maps while preserving linear-attention inference complexity.

## Metadata
- **Published**: 2026-07-26T22:23:35Z
- **Authors**: Masoud Badiei Khuzani, Sharath Honnaiah, Atiq Islam, Alex Cozzi, Abraham Bagherjeiran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23869v1)