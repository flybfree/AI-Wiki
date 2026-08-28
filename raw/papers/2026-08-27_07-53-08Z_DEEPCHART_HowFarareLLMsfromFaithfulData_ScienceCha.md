---
title: DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?
published: 2026-08-27T07:53:08Z
authors: Jiahui tang, Kuicai Dong, Dexun Li, Hongchao Gu, Haocheng Yu, Wei Han, Chen Zhang, Yong Liu, Hao Wang, Enhong Chen
url: http://arxiv.org/abs/2608.26757v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?

## Abstract
Faithful chart generation in real-world data-science workflows requires grounding visualizations in scattered evidence, computing chart-ready quantities, and rendering them accurately. Modern LLMs can produce visually plausible, instruction-compliant charts, yet data-level hallucinations remain difficult to detect in long, noisy, and multimodal contexts. To measure this gap, we introduce DEEPCHART, an expert-annotated benchmark of 1,482 task-conditioned chart-generation instances drawn from real-world scientific papers, financial filings, and ecosystem reports. DEEPCHART formulates chart generation as an Extract--Reason--Visualize pipeline and evaluates source-data extraction, derived-data reasoning, and chart rendering stage by stage. Experiments with state-of-the-art models show that visually plausible charts often conceal data-level hallucinations, with extraction and reasoning errors common in realistic long and multimodal settings. These findings suggest that larger context windows alone are insufficient; faithful chart generation also requires reliable evidence extraction and quantitative reasoning before rendering. Our benchmark and associated resources are available at https://github.com/tangdouer1005/DeepChart.

## Metadata
- **Published**: 2026-08-27T07:53:08Z
- **Authors**: Jiahui tang, Kuicai Dong, Dexun Li, Hongchao Gu, Haocheng Yu, Wei Han, Chen Zhang, Yong Liu, Hao Wang, Enhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26757v1)