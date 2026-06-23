---
title: Randomized YaRN Improves Length Generalization for Long-Context Reasoning
published: 2026-06-22T17:59:53Z
authors: Manas Mehta, Fangcong Yin, Greg Durrett
url: http://arxiv.org/abs/2606.23687v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Randomized YaRN Improves Length Generalization for Long-Context Reasoning

## Abstract
Large language models (LLMs) are typically pretrained on short sequences and then extended to work on longer sequences with additional training. However, such LLMs still struggle to further generalize to very long sequences. We propose Randomized YaRN, a training method that improves length generalization by combining YaRN-based positional extrapolation with randomized positional encoding and a length curriculum. During training on short context data, tokens are assigned YaRN positional encodings sampled from a larger position range, exposing the model to out-of-distribution positional representations even on short-context inputs. We evaluate Randomized YaRN on two challenging long-context reasoning benchmarks, BABILong and Multi-Round Coreference Resolution (MRCR). When training on data with <8K context, Randomized YaRN consistently improves reasoning performance on context lengths from 16K to 128K and outperforms standard fine-tuning, with the largest gains appearing at far out-of-distribution lengths. Our results suggest that progressively exposing models to OOD positional distributions provides an effective recipe for generalizable long-context reasoning.

## Metadata
- **Published**: 2026-06-22T17:59:53Z
- **Authors**: Manas Mehta, Fangcong Yin, Greg Durrett
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.23687v1)