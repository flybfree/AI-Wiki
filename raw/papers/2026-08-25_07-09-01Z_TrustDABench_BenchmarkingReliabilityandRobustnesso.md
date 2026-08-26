---
title: TrustDABench: Benchmarking Reliability and Robustness of LLMs for Structured Data Analysis
published: 2026-08-25T07:09:01Z
authors: Boshen Shi, Yize Liu, Chen Zhao, Ce Chi, Zhendong Wang, Xing Wang, Junlan Feng
url: http://arxiv.org/abs/2608.24145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrustDABench: Benchmarking Reliability and Robustness of LLMs for Structured Data Analysis

## Abstract
LLMs are increasingly used to analyze spreadsheets, CSV files, and other structured data, but producing a correct-looking answer is not the same as producing a trustworthy analysis. A trustworthy result should be supported by a valid path from the user question to the relevant data evidence. This requirement creates two diagnostic questions: whether an LLM can refuse to answer or ask for clarification when such a path does not exist, and whether it can preserve the correct analysis when the same evidence is expressed in different table forms. We introduce TrustDABench, a benchmark that operationalizes these questions as reliability and robustness. Starting from the evidence-path view, we derive 19 perturbation operators and instantiate them through an Agentic-LLM-based generation framework. TrustDABench contains 2,340 human-verified perturbed instances, and we evaluate eight representative LLMs. The results show substantial headroom: the best reliability result is only 24.21% average MRS, achieved by GPT-5.5, while the best robustness result still has 9.10% average ASR, achieved by Claude-Sonnet-5. The failures are systematic: models rarely detect conflicting evidence, often continue along executable but unsupported analysis paths, and remain sensitive to perturbations that change observation boundaries or cross-table relations. These findings suggest that stronger evidence-boundary recognition and representation-invariant reasoning are still needed for reliable structured-data analysis.

## Metadata
- **Published**: 2026-08-25T07:09:01Z
- **Authors**: Boshen Shi, Yize Liu, Chen Zhao, Ce Chi, Zhendong Wang, Xing Wang, Junlan Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24145v1)