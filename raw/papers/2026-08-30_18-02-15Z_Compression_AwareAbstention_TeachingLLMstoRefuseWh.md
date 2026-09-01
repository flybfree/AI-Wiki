---
title: Compression-Aware Abstention: Teaching LLMs to Refuse When KV-Compression Masks Remove Answer Evidence
published: 2026-08-30T18:02:15Z
authors: Mohammadali Khodabandehlou, Bhaskar Krishnamachari
url: http://arxiv.org/abs/2608.29934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compression-Aware Abstention: Teaching LLMs to Refuse When KV-Compression Masks Remove Answer Evidence

## Abstract
KV-cache compression reduces LLM inference memory by evicting context tokens, but when the evicted tokens contain answer-bearing evidence, the model may hallucinate instead of recognizing that the compressed context is insufficient. We address this failure from a behavioral perspective: to our knowledge, this is the first work to formulate compression-aware abstention as a learning problem, in which a model learns to answer when supporting evidence survives compression and abstain when it does not. We construct supervision from compressor survival masks and tight answer-bearing spans, labeling examples as Confident when evidence survives and Abstain when it is removed. A 10.1M-parameter LoRA adapter trained on ~2.6K MuSiQue 2-hop QA examples reduces base-model hallucinations by 97% under prompt-style truncation while preserving correct answering on evidence-retaining examples. Unlike prompt-only abstention baselines, which over-abstain on many answerable high-retention examples, the trained adapter learns a conditional policy. We also evaluate the method under actual compressed-cache decoding, where multi-compressor training yields a 6-22x relative lift over the unaided base on evidence-retaining examples. Controlled-deletion experiments show that the learned behavior is driven by evidence content rather than input length alone.

## Metadata
- **Published**: 2026-08-30T18:02:15Z
- **Authors**: Mohammadali Khodabandehlou, Bhaskar Krishnamachari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29934v1)