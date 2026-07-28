---
title: Cheap Probes Predict Expensive Training in 3D-CT Vision--Language Models
published: 2026-07-24T04:28:33Z
authors: Renjie Liang
url: http://arxiv.org/abs/2607.22771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cheap Probes Predict Expensive Training in 3D-CT Vision--Language Models

## Abstract
Picking the frozen image encoder for a 3D~CT vision--language model (VLM), together with the token-compression scheme on top of it, is a search over many candidates. There are several encoders, several ways to compress their tokens, and several token budgets, and the combinations grow fast. Comparing them the usual way means fine-tuning a large language model (LLM) on each combination, and running the whole sweep this way needs far more compute than most groups can spend. We ask whether a cheap probe on the encoder's cached embeddings can stand in for that comparison. We build an image-grounded probing benchmark over (encoder $\times$ compression) cells, with clinical attribute families and two validation gates, scale-sanity and probe-separability, that keep each attribute well-scaled and decodable. These gates are the main methodological contribution. On this benchmark we compare a range of read-out heads, and in a preliminary study we pair each probe with its matched downstream task. The early signal is encouraging: the cheap probe orders the candidates in close agreement with expensive fine-tuning, at about $r\approx0.95$ on the cells measured so far. We read this as an ordinal claim, a ranking predictor rather than an exact estimate, and we are explicit about where it stays preliminary. If it holds up, encoder and compression choices can be screened in minutes with frozen-token probes, with full training spent only on the finalists.

## Metadata
- **Published**: 2026-07-24T04:28:33Z
- **Authors**: Renjie Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22771v1)