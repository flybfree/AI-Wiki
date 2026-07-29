---
title: Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis
published: 2026-07-28T10:35:20Z
authors: Wanxu Cai, Zhengyu Chen, Huaisheng Zhu, Wei Wang, Jingang Wang, Qiang Xu
url: http://arxiv.org/abs/2607.25554v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis

## Abstract
Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. While recent Tool-Integrated Reasoning (TIR) internalizes deep search for multi-hop retrieval of facts, forecasting further demands temporal search and reasoning over historical trends and dynamic shifts. The key obstacle is data: historical queries induce temporal leakage that degrades forecasting into retrieval. Prior works either freeze information gathering with static observations, or rely on rejection sampling or unresolved fresh queries that discard vast amounts of data, degrading synthesis efficiency. We propose a time-truncation harness that enforces a temporal cut-off at every turn, enabling TIR-style sampling from historical events, reducing temporal leakage and reliance of rejection sampling or unsolved queries, increasing the sampling efficiency. We further build a large-scale corpus and a process-based metric and show that our harness naturally induces a broader temporal breadth of search and raises the proportion of high-quality data, further increasing the efficiency and reducing the reliance on complex rubrics. Distillation experiments show that students trained on harness-intervened data achieve the best performance, demonstrating harness-assisted model evolving that turns higher quality temporal search and reasoning data into a parametric advancement of the students.

## Metadata
- **Published**: 2026-07-28T10:35:20Z
- **Authors**: Wanxu Cai, Zhengyu Chen, Huaisheng Zhu, Wei Wang, Jingang Wang, Qiang Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25554v1)