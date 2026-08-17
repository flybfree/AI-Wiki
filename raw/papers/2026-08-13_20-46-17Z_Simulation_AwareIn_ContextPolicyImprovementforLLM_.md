---
title: Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement
published: 2026-08-13T20:46:17Z
authors: Bingyang Liu, Ziming Wei, Xiaohan Gao, David Z. Pan
url: http://arxiv.org/abs/2608.13767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement

## Abstract
Analog IC layout design remains a labor-intensive iterative process dominated by simulation-driven refinement. Although end-to-end layout generators accelerate initial placement and routing, they still require experts to manually tune layout optimization parameters with repeated post-layout simulations for stringent design specifications. While Bayesian Optimization (BO) is widely adopted for parameter tuning in analog IC design, at the layout level it typically requires hundreds to thousands of evaluations, each involving costly parasitic extraction and post-layout simulation, which makes it impractical. Recently, Large Language Models (LLMs) have demonstrated potential in improving the sample efficiency of such simulation-driven tuning. However, their restricted access to geometric layout context and design-specific heuristics limits their ability to manipulate the layout optimization process. In this paper, we propose a simulation-aware LLM multi-agent framework that performs in-context policy improvement (ICPI) by iteratively updating layout optimization parameters exposed by an analog layout generator through an act-observe-reflect loop on compact structured layout representations. Experiments on real-world analog circuits show that, with only tens of post-layout simulations, our approach improves post-layout performance over the generator's built-in heuristics and BO-based tuning method.

## Metadata
- **Published**: 2026-08-13T20:46:17Z
- **Authors**: Bingyang Liu, Ziming Wei, Xiaohan Gao, David Z. Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13767v1)