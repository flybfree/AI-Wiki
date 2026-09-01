---
title: Manacá-1B: An Open, Reproducible Brazilian-Portuguese Language Model and a Tokenizer-Aware, Paired Evaluation
published: 2026-08-31T01:00:14Z
authors: Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio Andre Machado Porto
url: http://arxiv.org/abs/2608.30114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Manacá-1B: An Open, Reproducible Brazilian-Portuguese Language Model and a Tokenizer-Aware, Paired Evaluation

## Abstract
Brazilian Portuguese remains under-served by open language models, and the few that exist are difficult to reproduce and are often compared without measures of uncertainty. We release Manacá-1B, an open decoder-only model of 1.72 billion parameters trained from scratch for Brazilian Portuguese with a fully containerized, reproducible pipeline. The pretraining is stable, with zero skipped or NaN steps and self-recovering loss spikes, and we release its full log and dynamics. We evaluate the model against nine open baselines on four Portuguese benchmarks under a single harness. Every comparison reports a standard error and a paired significance test, and the harness is validated against previously published numbers. On last-word prediction Manacá-1B is the strongest model below the 7B scale, exceeding both Tucano-1b1 and Tucano-2b4 on LAMBADA-PT with large paired margins; it is competitive on commonsense completion and near chance on multiple-choice reasoning, as are all small base models. Along the way we document a concrete evaluation pitfall: converting a SentencePiece tokenizer with case-folding normalization to the HuggingFace fast format silently drops the normalizer, routing every capitalized token to byte-fallback and depressing scores in a way that is invisible in aggregate metrics. The uncorrected tokenizer lowered LAMBADA-PT accuracy from 45.3 to 25.0; we quantify the effect and provide a one-line fix that reproduces the training tokenizer exactly. Code, raw training and evaluation logs, per-example prediction vectors, the model weights, and the corrected tokenizer are released so that every number in this paper can be recomputed.

## Metadata
- **Published**: 2026-08-31T01:00:14Z
- **Authors**: Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio Andre Machado Porto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30114v1)