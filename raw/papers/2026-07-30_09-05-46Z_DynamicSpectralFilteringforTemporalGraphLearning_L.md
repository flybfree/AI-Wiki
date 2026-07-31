---
title: Dynamic Spectral Filtering for Temporal Graph Learning: Learning Evolving Propagation Operators
published: 2026-07-30T09:05:46Z
authors: Yan Kong
url: http://arxiv.org/abs/2607.27891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Spectral Filtering for Temporal Graph Learning: Learning Evolving Propagation Operators

## Abstract
Temporal graph learning is commonly organized around the evolution of node states or the encoding of interaction histories. We study an underexplored, operator-centric question: should the graph propagation mechanism itself evolve over time? We introduce Dynamic Spectral Filtering (DSF), which represents propagation at snapshot t by a Chebyshev polynomial filter with vector-valued, time-dependent coefficients. DSF explicitly treats these compact multi-order coefficients as recurrent temporal states. A recurrent branch proposes updates, while multiplicative global and order-specific gates regulate their magnitude. The temporal state is independent of the number of nodes. On MOOC, Wikipedia, and Reddit temporal link-prediction benchmarks, converged DSF runs attain AP scores of 0.7851, 0.9088, and 0.9860, respectively, with 93K to 133K trainable parameters, 68 to 182 MB peak GPU memory, and 1.6 to 2.1 seconds of training per epoch. Against the closely related DEFT baseline, DSF is better on MOOC, within 0.001 AP on Reddit, and modestly lower on Wikipedia, while using 8.3 to 8.6 times fewer parameters, 25 to 33 times less GPU memory, and 5 to 19 times less time per epoch. Relative to all measured alternatives, it uses 3.3 to 38.6 times less GPU memory. These results support direct spectral-response evolution as a useful temporal inductive bias when computational efficiency is a first-class requirement.

## Metadata
- **Published**: 2026-07-30T09:05:46Z
- **Authors**: Yan Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27891v1)