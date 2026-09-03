---
title: Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?
published: 2026-09-01T22:47:16Z
authors: Wenlong Wang, Fergal Reid
url: http://arxiv.org/abs/2609.01924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?

## Abstract
Recent work identifies a mid-depth band of verbalisable, causally potent representations in a standard feedforward transformer --- a functional analogue of a global workspace. Whether the same workspace functionality emerges when depth is implemented through recurrence rather than a stack of distinct layers remains unknown. Looped and depth-recurrent transformers provide a direct test of this question because they reuse the same weights across depth. We extend the Jacobian lens to iterated architectures using a virtual-unrolling adapter. We apply the full workspace suite --- lens fitting, readout, and eleven causal experiment families --- to Ouro-2.6B (48 layers looped 4 times, deeply supervised) and Huginn-0125 (a 4-layer core recurred 16 times, trained for latent reasoning), using Qwen3.6-27B (64 untied layers) as the standard baseline. We find that a workspace forms in the iterated part of each architecture, but that recurrence changes how it can be accessed. Ouro reconstructs workspace content in every loop, and linear transport cannot carry that content across loop boundaries; writes and ablations must therefore span every remaining loop. Huginn carries content forward across all sixteen recurrences, while reads, writes, and ablations act only within a sliding window of roughly two recurrences. Whether newly injected content can be verbalised tracks explicit per-iteration supervision; whether existing content can be steered does not.

## Metadata
- **Published**: 2026-09-01T22:47:16Z
- **Authors**: Wenlong Wang, Fergal Reid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01924v1)