---
title: Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems
published: 2026-10-08T09:44:59Z
authors: Jiaqi Liao, Yuanzhao Zhai, Huanxi Liu, Xu Zhang, Zheming Zhuang, Dawei Feng, Bo Ding, Huaimin Wang
url: http://arxiv.org/abs/2610.11600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems

## Abstract
LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with external resources. However, attributing failures in such systems remains challenging because the observed outcome often does not directly reveal the error responsible for the failed execution. In this work, the attribution target is the decisive error, defined as the agent--step pair whose correction would recover the failed execution. Existing approaches largely identify suspicious steps without explicitly modeling how errors propagate across interactions or persist in unresolved loops, making decisive errors difficult to distinguish from downstream failure symptoms. We propose \textbf{E}rror-Propagation \textbf{M}odeling for \textbf{F}ailure \textbf{A}ttribution (\textbf{EMFA}). EMFA constructs a structured representation of the failed trajectory, models both cascading propagation and persistent interaction loops, and uses propagation-aware candidate screening followed by counterfactual verification to identify the decisive agent--step pair. On the Who\&When benchmark, EMFA achieves state-of-the-art step-level attribution accuracy and remains competitive at the agent level. It improves the previous best step-level results by 3.45 and 4.40 percentage points on the Hand-Crafted and Algorithm-Generated subsets, respectively.

## Metadata
- **Published**: 2026-10-08T09:44:59Z
- **Authors**: Jiaqi Liao, Yuanzhao Zhai, Huanxi Liu, Xu Zhang, Zheming Zhuang, Dawei Feng, Bo Ding, Huaimin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11600v1)