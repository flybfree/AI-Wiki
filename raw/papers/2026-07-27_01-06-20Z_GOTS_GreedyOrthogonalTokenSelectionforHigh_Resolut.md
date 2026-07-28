---
title: GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models
published: 2026-07-27T01:06:20Z
authors: Jun Ling, Tao Huang, Junzhuo Liu, Bowen Tang, Peng Wang
url: http://arxiv.org/abs/2607.23913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models

## Abstract
Modern vision-language models (VLMs) increasingly rely on dynamic or high-resolution visual encoding, producing thousands of visual tokens that substantially increase downstream language-model inference cost. Existing token-reduction methods assess token utility through token-wise importance, query relevance, coverage, pairwise diversity, or subset-level objectives. Our key insight is to view visual token reduction through selected-span complementarity: instead of scoring a token in isolation or through pairwise relations, we assess how much of its feature is orthogonal to the span of the already retained subset. Based on this perspective, we propose Greedy Orthogonal Token Selection (GOTS), a training-free and query-agnostic method. At each step, GOTS selects the token with the largest residual energy orthogonal to the current retained span. This rule exactly maximizes the one-step augmented Gram determinant among candidate additions, giving each greedy step a precise local geometric guarantee for subset expansion. Across five high-resolution VLM backbones from the Qwen-VL and InternVL families and eleven diverse benchmarks, GOTS achieves higher average performance retention than the strongest evaluated baselines, and a controlled OCRBench study shows that it reduces model-side time-to-first-token after accounting for selection overhead. Code is available at https://github.com/newLLing/GOTS.

## Metadata
- **Published**: 2026-07-27T01:06:20Z
- **Authors**: Jun Ling, Tao Huang, Junzhuo Liu, Bowen Tang, Peng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23913v1)