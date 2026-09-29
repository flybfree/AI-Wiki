---
title: STR: Supervised Transcoder Replacement for Reducing Steering Side Effects
published: 2026-09-26T12:03:39Z
authors: Haonan Yu, Junhao Liu, Zhenyu Yan, Haoran Lin, Xin Zhang
url: http://arxiv.org/abs/2609.32519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STR: Supervised Transcoder Replacement for Reducing Steering Side Effects

## Abstract
Model steering can strengthen a target behavior while degrading other useful behaviors. We introduce Supervised Transcoder Replacement (STR) to reduce these side effects for existing steering methods, including those fitted without a protection objective. STR learns a replacement for the multilayer perceptron (MLP) computation at the steering layer through supervision for target control, non-target preservation, and fidelity without steering. Selected steering methods then fit directions on the frozen replacement while retaining their own fitting objectives. We evaluate three steering methods across Gemma and Llama models using Corrigibility preferences and four harmful-request safety datasets. SALAD-Bench supplies protection training data and a separate in-distribution evaluation split; HarmBench, AdvBench, and StrongREJECT are reserved for out-of-distribution testing. STR substantially reduces steering side effects on the in-distribution evaluation and extends this protection to the unseen safety datasets while retaining effective target control. For target-only supervised steering vectors, pooled out-of-distribution attack success rate falls from 42.46% to 14.42% on Gemma-3-4B and from 34.97% to 12.91% on Gemma-3-12B. These results show that replacement training can benefit steering methods fitted without protection objectives.

## Metadata
- **Published**: 2026-09-26T12:03:39Z
- **Authors**: Haonan Yu, Junhao Liu, Zhenyu Yan, Haoran Lin, Xin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32519v1)