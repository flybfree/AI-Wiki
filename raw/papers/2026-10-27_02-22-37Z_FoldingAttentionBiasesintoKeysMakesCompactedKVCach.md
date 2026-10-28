---
title: Folding Attention Biases into Keys Makes Compacted KV Caches Run on Standard Kernels
published: 2026-10-27T02:22:37Z
authors: Utkarsh Kanwat
url: http://arxiv.org/abs/2610.36520v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Folding Attention Biases into Keys Makes Compacted KV Caches Run on Standard Kernels

## Abstract
Attention Matching (AM) compacts a KV cache by keeping some keys per head, refitting their values and adding a bias to each kept key's logit. FlashAttention and vLLM's paged caches have no input for it. We fold the bias into the keys along one closed-form direction per head, fitted on context queries, giving a plain cache with AM's size and head dimension and the model's own query path; the output error is bounded by how far each query's projection on that direction is from 1. With equal per-head budgets, unmodified vLLM serves folded caches through a KV connector, matching Hugging Face's answers on all 51 Qwen3-4B questions and its greedy output on 180 of 200 Qwen3-14B LongBench samples. With equal budgets on QuALITY (Qwen3-1.7B, 4B, 8B, Llama-3.1-8B) and LongHealth (three Qwen3 models), the fold is within noise of AM's accuracy in 13 of 14 settings, with lower KL to the full cache than dropping the bias in all 12 where both ran. Under the published per-head budgets, on Qwen3-4B, its Instruct-2507 variant and Llama-3.1-8B, it is within noise of AM in 9 of 10, no longer beats dropping the bias in KL, and the two each win once in accuracy.

## Metadata
- **Published**: 2026-10-27T02:22:37Z
- **Authors**: Utkarsh Kanwat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36520v1)