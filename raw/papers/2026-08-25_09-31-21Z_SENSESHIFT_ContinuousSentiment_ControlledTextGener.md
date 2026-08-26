---
title: SENSESHIFT: Continuous Sentiment-Controlled Text Generation via Encoder-based Mask Infilling
published: 2026-08-25T09:31:21Z
authors: Shahed Masoudian, Markus Frohmann, Emmanouil Karystinaios, Navid Rekabsaz, Markus Schedl
url: http://arxiv.org/abs/2608.24304v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SENSESHIFT: Continuous Sentiment-Controlled Text Generation via Encoder-based Mask Infilling

## Abstract
Recent controllable text generation (CTG) for sentiment control has largely focused on decoder-based large language models, making causal attention the dominant paradigm. While effective for fluent generation, these models still struggle to satisfy complex constraints and follow fine-grained sentiment signals specified by users. Existing sentiment-aware CTG methods typically simplify the problem by treating sentiment either as a coarse categorical label (e.g., positive or negative) or as a single fine-grained control signal applied to an entire document. Consequently, more challenging settings such as sentence-level sentiment control within long-form text remain underexplored. To address these limitations, we introduce SenseShift , an encoder-based framework for fine-grained sentence-level CTG. Unlike standard decoder architectures, SenseShift leverages bidirectional attention, quantized sentiment signals, and iterative mask infilling to generate local sentences conditioned on target sentiment intensity. Empirical evaluations on story and review generation demonstrate that SenseShift achieves stronger sentiment controllability while maintaining text quality and robustness to out-of-domain generation compared to larger decoder-based baselines.

## Metadata
- **Published**: 2026-08-25T09:31:21Z
- **Authors**: Shahed Masoudian, Markus Frohmann, Emmanouil Karystinaios, Navid Rekabsaz, Markus Schedl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24304v1)