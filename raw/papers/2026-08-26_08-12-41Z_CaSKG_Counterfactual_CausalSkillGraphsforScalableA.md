---
title: CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval
published: 2026-08-26T08:12:41Z
authors: Zhiyuan Li, Linyuan Gao, Xuechun Ding, Hongwei Chen, Yuan Wu, Yi Chang
url: http://arxiv.org/abs/2608.25500v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval

## Abstract
Reusable skill libraries allow large language model (LLM) agents to reuse procedural knowledge across tasks, but they also turn memory access into a challenging retrieval problem. Full-library prompting preserves coverage at high context cost, vector retrieval returns compact neighborhoods but treats skills as independent text, and graph-based retrieval can recover workflow context only when the edges that carry relevance are reliable. We propose CaSKG, a counterfactual-causal skill graph framework that calibrates procedural relations before retrieval. CaSKG first builds a high-recall directed candidate graph from semantic, lexical, input/output, and structural evidence, with repair evidence and an optional LLM judge further refining candidate scores. It then applies direction-conditioned textual counterfactual probes that remove, substitute, and reorder skill pairs, aggregates the evidence with Bayesian smoothing, and publishes a state-filtered weighted graph for task-conditioned expansion. The graph is constructed offline and used without changing the downstream agent policy or task interface. Across six LLM backbones on ALFWorld ID-140 and ScienceWorld U211, CaSKG achieves the highest task score in all twelve combinations of model and benchmark. Relative to Graph-of-Skills (GoS), it improves the six-model macro-average ScienceWorld score from 72.62 to 80.50 and ALFWorld success from 80.01\% to 86.79\%, while reducing mean environment steps on both benchmarks. Qualitative and ablation analyses further show that calibrated edges help retrieval preserve prerequisites, state-changing actions, verification routines, and final completion steps. These results position edge-confidence calibration as an effective route to compact and executable skill retrieval at scale\footnote{Code is available at: https://github.com/ZhiyuanLi218/Caskg }.

## Metadata
- **Published**: 2026-08-26T08:12:41Z
- **Authors**: Zhiyuan Li, Linyuan Gao, Xuechun Ding, Hongwei Chen, Yuan Wu, Yi Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25500v1)