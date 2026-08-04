---
title: SymboUQ: Symbolic Uncertainty Quantification for Spatial Reasoning in LLMs
published: 2026-08-01T03:36:09Z
authors: Dahai Yu, Lin Jiang, Rongchao Xu, Guang Wang
url: http://arxiv.org/abs/2608.00417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SymboUQ: Symbolic Uncertainty Quantification for Spatial Reasoning in LLMs

## Abstract
Although large language models (LLMs) can produce fluent spatial reasoning traces, their intermediate relations may fail to support the final conclusion, making token-level confidence insufficient for final-answer reliability estimation. Existing formal verifiers provide stronger semantic evidence, but their applicability is partial: a parsed claim need not yield a definite semantic verdict. To address this issue, we introduce SymboUQ, a symbolic uncertainty quantification framework that estimates final-answer reliability from reasoning traces by distinguishing symbolizability, whether a claim can be represented in the verifier's formal language, from semantic determinacy, whether its execution yields an entailed or contradicted verdict rather than an unknown or not-evaluable outcome. SymboUQ comprises (i) a Layout Auditor that executes ordered spatial claims and extracts feasibility, conflict, and repair evidence; (ii) a label-free Determinacy Profile that characterizes effective executable coverage; and (iii) a Determinacy-Aware Reliability Composer that integrates constraint-based, representation-based, and decoding-based scores according to verifier applicability. Extensive experiments on five spatial reasoning benchmarks with four frozen LLM backbones show that SymboUQ achieves approximately an 8% relative improvement in AUROC and a 7% relative reduction in class-balanced Brier loss over the strongest baseline.

## Metadata
- **Published**: 2026-08-01T03:36:09Z
- **Authors**: Dahai Yu, Lin Jiang, Rongchao Xu, Guang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00417v1)