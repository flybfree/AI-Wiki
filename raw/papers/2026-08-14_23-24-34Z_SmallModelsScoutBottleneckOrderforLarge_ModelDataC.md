---
title: Small Models Scout Bottleneck Order for Large-Model Data Control
published: 2026-08-14T23:24:34Z
authors: Seungmin Choi, Jiwon Sung, Muhammad Umer, Abhiram Rao Gorle, Guijin Son, Youngjae Yu, John M. Cioffi
url: http://arxiv.org/abs/2608.14936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Small Models Scout Bottleneck Order for Large-Model Data Control

## Abstract
Small proxy models are commonly used to identify data mixtures for larger-scale training. We ask whether their training trajectories reveal another transferable structure: the order in which larger models should resolve skill bottlenecks. We formulate first-passage skill training, where each monitored skill has a target floor and the objective is to minimize the tokens required to reach all floors. We introduce LogFloor, a closed-loop controller that directs each round toward current bottlenecks, producing phase-ordered resolution trajectories. Across five bAbI skill slices on Qwen2.5-1.5B, LogFloor reduces token cost by 56.2% on average. In 70M-to-12B transfer, three-round replay of a 70M scout path reaches every floor in all eight target runs, saving 30.9% by pair mean, 39.4% in pooled training tokens, and 37.6% under source-cost accounting. On MMLU-control, a frozen scout path succeeds across all eight 12B runs. Collapsing a path to its static marginal mixture or reversing its phase order removes most benefits, while bottleneck labels alone remain partially useful. These results identify phase-ordered bottleneck resolution as a transferable curriculum structure for monitored skill-targeted training.

## Metadata
- **Published**: 2026-08-14T23:24:34Z
- **Authors**: Seungmin Choi, Jiwon Sung, Muhammad Umer, Abhiram Rao Gorle, Guijin Son, Youngjae Yu, John M. Cioffi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14936v1)