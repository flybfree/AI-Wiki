---
title: SUP-MIMIC: A Multi-Task Clinical Diagnosis Benchmark for Evaluating LLMs' Robustness to Contradictory Evidence
published: 2026-08-30T05:59:47Z
authors: Yi Yu, Bo Wang, Chong Feng, Ge Shi, Xia Liu, Ziyi Yang, Xuewen Shi
url: http://arxiv.org/abs/2608.29582v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SUP-MIMIC: A Multi-Task Clinical Diagnosis Benchmark for Evaluating LLMs' Robustness to Contradictory Evidence

## Abstract
Current evaluations of large language models (LLMs) primarily focus on factual knowledge retrieval, overlooking the fundamental challenge of navigating the complex, non-bijective mappings between clinical indicators and diagnoses. Existing benchmarks fail to assess whether large language models truly possess the reasoning capability required for diagnostic ambiguity scenarios, where identical clinical presentations may correspond to different etiologies, and diagnostic convergence scenarios, where heterogeneous symptoms ultimately indicate the same disease. To address this issue, we propose SUP-MIMIC, a multi-task framework utilizing MIMIC-IV-v3.1 that comprises Basic Assessment (BA), Diagnostic Divergence Task (DDT), and Diagnostic Convergence Task (DCT). Specifically, DDT is designed to evaluate the model's "one-to-many" disambiguation capability among phenotypically similar cases, while DCT assesses the model's ability to identify "many-to-one" diagnostic patterns across different pathophysiological pathways. Comprehensive evaluation of state-of-the-art LLMs reveals substantial performance degradation on DDT and DCT compared to baseline tasks, exposing a systemic reliance on statistical shortcuts over genuine causal reasoning. Our findings further highlight a conservative bias toward "healthy" predictions, implying non-trivial risks for missed diagnoses in realistic medical settings. This work establishes a rigorous methodology for quantifying clinical reasoning robustness and provides a roadmap for enhancing the safety of language models in clinical medicine.

## Metadata
- **Published**: 2026-08-30T05:59:47Z
- **Authors**: Yi Yu, Bo Wang, Chong Feng, Ge Shi, Xia Liu, Ziyi Yang, Xuewen Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29582v1)