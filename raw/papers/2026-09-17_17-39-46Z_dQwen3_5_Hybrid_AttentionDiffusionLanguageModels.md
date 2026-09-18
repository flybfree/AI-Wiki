---
title: dQwen3.5: Hybrid-Attention Diffusion Language Models
published: 2026-09-17T17:39:46Z
authors: Anton Xue, Litu Rout, Aditya Akella, Adam Klivans, Sujay Sanghavi, Sanjay Shakkottai
url: http://arxiv.org/abs/2609.20751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# dQwen3.5: Hybrid-Attention Diffusion Language Models

## Abstract
Adapting a pretrained autoregressive (AR) model is a cost-efficient route to a diffusion language model (DLM). While nearly all such adaptations start from a full-attention transformer, AR modeling has shifted toward hybrid architectures that interleave attention and RNN layers. This creates an obstacle for adaptation: unlike attention, RNNs are structurally causal and nontrivial to bidirectionalize. Despite this mismatch, we investigate whether such backbones can become effective DLMs by adapting Qwen3.5 at 0.8B, 2B, 4B, and 9B scales, yielding the dQwen3.5 family. We find that hybrid backbones can be efficient starting points for adaptation: against a full-attention control, the hybrid reaches a given training loss in about half the tokens. Across scales, dQwen3.5 resembles full-attention DLMs in any-order decoding behavior and performs strongly under parallel decoding.

## Metadata
- **Published**: 2026-09-17T17:39:46Z
- **Authors**: Anton Xue, Litu Rout, Aditya Akella, Adam Klivans, Sujay Sanghavi, Sanjay Shakkottai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.20751v1)