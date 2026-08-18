---
title: Hallucination Span Detection with Input-Side Evidence Alignment
published: 2026-08-16T15:30:29Z
authors: Miyu Yamada, Yuki Arase
url: http://arxiv.org/abs/2608.15804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hallucination Span Detection with Input-Side Evidence Alignment

## Abstract
Hallucinations remain a major obstacle to the reliable use of large language models (LLMs) in conditional text generation. Existing methods primarily assess the factuality of an entire generated text, providing limited insight into which output spans are hallucinated or how they relate to the input. We introduce the task of hallucination span detection with input-side evidence alignment, which jointly identifies hallucinated spans and aligns output tokens with the corresponding input evidence. Our approach is based on the observation that faithful output tokens are predictable from the input, whereas hallucinated tokens are not. We therefore train an encoder-based model to predict masked output tokens from the input representation, using prediction confidence for hallucination detection while naturally producing alignments to the input. Experiments show that the proposed method effectively detects hallucinated spans and identifies meaningful input-side evidence. Human evaluation confirms the quality of the predicted alignments.

## Metadata
- **Published**: 2026-08-16T15:30:29Z
- **Authors**: Miyu Yamada, Yuki Arase
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15804v1)