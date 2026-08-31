---
title: Memristive-Friendly Hadamard Reservoir Computing: Structured, Multiplier-Free Recurrences at Scale
published: 2026-08-28T12:58:42Z
authors: Andrea Ceni, Gianluca Milano, Carlo Ricciardi, Claudio Gallicchio
url: http://arxiv.org/abs/2608.28295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memristive-Friendly Hadamard Reservoir Computing: Structured, Multiplier-Free Recurrences at Scale

## Abstract
Reservoir Computing (RC) designs Recurrent Neural Networks around a fixed, i.e., untrained, recurrent layer, and is a natural candidate for neuromorphic hardware. Memristive-friendly reservoirs derive the neuron dynamics from memristive-device kinetics, but still rely on dense recurrent matrices, which are expensive to realize physically. In this paper, we replace the dense matrix with a structured orthogonal operator, built from sign diagonals, a permutation, and a fast Walsh-Hadamard transform. The operator is multiplier-free, requires $O(N)$ parameters and $O(N\log N)$ operations per step, and is never materialized as a matrix. We instantiate it in a standard and in a memristive-friendly Echo State Network, with one binary input connection per unit.   Our mathematical analysis shows that exact orthogonality yields an echo state condition that is tight in the recurrent scaling, and a noise response that is predictable at design time. Moreover, the operator mixes the whole state in a single application. Experiments on twenty classification and seven regression benchmarks, at reservoir sizes up to $N = 8192$, show that the structured models match dense orthogonal reservoirs, and achieve better mean performance than the cycle reservoir by a margin that widens with size. Furthermore, we time the recurrent step on three hardware platforms, where it is up to $50\times$ faster than a dense product and $10^4\times$ smaller in memory. Finally, we ablate the operator and measure the response to noise, quantization, device mismatch and discrete faults.

## Metadata
- **Published**: 2026-08-28T12:58:42Z
- **Authors**: Andrea Ceni, Gianluca Milano, Carlo Ricciardi, Claudio Gallicchio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28295v1)