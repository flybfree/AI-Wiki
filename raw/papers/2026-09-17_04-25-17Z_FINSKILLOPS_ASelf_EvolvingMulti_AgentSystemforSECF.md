---
title: FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA
published: 2026-09-17T04:25:17Z
authors: Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, Chaolong Jiang, Jijun Chi, Tung Sum Thomas Kwok, Bohuai Xiao, Jingrui Tian, Xinlu Wu, Xingao Zhan, Peng Lu, Muzhi Li, Yihong Wu, Liheng Ma, Sicheng Lyu, Tianshuo Yan, Junhao Zhu, Yaqian Xu, Lei Ding, Yufei Cui, Ziquan Liu, Boyu Han, Hengli Liu, Ling Zhou, Xinyu Wang
url: http://arxiv.org/abs/2609.19680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA

## Abstract
Financial QA systems are typically improved before deployment through better retrieval, prompting, or agent coordination, leaving their reliability behavior fixed thereafter. In practice, new SEC-filing questions repeatedly expose heterogeneous errors in period, entity, evidence use, and calculation. Existing self-improvement methods can turn failures into new behaviors, but offer limited control over where a correction should apply or which previously correct answers it may break. We therefore frame post-deployment improvement as controlled behavioral maintenance: recurring failures should become scoped skill patches, and each patch should earn deployment with- out introducing regressions. We instantiate this view in FINSKILLOPS, a multi-agent system for SEC filing QA. FINSKILLOPS derives reusable skills from evidence-grounded, typed failure diagnoses and governs them through targeted validation, protected-case regression checks, negative controls, and versioned replacement or retirement. Across six financial QA benchmarks, a single frozen skill registry achieves the highest verdict-weighted correctness and reference consistency among the evaluated systems. Evolved skills raise correctness from 3.70 to 4.55 on our enhanced benchmark. In a separate 12-round operational study, only six of 33 proposed skills are promoted, while the monitoring non-correct rate falls from 20.0% to 12.5%. These results establish controlled skill scope, admission, and lifecycle management as the foundation for reliable self-improvement.

## Metadata
- **Published**: 2026-09-17T04:25:17Z
- **Authors**: Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, Chaolong Jiang, Jijun Chi, Tung Sum Thomas Kwok, Bohuai Xiao, Jingrui Tian, Xinlu Wu, Xingao Zhan, Peng Lu, Muzhi Li, Yihong Wu, Liheng Ma, Sicheng Lyu, Tianshuo Yan, Junhao Zhu, Yaqian Xu, Lei Ding, Yufei Cui, Ziquan Liu, Boyu Han, Hengli Liu, Ling Zhou, Xinyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19680v1)