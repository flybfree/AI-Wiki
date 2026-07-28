---
title: Practical advantage beyond the quadratic speedup limit with fully-quantum walks
published: 2026-07-24T18:00:06Z
authors: Massimiliano Incudini, Guglielmo Mazzola
url: http://arxiv.org/abs/2607.22818v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Practical advantage beyond the quadratic speedup limit with fully-quantum walks

## Abstract
We introduce a new class of fully-quantum Metropolis walks in which both the proposal and acceptance steps are intrinsically quantum. Unlike standard quantum walks obtained by quantizing classically efficient Markov chains, our algorithm employs Hamiltonian simulation as a quantum-native proposal mechanism, enlarging the class of quantum walks beyond classical counterparts. We target the problem of sampling from the low-temperature Gibbs distribution of classical dense Ising models, within a fixed error in total variation distance. This approach achieves about a cubic polynomial asymptotic advantage over previous quantum-walks, resulting in a total sixth-degree polynomial queries speedup compared to the best classical walk. This shows that speedups beyond the widely assumed quadratic limit are possible within the quantum walk formalism. We perform a complete fault-tolerant compilation of all algorithmic primitives and benchmark against CPU, GPU, and FPGA implementations of the best classical Markov chain. Under identical hardware assumptions, the resulting advantage runtime crossover is reduced from approximately $10^3$ years for conventional quantum walks to less than one day. These results identify fully-quantum Markov chains as a promising route toward practical quantum advantage.

## Metadata
- **Published**: 2026-07-24T18:00:06Z
- **Authors**: Massimiliano Incudini, Guglielmo Mazzola
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22818v1)