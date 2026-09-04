---
title: Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards
published: 2026-09-02T21:49:21Z
authors: Alejandro Barón García, Feng Wang, Emilia Garcia Casademont, Han Xiao
url: http://arxiv.org/abs/2609.03181v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards

## Abstract
We present Jina-OCR-v1, an end-to-end document parsing model built to serve on low-budget GPUs. It combines the compressed-vision encoder and the 3B mixture-of-experts decoder of DeepSeek-OCR, which activates about 570M parameters per token, with a FastMTP speculative decoding head that shares a single draft block recursively across K=3 prediction steps. Greedy verification makes decoding lossless. Post-training combines instruction alignment, robustness fine-tuning on difficult documents, and GRPO under dense verifiable rewards: deterministic formula, table, and structural checks that award partial credit. The training data mixes cleaned public corpora with targeted synthetic pages. At the default dynamic-resolution setting, Jina-OCR-v1 scores 91.14 on OmniDocBench v1.6 and 83.4 on olmOCR-Bench, and reaches the highest page throughput in our comparison at 2.57 pages per second. On a low-budget GPU such as the NVIDIA L4, FastMTP doubles decoding speed over greedy autoregressive decoding. The model is publicly available at https://huggingface.co/jinaai/jina-ocr-v1.

## Metadata
- **Published**: 2026-09-02T21:49:21Z
- **Authors**: Alejandro Barón García, Feng Wang, Emilia Garcia Casademont, Han Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03181v1)