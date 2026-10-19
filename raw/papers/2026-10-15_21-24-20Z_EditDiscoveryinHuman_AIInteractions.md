---
title: Edit Discovery in Human-AI Interactions
published: 2026-10-15T21:24:20Z
authors: Alireza Mirrokni, Shayan Kiyani, George Pappas, Hamed Hassani
url: http://arxiv.org/abs/2610.22661v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Edit Discovery in Human-AI Interactions

## Abstract
Human-AI interactions are becoming a rich source of data for improving AI systems: while many model responses are already satisfactory, others expose failures that could become valuable supervision if identified and corrected. We study this setting through the notion of an editor: a more capable evaluation process that can inspect a response and either confirm it or modify it, but whose invocation is costly. The editor may be a human expert, a stronger AI system, or the same model equipped with additional computation, context, tools, or information. The key challenge is to decide which interactions to send to the editor before knowing whether an edit will actually be made, since invoking the editor itself consumes limited resources such as expert time, inference cost, latency, or tool-use overhead. We formulate this problem as Edit Discovery Optimization (EDO), which seeks to minimize edit opportunities missed among skipped interactions while controlling unnecessary confirmations and respecting an editor-cost budget. We characterize the population-optimal policy and show that it takes the form of a cost-adjusted threshold on the posterior probability of an edit. Building on this structure, we develop EDIT (Edit Discovery via Iterative Thresholding), an online algorithm for the partial-feedback setting in which edit labels are revealed only for selected interactions. EDIT combines an adaptive edit score, a confirmation-control threshold, and a cost-aware selection rule; it satisfies the editor budget at every round and controls the average confirmation rate up to a vanishing finite-horizon term, without distributional assumptions on the interaction stream. Across four reasoning and factual question-answering benchmarks, EDIT achieves a better trade-off between editor cost, Type-I error, and Type-II error than direct LLM-based batch selection.

## Metadata
- **Published**: 2026-10-15T21:24:20Z
- **Authors**: Alireza Mirrokni, Shayan Kiyani, George Pappas, Hamed Hassani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22661v1)