---
title: Inverted Detection and Control in Steering Vectors
published: 2026-08-03T23:42:24Z
authors: Max Torop, Aria Masoomi, Jennifer Dy
url: http://arxiv.org/abs/2608.02957v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inverted Detection and Control in Steering Vectors

## Abstract
Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-control phenomenon in which some highly discriminative SVs that are aligned with positive representations can consistently promote the opposite behavior. We refer to such vectors as inverted-steering vectors (ISVs). We provide a geometric characterization of ISVs' effects, finding that steering along these directions systematically pushes representations in discriminative downstream heads as if the concept were absent, even prior to decoding. Motivated by this analysis, we propose an approach for distinguishing ISVs without requiring generation or associated response scoring. This enables targeted sign flips, which we use to improve a foundational detection-based steering pipeline via Inference Time Intervention (ITI). Our approach improves results in 27/30 experiments, ranging from +0.9% to +138%. We evaluate our findings on Gemma 3 12B, Qwen 2.5 14B, and Olmo 3 7B across 5 concepts.

## Metadata
- **Published**: 2026-08-03T23:42:24Z
- **Authors**: Max Torop, Aria Masoomi, Jennifer Dy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02957v1)