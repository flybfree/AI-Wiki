---
title: Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization
published: 2026-07-19T01:13:09Z
authors: Libo Sun, Po-Wei Harn, Zewei Zhang, Peixiong He, Xiao Qin
url: http://arxiv.org/abs/2607.17019v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization

## Abstract
We study whether \sigreg -- LeJEPA's anti-collapse objective -- can reshape representations during standard autoregressive language-model pretraining, and when the resulting geometry helps \kv-cache quantization. We train 110M-parameter models on 10B FineWeb tokens and report three findings. \textbf{(1)} At $λ{=}0.01$, \sigreg reduces hidden-state pairwise-cosine anisotropy by $38\%$ across three paired seeds. Perplexity increases by less than $0.35\%$ in every pair, with no consistent zero-shot loss. \textbf{(2)} This change does not propagate from hidden states to the \kv cache. Applying \sigreg directly to K and V during continued training, however, reduces mean cache anisotropy by $94\%$ across four checkpoints. A matched continuation without the \kv term leaves cache geometry nearly unchanged, and the frozen-trunk retrofits we tested do not reproduce the effect. \textbf{(3)} Under untransformed symmetric group-free quantization, direct \kv regularization is the only training condition that prefers per-channel scaling in all three seeds, and under that same 3-bit per-channel scheme the baseline incurs $4.3$--$7.9\times$ the directly regularized model's \dnll. Under the full simulated KIVI-style configuration (mixed arrangement, zero-points, grouped scales), however, all models reach near-parity, including when storage overhead is approximately matched. In this 110M regime, the training intervention helps when quantizer scales are coarse; the advantage vanishes under the tested combination of token-local grouping, mixed \kv scaling, and zero-points. To our knowledge this is the first training-time \emph{distributional} regularization of standard \kv-cache geometry evaluated against post-hoc cache quantization.

## Metadata
- **Published**: 2026-07-19T01:13:09Z
- **Authors**: Libo Sun, Po-Wei Harn, Zewei Zhang, Peixiong He, Xiao Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17019v1)