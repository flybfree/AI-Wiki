---
title: Instruction Quality Matters: Refining Instructions for Effective Preference Learning
published: 2026-08-27T08:09:36Z
authors: Seohyeong Lee, Hwaran Lee, Buru Chang
url: http://arxiv.org/abs/2608.26779v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instruction Quality Matters: Refining Instructions for Effective Preference Learning

## Abstract
Preference learning optimizes models using response pairs, yet the informativeness of these pairs is fundamentally shaped by the instructions from which they are generated. We identify instruction quality as a hidden bottleneck in preference learning: low-quality or ambiguous instructions restrict the response-quality distribution, limiting strong chosen responses and weakening preference signals. Through Best- and Worst-of-N analyses, we show that instruction quality constrains both the ceiling and floor of sampled response quality. Motivated by this observation, we introduce an instruction-refinement pipeline that selects weak instructions using reward signals and revises them with rubric-guided LLM feedback, improving preference data without discarding examples. Across offline and online preference learning settings, experiments on multiple models and benchmarks show broad alignment improvements over original data and alternative data-improvement strategies. Further analyses indicate that instruction refinement raises achievable response quality and complements response-centric preference data curation. Overall, instruction quality emerges as a key factor governing how informative preference signals are formed for LLM alignment. Code is available at: https://github.com/01choco/instruction-refinement/

## Metadata
- **Published**: 2026-08-27T08:09:36Z
- **Authors**: Seohyeong Lee, Hwaran Lee, Buru Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26779v1)