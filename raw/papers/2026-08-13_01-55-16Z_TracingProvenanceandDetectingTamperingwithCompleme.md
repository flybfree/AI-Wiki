---
title: Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks
published: 2026-08-13T01:55:16Z
authors: Xiaoyan Feng, Yanjun Zhang, He Zhang, Leo Yu Zhang, Shirui Pan
url: http://arxiv.org/abs/2608.12713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks

## Abstract
Watermarking LLM-generated text is an important task for tracing its provenance. Existing LLM watermarks preserve provenance under editing, but this same robustness allows an adversary to alter critical content while retaining attribution, a vulnerability known as piggyback spoofing. We introduce an innovative watermark that jointly provides provenance and tamper evidence. It co-embeds a robust signal and a fragile signal into each generated token. The signals share the same mechanism but use independent keys and different seeding windows over normalized text, making one resilient to edits and the other sensitive to reader-visible changes. Multiple rounds of unbiased tournament reweighting preserve the expected generation distribution, while a periodic round-allocation pattern controls the trade-off between the two signals. At detection, their scores form a two-dimensional space supporting three decisions: Intact, Tampered, and No-Watermark. Across two large language models and two prompt datasets, our method demonstrates the highest tamper-detection rate among the evaluated methods while maintaining competitive attribution robustness and perplexity. Ablation studies show that reliable three-state detection requires a well-defined notion of intactness, co-embedding of the two signals, and complementary sensitivity to edits.

## Metadata
- **Published**: 2026-08-13T01:55:16Z
- **Authors**: Xiaoyan Feng, Yanjun Zhang, He Zhang, Leo Yu Zhang, Shirui Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12713v1)