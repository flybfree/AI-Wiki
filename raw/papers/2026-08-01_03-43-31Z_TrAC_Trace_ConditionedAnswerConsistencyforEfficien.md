---
title: TrAC: Trace-Conditioned Answer Consistency for Efficient Uncertainty Quantification in LLMs
published: 2026-08-01T03:43:31Z
authors: Dahai Yu, Lin Jiang, Rongchao Xu, Guang Wang
url: http://arxiv.org/abs/2608.00422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrAC: Trace-Conditioned Answer Consistency for Efficient Uncertainty Quantification in LLMs

## Abstract
Large language models (LLMs) can generate fluent reasoning traces that nevertheless lead to incorrect answers, making response-level uncertainty estimation important for abstention, human review, and adaptive compute allocation. Existing approaches generally fall into three categories: passive single-trace methods use token-level confidence signals, sampling-based methods compare multiple complete traces at higher generation cost, and active prefix-based methods probe partial traces to study answer stabilization or preference transitions. However, none actively re-elicits an answer from a completed reasoning trace to measure its consistency with and support for the original answer. To address this gap, we introduce Trace-Conditioned Answer Consistency (TrAC), a correctness-supervised uncertainty quantification framework that combines active and passive signals anchored to one completed reasoning trace. Its active component, Prefix-Conditioned Elicitation (PCE), re-elicits a short answer conditioned on the completed trace and represents both its consistency with the original answer and its token-level probabilistic support. Its passive component, Trace Uncertainty Profile (TUP), summarizes how token-level uncertainty evolves throughout the original generation without additional decoding. A lightweight head then integrates the two representations into a response-correctness score. Across five mathematical reasoning benchmarks and three LLM families, TrAC improves macro AUROC by 1.8% and reduces AURC by 3.4% relative to eight-sample self-consistency, while using one complete reasoning trace and a short cached answer probe. When eight samples are already available, augmenting sample consensus with re-elicitation further improves macro AUROC by 4.3% and reduces AURC by 8.3%, without additional full-trace generation.

## Metadata
- **Published**: 2026-08-01T03:43:31Z
- **Authors**: Dahai Yu, Lin Jiang, Rongchao Xu, Guang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00422v1)