---
title: The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy
published: 2026-07-29T09:09:13Z
authors: Zeyu Wang
url: http://arxiv.org/abs/2607.26648v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy

## Abstract
Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates. We argue the energy dividend of sparsity is not a property of SNNs but of the task. Holding architecture fixed and swapping only the hidden unit (continuous vs. leaky-integrate-and-fire), plus a two-sided target-firing-rate probe, we measure how far activity can be pushed down before quality breaks. Low-load feed-forward perception sparsifies to 5% firing at no accuracy cost; a recurrent language model cannot go below ~50% -- the recurrent state must stay active to carry information. A spiking Transformer, by contrast, sparsifies freely to 2% (3 seeds) -- so the ceiling is a property of recurrent compression, not sequence modeling. Attention escapes the floor only by storing the full key-value cache, trading a firing floor for a memory wall: on neuromorphic hardware, recurrence and attention pay on different axes, neither escapes. We formalize the ceiling with an information-theoretic bound rho >= H_b^{-1}(log2 M / H) and confirm its predictions: the floor rises with memory load, falls with state width, and (refuting a naive memory-only reading) rises with task difficulty. A layer-wise input floor further caps op reduction under dense input, isolating event-driven perception as where neuromorphic hardware wins.

## Metadata
- **Published**: 2026-07-29T09:09:13Z
- **Authors**: Zeyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26648v1)