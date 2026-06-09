---
title: Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find
published: 2026-05-15T17:43:16Z
authors: Gabriel Garcia
url: http://arxiv.org/abs/2605.16234v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find

## Abstract
When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests. Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped. Both are output-grounded swap-KL probes, but they need not agree: on pretrained transformers the protocol gap can change which layers look safe to prune by several-fold under the same evaluator, especially when replacement distances are high.   We measure both protocols across checkpoints and architectures. On a Pythia training trajectory (410M and 1.4B), the replacement-interchange gap grows from initialization to convergence. Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal. Before layer removal or merging, score both swap-KLs on the target checkpoint; the diagnostic requires only unlabeled forward passes.

## Metadata
- **Published**: 2026-05-15T17:43:16Z
- **Authors**: Gabriel Garcia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.16234v1)