---
title: CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits
published: 2026-08-03T07:13:00Z
authors: Wei Wang, Shuanghe Liu, Zhu Zhuo, Jiaqi Zhong, Xiaozhao Zhao, Xiaojie Zuo, Jie Su
url: http://arxiv.org/abs/2608.01805v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits

## Abstract
LLM multi-agent systems suffer from Correctness Collapse, where high task-level accuracy conceals severe process-level failures. This is especially hazardous in safety-critical embodied settings such as automotive cockpits, where lexically correct utterances may trigger dangerous physical operations. Existing attribution methods rely on text traces alone, missing dependency structure, multi-channel evidence, and safety-aware evaluation. We introduce CockpitHAT, a hierarchical attribution framework that replaces positional windows with dependency-distance thresholds from interaction DAGs, integrates multi-channel evidence via an embodied adapter, and applies a safety-uplift to high-risk failures during confidence-weighted analyst consensus. We further release CockpitBench, a benchmark of 212 annotated failure traces spanning dialogue, vehicle-state, environmental, and memory channels, each labeled with ISO 26262 ASIL severity via three-expert consensus. On the public Who&When benchmark, CockpitHAT achieves agent-level / step-exact accuracies of 77.9% / 37.8% on the Hand-Crafted split and 86.5% / 46.0% on the Algorithm-Generated split, surpassing the text-only SOTA ECHO by up to 17.6 / 16.7 points. On CockpitBench, it attains 78.3% agent-level and 38.2% step-exact accuracy. These results establish dependency-aware, multi-channel, risk-calibrated attribution as an effective paradigm for reliable failure diagnosis in real-world embodied LLM multi-agent systems.

## Metadata
- **Published**: 2026-08-03T07:13:00Z
- **Authors**: Wei Wang, Shuanghe Liu, Zhu Zhuo, Jiaqi Zhong, Xiaozhao Zhao, Xiaojie Zuo, Jie Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01805v1)