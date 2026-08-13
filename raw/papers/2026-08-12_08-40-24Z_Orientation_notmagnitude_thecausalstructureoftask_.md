---
title: Orientation, not magnitude: the causal structure of task-vector interference in merged language models
published: 2026-08-12T08:40:24Z
authors: Chencheng Zhu
url: http://arxiv.org/abs/2608.11797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Orientation, not magnitude: the causal structure of task-vector interference in merged language models

## Abstract
Model merging by task arithmetic works until it doesn't, and the field diagnoses why with magnitudes: layerwise representation bias, deviations from cross-task linearity, parameter overlap. Tracking the exact layerwise cross-term of merged LLMs through a factorial ledger and intervening on it directly, we find magnitude insufficient - and inconsistent across model families - as a diagnostic axis. An exact decomposition of the layerwise flux shows it is dominated by amplifying transport of the existing cross-term (~65-70% in both families, gain >1 per late block), and erasing the term is undone by propagation - rebuilt to 99% of its norm at cosine 0.99 - unless applied near the output; a basin test with six starting displacements establishes the carried direction as an attractor of the forward pass. That direction is causally load-bearing: erasure along it removes expressed interference dose-dependently and saturates at exact erasure, while norm-matched wrong-direction controls fail or backfire. Instruction wrappers gate the effect: the same erasure finds 13x less relative interference to remove under a wrapper that internally amplifies the cross-term, because the wrapper drowns the interaction in a template-pinned main effect rather than shrinking it - a structure that replicates across further instruction templates but not under a length-matched control. Magnitude, by contrast, is at best a coarse correlate, and the striking +-15% "universality" of naive bfloat16 generation turns out to be quantization roughness. Task pairs whose local cross-term generation differs by at most 1.9x differ by 14x-337x in causally removable interference. All 46 predictions were preregistered and frozen before their data; falsifications, including of our own headline expectations and of behavioral recovery under a validated continuous endpoint, are reported as such.

## Metadata
- **Published**: 2026-08-12T08:40:24Z
- **Authors**: Chencheng Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11797v1)