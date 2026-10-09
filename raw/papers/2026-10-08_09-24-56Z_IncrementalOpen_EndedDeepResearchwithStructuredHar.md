---
title: Incremental Open-Ended Deep Research with Structured Harness
published: 2026-10-08T09:24:56Z
authors: Meilin Chen, Hongyuan Bao
url: http://arxiv.org/abs/2610.11566v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Incremental Open-Ended Deep Research with Structured Harness

## Abstract
Existing Open-Ended Deep Research (OEDR) systems primarily generate reports from scratch, making them inefficient for scenarios where research reports need to be continuously maintained as new information emerges. We introduce \textbf{Incremental Open-Ended Deep Research (Incremental-OEDR)}, a research setting that treats a report as an evolving research state and incrementally updates it by preserving valid knowledge, revising outdated or incomplete content, and incorporating newly available information. To support this setting, we propose \textbf{Structured Harness}, which represents reports as structured collections of outlines, sections, and supporting evidence, and provides structured retrieval, a persistent structured evidence pool, and structured generation for selective report updating and evidence reuse. We further establish a temporal evaluation framework spanning ten years, with \emph{Single-Step Task} and \emph{Long-Chain Task} to evaluate incremental updates over both individual transitions and long-term update chains. Extensive Experiments on DeepResearch Bench and DeepConsult under both the Open-source Configuration (OC) and Proprietary Configuration (PC) show that Incremental-OEDR maintains competitive report quality while substantially improving report continuity and reducing research costs. As shown in Figure~\ref{fig:profile}, it achieves up to 0.51 higher content-level ROUGE-L F1, 0.63 higher outline-level EM F1, 33\% lower token consumption, and 61\% fewer search calls than OEDR on DeepResearch Bench. For more details, please refer to our project page: https://ioedr-project.github.io/.

## Metadata
- **Published**: 2026-10-08T09:24:56Z
- **Authors**: Meilin Chen, Hongyuan Bao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11566v1)