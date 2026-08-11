---
title: Full-bandwidth transformer
published: 2026-08-09T19:59:45Z
authors: Xi Wang, Ziyang Cai, Zheng Zhan, Harry Dong, Ying Fan, Gustavo de Rosa, Tim Pearce, John Langford
url: http://arxiv.org/abs/2608.08888v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Full-bandwidth transformer

## Abstract
Autoregressive transformers compute along two axes: horizontally across generated tokens, and vertically through model depth. Dense attention gives each token broad horizontal access to the past, but the vertical feedback channel between decoding steps remains narrow: only the sampled token returns to the bottom of the stack, while the top-layer hidden state is discarded. We introduce the \emph{full-bandwidth transformer}, which widens this channel with \emph{latent feedback}: at each decoding step, the previous top-layer hidden state is fused with the sampled token embedding through a gated linear unit and fed back as the next input. Latent feedback lets non-verbalized computation re-enter the stack with a renewed depth budget, while preserving the standard transformer architecture, KV cache, and language-modeling objective. To train full-bandwidth transformers without losing parallel teacher forcing, we use a scheduled multi-pass objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper feedback passes for stability. We train 1B-parameter full-bandwidth transformers up to 400B tokens and find that latent feedback improves validation loss, 5-shot language-model evaluation, math and coding generation, and instruction-tuned performance. With negligible per-token decoding overhead, full-bandwidth transformers match or approach standard transformers trained with roughly $1.5\times$ more tokens, and manage to produce shorter reasoning traces at equal or better accuracy.

## Metadata
- **Published**: 2026-08-09T19:59:45Z
- **Authors**: Xi Wang, Ziyang Cai, Zheng Zhan, Harry Dong, Ying Fan, Gustavo de Rosa, Tim Pearce, John Langford
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08888v1)