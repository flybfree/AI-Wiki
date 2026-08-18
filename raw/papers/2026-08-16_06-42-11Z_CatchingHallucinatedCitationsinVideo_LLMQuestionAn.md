---
title: Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study
published: 2026-08-16T06:42:11Z
authors: Yogesh Kumar
url: http://arxiv.org/abs/2608.15574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study

## Abstract
Video question answering systems built on vision-language models often produce timestamped claims with high confidence even when unsupported by the cited frame. This deceptive hallucination arises because timestamps imply grounding without ensuring correctness, increasing user trust but not accuracy. We introduce a pipeline that closes this loop. A retrieval-augmented language model drafts answers with per-claim timestamp citations, and each cited frame is independently re-examined before being shown to the user. We compare against a plain baseline and ablate three verification designs, evaluated on both Apple Silicon (MLX) and Google Colab (HF Transformers, CUDA). Directly asking the vision model whether a frame supports a claim fails completely (0% catch rate on 40 claims) due to sycophancy. Blind re-captioning plus a general LLM judge improves results but is unstable, oscillating between 0% and 100% flagged depending on prompt phrasing. Replacing that judge with a small natural language inference model yields a stable, interpretable verifier that catches 79% of fabricated claims on adversarial false-premise questions while leaving true claims untouched. We release the full pipeline, evaluation harness, and implementations for both Apple Silicon and Colab. Code is available at https://github.com/yogesh-iitj/grounded-video-qa.

## Metadata
- **Published**: 2026-08-16T06:42:11Z
- **Authors**: Yogesh Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15574v1)