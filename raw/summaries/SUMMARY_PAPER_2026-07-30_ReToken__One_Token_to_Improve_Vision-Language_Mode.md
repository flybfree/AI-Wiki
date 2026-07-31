---
title: ReToken: One Token to Improve Vision-Language Models for Visual Retrieval
url: http://arxiv.org/abs/2607.28627v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-59-56Z_ReToken_OneTokentoImproveVision_LanguageModelsforV.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReToken, a lightweight method that uses a single learnable embedding to select relevant visual tokens from a KV cache for long visual context retrieval. It achieves consistent improvements on multiple benchmarks, including Visual Haystacks and LVBench, with gains of up to 13.4 points on Qwen3VL-8B. The approach enables efficient training and inference on a single H100 GPU.

## Key Takeaways
- ReToken trains a single embedding that acts as an explicit retrieval target to pick sparse query-relevant visual tokens from the pre-filled KV cache, reducing token processing load.
- It yields consistent gains across image and video tasks: Visual Haystacks improves Qwen3VL-8B by 13.4 points and InternVL3.5 by 12.4 points, exceeding a 20% relative improvement.
- The method transfers zero-shot to long video on LVBench, delivering an 8.0‑point gain for Qwen3VL-8B.

## Context
Long visual context is a bottleneck in vision-language models because processing many tokens simultaneously consumes GPU memory and degrades performance as distractors increase. Existing solutions often require large batch sizes or costly inference pipelines that cannot fit on standard hardware.

## Implications
ReToken’s lightweight design makes it practical for real‑world deployment where resources are limited, encouraging developers to adopt sparse token selection in long video retrieval systems. This could lead to faster response times and lower compute costs across multimodal applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28627v1)
