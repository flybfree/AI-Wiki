---
title: Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration
published: 2026-08-20T06:50:23Z
authors: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
url: http://arxiv.org/abs/2608.19701v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration

## Abstract
Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode \textit{Memory Correlation Bias}. To address the issue, we propose the \textbf{C}orrelation-\textbf{A}ware \textbf{M}emory \textbf{A}rbitration (CAMA) framework that jointly decouples retrieved memories and recovers missing independent evidence. We model the retrieved memories as query-conditioned evidence groups and combine neural dependency inference with provenance-based symbolic priors to estimate the effective number of independent evidence sources, thereby preventing correlated memories from forming a false majority. Since critical independent evidence may be absent from the initial retrieval set, \textsc{CAMA} further learns a sequential recovery policy that actively retrieves alternative evidence or traces upstream sources before making the final decision, aiming to recover sufficient independent evidence for reliable arbitration while minimizing retrieval cost. Experiments on multiple benchmarks demonstrate the superiority of our method over the state-of-the-art baseline methods, suppressing false majorities induced by correlated memories.

## Metadata
- **Published**: 2026-08-20T06:50:23Z
- **Authors**: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19701v1)