---
title: ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization
published: 2026-08-04T06:48:17Z
authors: Hujian Zhu, Yihao Huang, Felix Juefei-Xu, Xinfeng Li, Peng Zeng, Simeng Qin, Qing Guo, Geguang Pu
url: http://arxiv.org/abs/2608.03210v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization

## Abstract
Foundation models have achieved remarkable success across diverse tasks, but they remain vulnerable. To investigate such vulnerabilities, semantic-shift jailbreaks have recently emerged as a promising attack paradigm. They bypass explicit safety mechanisms by replacing harmful terms in original harmful questions with benign alternatives and leveraging contextual information to induce the target model to reinterpret these alternatives as their corresponding harmful concepts. However, existing semantic-shift jailbreaks often achieve limited effectiveness. In this work, we reveal that this limitation arises from overlooking the semantic-shift capability of contexts. Through systematic analysis, we find that contexts exhibit substantially different abilities in inducing semantic shifts: contexts with stronger semantic-shift capabilities are more likely to guide models toward recovering harmful meanings and achieving successful jailbreaks. Based on this finding, we systematically identify and distill the characteristics of effective contexts and propose a black-box context-aware semantic-shift jailbreak framework with Iterative Context Optimization (ICO). In each iteration, ICO leverages these characteristics and feedback from the target model to optimize contexts. Extensive experiments on three datasets and eight target foundation models demonstrate that ICO consistently outperforms eight state-of-the-art baselines, achieving an average attack success rate of 74.6%.

## Metadata
- **Published**: 2026-08-04T06:48:17Z
- **Authors**: Hujian Zhu, Yihao Huang, Felix Juefei-Xu, Xinfeng Li, Peng Zeng, Simeng Qin, Qing Guo, Geguang Pu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03210v1)