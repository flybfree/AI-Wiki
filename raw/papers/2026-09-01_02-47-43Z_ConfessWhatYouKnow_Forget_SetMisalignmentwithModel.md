---
title: Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning
published: 2026-09-01T02:47:43Z
authors: Miso Kim, Georu Lee, Seungwon Jeong, Woojin Lee
url: http://arxiv.org/abs/2609.00605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning

## Abstract
Machine unlearning for large language models (LLMs) often assumes that a pre-defined forget set matches what the model has memorized, but this frequently breaks in realistic privacy settings where the original training data is inaccessible. We term this gap forget-set misalignment and identify two cases. In Under Unlearning, the forget set omits memorized information and leakage persists. In Out-of-Knowledge Unlearning, the algorithm is driven to "forget" knowledge the model never learned, perturbing parameters and degrading utility. Using gradient-level analysis, we show these behaviors arise from misaligned unlearning targets rather than specific optimization choices. We then propose CONfession-to-Forget-Set (CONFS), a data-blind framework that constructs model-aligned forget sets by eliciting and formalizing the model's memorized knowledge. Across synthetic, multimodal, and real-world benchmarks, CONFS approaches Gold-standard performance on several metrics and achieves a competitive forgetting-utility balance, while preserving utility better than other data-blind forget-set constructions.

## Metadata
- **Published**: 2026-09-01T02:47:43Z
- **Authors**: Miso Kim, Georu Lee, Seungwon Jeong, Woojin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00605v1)