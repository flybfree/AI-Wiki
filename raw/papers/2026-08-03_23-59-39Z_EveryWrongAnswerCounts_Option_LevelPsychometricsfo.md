---
title: Every Wrong Answer Counts: Option-Level Psychometrics for LLM Multiple-Choice Benchmarks
published: 2026-08-03T23:59:39Z
authors: Xiao Fei, Yang Zhang, Sarah Almeida Carneiro, Michalis Vazirgiannis
url: http://arxiv.org/abs/2608.02966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Every Wrong Answer Counts: Option-Level Psychometrics for LLM Multiple-Choice Benchmarks

## Abstract
Most multiple-choice question (MCQ) benchmarks evaluate Large Language Models (LLMs) only by whether they select the correct answers. This binary scoring treats all incorrect responses alike, even though an LLM's preferences among incorrect options may contain systematic and useful information about its behavior and ability. We introduce the LLM Nominal Response Model (LLM-NRM), an option-aware psychometric framework that models the full distribution over answer choices to jointly estimate LLM ability and option-level item characteristics, while separating model-specific response calibration sharpness, positional preference, and difficulty-dependent fallback behavior. Across 189 LLMs and 31,554 items from 14 benchmarks, LLM-NRM predicts held-out LLM-item interactions more accurately than binary Item Response models and conventional nominal-response baselines, and its ability estimates achieve the strongest Spearman correlation of 0.920 with the external human-preference Arena.ai Elo leaderboard. Distractor identity contributes +101% additional Fisher Information per item beyond correctness, and incorrect responses alone recover full-information ability estimates with Spearman 0.943. The learned item parameters also enable efficient benchmarking, where 41 selected items preserve the full-bank ranking with Kendall's correlation 0.85, corresponding to a 770 times reduction. In conclusion, we show that incorrect answers carry distinct and useful measurement information rather than representing equivalent mistakes.

## Metadata
- **Published**: 2026-08-03T23:59:39Z
- **Authors**: Xiao Fei, Yang Zhang, Sarah Almeida Carneiro, Michalis Vazirgiannis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02966v1)