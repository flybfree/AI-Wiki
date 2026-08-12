---
title: Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?
published: 2026-08-11T12:41:49Z
authors: Nigel Bastian Cendra, Abdelhamid Ezzerg, Fernando Julio Cendra, Jeremias Knoblauch, Jakob Zeitler
url: http://arxiv.org/abs/2608.10867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?

## Abstract
Gradient-free post-training has emerged as a compelling alternative to gradient-based optimization for large language models (LLMs), but existing approaches remain costly. We ask whether structured search can identify a strong single expert under a modest evaluation budget. Motivated by evidence that useful weight updates lie in low-dimensional subspaces, we apply Bayesian optimization within a random linear embedding of weight space. Our method requires no backpropagation and uses a Gaussian process surrogate to guide candidate evaluations efficiently. Across several reasoning benchmarks with Qwen2.5-Instruct models from 0.5B to 3B parameters, Bayesian optimization using five times less candidate evaluations matches or exceeds RandOpt. These results show that surrogate-guided search can substantially reduce the evaluation cost of gradient-free post-training while producing stronger deployable single experts.

## Metadata
- **Published**: 2026-08-11T12:41:49Z
- **Authors**: Nigel Bastian Cendra, Abdelhamid Ezzerg, Fernando Julio Cendra, Jeremias Knoblauch, Jakob Zeitler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10867v1)