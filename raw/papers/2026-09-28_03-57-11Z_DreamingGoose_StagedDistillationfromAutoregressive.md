---
title: DreamingGoose: Staged Distillation from Autoregressive Transformers to Bidirectional Recurrent Diffusion Language Models
published: 2026-09-28T03:57:11Z
authors: Julian Boesch, Andrew Wee, Alexander Stranzl
url: http://arxiv.org/abs/2609.34253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DreamingGoose: Staged Distillation from Autoregressive Transformers to Bidirectional Recurrent Diffusion Language Models

## Abstract
Pretrained autoregressive Transformers represent a large sunk investment in compute. Existing conversion methods reuse that investment by changing either the architecture (attention to recurrence) or the objective (next-token prediction to denoising), never both. We convert Qwen3 teachers at 1.7B and 8B into attention-free, bidirectional, gated-delta-rule diffusion students in three stages, so that each capability can be traced to the stage that kept or lost it. Language modeling transfers only partially and in-distribution; in-context retrieval does not transfer. On a multi-query recall probe where the teachers score 0.34-0.58, both converted students score 0.000, and diffusion pretraining alone does not restore retrieval. A retrieval curriculum in the final stage, which gradually lengthens the gap between a key-value table and the queries that address it, restores it only stochastically: on a fixed schedule, one seed in three learns to retrieve. Advancing the gap only while a running accuracy estimate stays above a threshold works for all three of those seeds, holds on real text, and carries unchanged to 8B, where two of three seeds succeed. The third had not learned within its fixed 16k-step budget: retrieval switches on abruptly at a seed-dependent step (6.5k and 11k in the other two), so a fixed budget can cut a late run off. One boundary survives every intervention: every model that learns retrieval scores 0.000 on tokens that never appeared in a retrieval episode, and an arm that resamples the key and value tokens every batch shows this is a coverage limit, not memorization of particular bindings. Separately, we convert a 7B code model into a 3:1 recurrent-attention block-diffusion hybrid over 85k steps and report two negative training results.

## Metadata
- **Published**: 2026-09-28T03:57:11Z
- **Authors**: Julian Boesch, Andrew Wee, Alexander Stranzl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34253v1)