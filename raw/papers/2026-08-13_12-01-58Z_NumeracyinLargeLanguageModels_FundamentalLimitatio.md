---
title: Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement
published: 2026-08-13T12:01:58Z
authors: Aoxin Ni
url: http://arxiv.org/abs/2608.13129v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement

## Abstract
Large language models (LLMs) achieve strong results on mathematical reasoning benchmarks yet remain unreliable on elementary numerical tasks, including magnitude comparison, large-integer arithmetic, fractions, and scientific notation. This survey examines basic numerical understanding as a capability distinct from high-level mathematical reasoning. We propose the Numerical Grounding Framework (NGF), which decomposes numeracy into Representational Grounding (RG), mapping numeral forms to value, magnitude, and equivalent representations, and Procedural Grounding (PG), executing arithmetic operations in accordance with their mathematical definitions. Using NGF, we organize recent diagnostic benchmarks, failure modes, structural explanations, and mitigation strategies. We review evidence concerning tokenization, positional encoding, embedding geometry, and pretraining-data distribution. We also apply NGF in a coordinated evaluation of three frontier model families across Number Cookbook, NumericBench, and GSM-Symbolic, comparing atomic, contextual, and reasoning-assisted numeracy. Architectural interventions such as digit-aware tokenization and Abacus Embeddings can improve models trained from scratch but are generally unavailable to users of pretrained systems, for whom supervised fine-tuning, reasoning scaffolds, and external tools are more practical. We conclude with deployment recommendations and research directions for more reliable numerical behavior in foundation models.

## Metadata
- **Published**: 2026-08-13T12:01:58Z
- **Authors**: Aoxin Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13129v1)