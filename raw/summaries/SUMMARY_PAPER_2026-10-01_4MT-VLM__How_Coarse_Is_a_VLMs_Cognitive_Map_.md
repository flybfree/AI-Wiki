---
title: 4MT-VLM: How Coarse Is a VLMs Cognitive Map?
url: http://arxiv.org/abs/2609.39238v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_08-06-49Z_4MT_VLM_HowCoarseIsaVLMsCognitiveMap.md
generated_at: 2026-10-01 10:56
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces 4MT-VLM, a novel benchmark designed to evaluate how well vision-language models maintain spatial recognition when viewing environments from unfamiliar angles. The study reveals that while current models can identify locations from trained perspectives, their performance collapses under viewpoint rotation, indicating a fundamentally coarse and unstable internal representation of three-dimensional space compared to human observers.

## Key Takeaways
- The 4MT-VLM dataset uses procedurally generated landscapes across five controlled stimulus modes to isolate spatial layout from visual appearance cues, enabling precise measurement of viewpoint-invariant recognition using four-alternative forced choice testing.
- State-of-the-art vision-language models experience severe performance degradation when camera angles shift beyond forty-five degrees, frequently falling below random chance levels while human participants maintain high accuracy under identical conditions.
- Even leading frontier architectures only partially recover spatial awareness when distractor objects are separated by more than thirty meters, confirming that their cognitive maps lack the fine-grained geometric resolution required for robust navigation and environmental understanding.

## Context
Evaluating artificial intelligence systems requires moving beyond static image recognition to assess dynamic spatial reasoning capabilities that mirror human perception. This benchmark addresses a critical gap in multimodal AI research by providing a standardized, clinically inspired protocol to measure how well models construct stable mental representations of physical environments across varying perspectives.

## Implications
The findings suggest that current vision-language architectures are

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39238v1)
