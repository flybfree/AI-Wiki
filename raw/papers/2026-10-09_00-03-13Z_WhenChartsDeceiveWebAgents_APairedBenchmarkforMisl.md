---
title: When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks
published: 2026-10-09T00:03:13Z
authors: Yisheng Li, Dongming Han, Hongkun Pan, Bingcheng Mao, Zijian Wang, Yunlong Mao, Wei Tong, Sheng Zhong
url: http://arxiv.org/abs/2610.12823v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks

## Abstract
Web agents increasingly browse, interpret, and act on web content on behalf of users. In many realistic workflows, however, the visual evidence they consume is not neutral: charts and dashboards can be misleading, shaping judgments without issuing any explicit malicious instruction. Unlike chart question answering, Web Agents treat charts as intermediate evidence whose misinterpretation can propagate into concrete downstream actions --- a reliability risk that remains underexplored. We introduce MisVisAgentBench, the first paired executable benchmark for evaluating how misleading visualizations affect Web Agent execution. It comprises 280 task instances in matched clean--misleading pairs that differ only in chart evidence. We further provide a diagnostic framework that isolates misleading-induced failures from baseline task difficulty (Zhu et al., 2025) and captures execution-level effects such as extra browsing steps and decision hesitation. Across thirteen vision-language Web Agents, replacing clean charts with misleading counterparts reduces the average task success rate by more than 34 percentage points. Moreover, these failures predominantly follow the targeted misleading action branch, suggesting that deceptive charts systematically redirect rather than randomly disrupt agent decisions. These results reveal that visualization robustness is a critical yet understudied dimension of Web Agent safety and reliability.

## Metadata
- **Published**: 2026-10-09T00:03:13Z
- **Authors**: Yisheng Li, Dongming Han, Hongkun Pan, Bingcheng Mao, Zijian Wang, Yunlong Mao, Wei Tong, Sheng Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12823v1)