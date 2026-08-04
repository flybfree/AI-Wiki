---
title: Constrained Co-Design for Photonic Bayesian Neural Networks
published: 2026-08-03T13:47:48Z
authors: Hendrik Borras, Xiao Wang, Bernhard Klein, Robin Janssen, Frank Brückerhoff-Plückelmann, Wolfram Pernice, Holger Fröning
url: http://arxiv.org/abs/2608.02229v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constrained Co-Design for Photonic Bayesian Neural Networks

## Abstract
Classical neural networks frequently produce overconfident predictions on ambiguous or out-of-distribution (OOD) data, a liability that grows with each AI system deployed in safety-critical real-world scenarios. Bayesian neural networks (BNNs) provide a principled framework for uncertainty-aware prediction by replacing deterministic parameters with probability distributions, but repeated sampling increases latency, memory traffic, and energy consumption. Photonic probabilistic computing offers a promising alternative by exploiting intrinsic optical stochasticity for fast and parallel sampling. However, photonic BNNs are not ideal samplers: analog constraints on quantization, programming error, dynamic range, and representable mean and variance restrict the variational families that can be implemented in hardware. In this work, we study which hardware-imposed constraints limit scalable photonic BNN inference, how these constraints can be represented, and which ranges can be tolerated by photonic BNNs beyond small proof-of-concept networks. We formulate photonic BNN inference as constrained stochastic variational inference and perform a systematic ablation study over stochasticity location, stochasticity modality, quantization, programming error, and mean/variance bounds. From these results, we derive concrete co-design guidelines that distinguish hardware constraints that can be compensated by training from those requiring hardware or architecture intervention. We validate these guidelines under coupled, hardware-realistic constraints on Dirty-MNIST, CIFAR-10, and CINIC-10, using Fashion-MNIST and SVHN as OOD benchmarks, showing that hardware-aware training recovers predictive performance and uncertainty quality whenever the required variational family remains representable, whereas violations of representational limits require targeted hardware modifications.

## Metadata
- **Published**: 2026-08-03T13:47:48Z
- **Authors**: Hendrik Borras, Xiao Wang, Bernhard Klein, Robin Janssen, Frank Brückerhoff-Plückelmann, Wolfram Pernice, Holger Fröning
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02229v1)