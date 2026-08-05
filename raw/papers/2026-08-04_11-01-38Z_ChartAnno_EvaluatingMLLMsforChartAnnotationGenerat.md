---
title: ChartAnno: Evaluating MLLMs for Chart Annotation Generation
published: 2026-08-04T11:01:38Z
authors: Zhenghan Chen, Zekai Shao, Lidan Tan, Xin Lin, Xingchen Zeng, Yi Shan, Ziyue Lin, Xiaoliang Fu, Xinyuan Liu, Yuetong Guo, Fen Wang, Bongshin Lee, Siming Chen
url: http://arxiv.org/abs/2608.03464v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ChartAnno: Evaluating MLLMs for Chart Annotation Generation

## Abstract
Multimodal large language models (MLLMs) have made significant progress in chart understanding, generation, and editing, but their ability to annotate existing charts remains underexplored. Annotating charts is a common yet challenging communicative task, requiring models to infer intended messages, interpret chart semantics, and place appropriate textual or graphical elements. To address this gap, we introduce ChartAnno, a benchmark for evaluating MLLMs on chart annotation generation. It contains 1,200 real-world charts with paired code and annotation instructions across three levels of instruction specificity. We evaluate 10 representative MLLMs under two primary input settings: (1) chart code alone and (2) both chart code and chart image, and further include a chart image-only ablation study. Results show that proprietary models remain stronger overall, although large-scale open-source models narrow the gap. More specific instructions improve annotation quality, while inferring abstract intent remains most difficult for current MLLMs. Providing chart images brings limited overall gains, with improvements mainly appearing in design-related metrics. These findings highlight chart annotation generation as a challenging task requiring semantic grounding and effective annotation design. Code and data will be released in a future version.

## Metadata
- **Published**: 2026-08-04T11:01:38Z
- **Authors**: Zhenghan Chen, Zekai Shao, Lidan Tan, Xin Lin, Xingchen Zeng, Yi Shan, Ziyue Lin, Xiaoliang Fu, Xinyuan Liu, Yuetong Guo, Fen Wang, Bongshin Lee, Siming Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03464v1)