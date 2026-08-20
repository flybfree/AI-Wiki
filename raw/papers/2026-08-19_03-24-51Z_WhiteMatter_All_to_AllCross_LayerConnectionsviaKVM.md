---
title: WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing
published: 2026-08-19T03:24:51Z
authors: Wenbo Zhang, Xiang Ren
url: http://arxiv.org/abs/2608.18486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing

## Abstract
In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during autoregressive decoding. Feedback architectures allow shallow consumer layers to attend to KV produced by deeper past-token representations, but give all consumer layers the same fixed connection patterns to source layers. We propose WhiteMatter, which connects every attention layer to the representations from all layers of each past token, with connection weights that can vary across consumer layers and adapt to the source token. For each token, a router implements these connections by mixing its $L$ layer states into $k$ KV channels that are cached for subsequent tokens; each consumer layer attends to one of the channels. The number of channels $k$ controls the KV-cache size. Setting $k<L$ reduces the cache's memory footprint. In our pretraining experiments, WhiteMatter outperforms a vanilla Transformer with 50% more layers and retains most of this gain with a 50% KV-cache compression.

## Metadata
- **Published**: 2026-08-19T03:24:51Z
- **Authors**: Wenbo Zhang, Xiang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18486v1)