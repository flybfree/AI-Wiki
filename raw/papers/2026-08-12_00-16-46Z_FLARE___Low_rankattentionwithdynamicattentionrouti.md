---
title: FLARE++: Low-rank attention with dynamic attention routing
published: 2026-08-12T00:16:46Z
authors: Vedant Puri, Yongjie Jessica Zhang, Levent Burak Kara
url: http://arxiv.org/abs/2608.11519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLARE++: Low-rank attention with dynamic attention routing

## Abstract
Full self-attention is a strong token mixer for PDE surrogates on irregular domains, but its quadratic cost limits its use on high-resolution problems. Efficient latent-attention models such as the Fast Low-rank Attention Routing Engine (FLARE) avoid that cost by routing all N tokens through M << N learned latent queries, but those queries are parameters: once trained, the same learned query templates serve every input. We remove this restriction with FLARE++, a low-rank attention architecture with dynamic token routing. FLARE++ reuses FLARE's own encoder to build its routing queries: learned latent seeds drive one extra encode call that gathers the N input tokens into M input-conditioned queries, and those queries then determine how the same tokens are compressed and redistributed. This preserves FLARE's explicit low-rank factorization and linear O(NM) complexity, and expresses the complete routing operation with standard scaled dot-product attention (SDPA) calls alone. We also provide a multi-GPU context-parallel implementation that shards input tokens across devices without ever gathering the full token sequence on one of them. FLARE++ is competitive across a set of standard PDE surrogate benchmarks, improving on fixed-query FLARE by 24% on average, and it gains 2.3 points of average accuracy on Long Range Arena.

## Metadata
- **Published**: 2026-08-12T00:16:46Z
- **Authors**: Vedant Puri, Yongjie Jessica Zhang, Levent Burak Kara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11519v1)