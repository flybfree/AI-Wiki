---
title: DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models
published: 2026-10-27T10:11:04Z
authors: Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev, Ivan Krivorotov, Valentin Beliaev, Nikita Arsenin, Dmitry Bocharov, Aleksei Goncharov
url: http://arxiv.org/abs/2610.36950v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models

## Abstract
Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it. We present DCKV, a differentiable codec for the KV cache and the first KV-cache codec that is trained end to end. Its transform, its quantizer and its entropy models, which are conditioned on the prompt tokens and on already decoded neighbouring positions, are optimized together against the frozen language model, both for the code length that the entropy models assign and for the change of the model's output. On Qwen3.5-2B, DCKV stores a compressed token in more than 55 times fewer bytes than bf16 at a loss of at most 1.8 points on three long-context benchmarks, and in more than 100 times fewer bytes at a loss of at most 3.6 points.

## Metadata
- **Published**: 2026-10-27T10:11:04Z
- **Authors**: Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev, Ivan Krivorotov, Valentin Beliaev, Nikita Arsenin, Dmitry Bocharov, Aleksei Goncharov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36950v1)