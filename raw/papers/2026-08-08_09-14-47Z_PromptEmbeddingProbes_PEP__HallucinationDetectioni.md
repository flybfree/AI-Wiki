---
title: Prompt Embedding Probes (PEP): Hallucination Detection in LLMs from Hidden States
published: 2026-08-08T09:14:47Z
authors: Zakhar Mrykhin, Valentin Malykh
url: http://arxiv.org/abs/2608.08024v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompt Embedding Probes (PEP): Hallucination Detection in LLMs from Hidden States

## Abstract
Large language models (LLMs) can generate fluent and useful responses but remain prone to hallucinations. We introduce Prompt Embedding Probes (PEP), a white-box method for answer-level hallucination detection from the hidden states of a frozen LLM. PEP extends standard linear probes by augmenting the input with a small number of learnable prompt embeddings. We evaluate PEP on TriviaQA, GSM8K, and MedQA using Qwen3 models at multiple scales. PEP improves hidden-state-based detection over standard linear probes in the main in-distribution setting. We further evaluate PEP for pre-generation prediction, cross-model transfer, and out-of-distribution generalization. PEP remains effective in the pre-generation and cross-model settings, whereas robust cross-dataset transfer remains difficult. These results show that prompt-based adaptation can strengthen hidden-state probing while keeping the backbone frozen and adding only a small number of trainable parameters.

## Metadata
- **Published**: 2026-08-08T09:14:47Z
- **Authors**: Zakhar Mrykhin, Valentin Malykh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08024v1)