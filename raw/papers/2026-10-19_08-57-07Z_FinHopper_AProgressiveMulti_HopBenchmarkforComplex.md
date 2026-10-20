---
title: FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation
published: 2026-10-19T08:57:07Z
authors: Yuxuan Wu, Miaopei Lin, Qiufang Ying, Lin Dan, Hao Zhao, Qirui Liu, Yuteng Shen, Shaohui Wu, Weihong Luo, Xiku Du, Xing Tang, Hao Chen
url: http://arxiv.org/abs/2610.26036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation

## Abstract
Financial agents are expected to answer factual investment queries through open search, but financial multi-hop retrieval differs from general multi-hop QA in a crucial way: each intermediate answer is an exact typed constraint, such as an entity, date, event, or numerical indicator, that determines the next query. This strict answer-conditioned dependency makes small intermediate errors cascade into plausible but wrong search trajectories. We introduce FinHopper, a benchmark for complex financial agents with controlled reasoning depth from 1 to 6 hops, covering stocks, funds, and macroeconomic facts, with gold intermediate answers for process-level evaluation. To construct FinHopper at scale, we design a state-transition-based synthesis framework that composes verified atomic financial QA patterns into dependency-preserving chains, followed by targeted in-synthesis verification, model-ensemble checking, and public-search validation by financial experts. Experiments with 20 LLM-agent configurations show that public search tools are necessary but insufficient: performance drops sharply as hop depth increases, the best model remains far below human experts, and process-aware scoring reveals partial reasoning progress hidden by final-answer-only evaluation. The benchmark is available at https://github.com/justajustin/FinHopper/.

## Metadata
- **Published**: 2026-10-19T08:57:07Z
- **Authors**: Yuxuan Wu, Miaopei Lin, Qiufang Ying, Lin Dan, Hao Zhao, Qirui Liu, Yuteng Shen, Shaohui Wu, Weihong Luo, Xiku Du, Xing Tang, Hao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26036v1)