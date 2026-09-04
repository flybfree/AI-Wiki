---
title: LevelSyn: Physical-Aware Logic Synthesis via Level-Asynchronous Graph Neural Networks
published: 2026-09-03T09:46:02Z
authors: Jingyi Zhou, Zhengyuan Shi, Ziyang Zheng, Qiang Xu
url: http://arxiv.org/abs/2609.03594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LevelSyn: Physical-Aware Logic Synthesis via Level-Asynchronous Graph Neural Networks

## Abstract
As integrated circuit technology scales into the nanometer regime, the traditional disconnect between logic synthesis and physical design has led to significant PPA (Power, Performance, and Area) degradation and prolonged design closure cycles. Traditional logic synthesis relies on non-physical Wire Load Models (WLMs), while recent spectral-based placement predictors often neglect the inherent hierarchical logic depth and signal flow of netlists, which leads to low-fidelity spatial estimations. To bridge this gap, we propose LevelSyn, a novel physical-aware logic synthesis framework that integrates hierarchical representation learning with a wirelength-driven optimization engine. At its core, LevelSyn leverages a level-asynchronous Graph Neural Network (GNN) to predict high-fidelity gate coordinates by capturing the structural and directional semantics of And-Inverter Graphs (AIGs). To handle industrial-scale designs, a level-aligned subgraph partitioning strategy is introduced to eliminate memory bottlenecks while preserving local logical dependencies. These spatial insights are seamlessly integrated into a newly developed physical-informed synthesis engine within the Berkeley ABC framework. Experimental results on the EPFL benchmark suite demonstrate that LevelSyn significantly outperforms state-of-the-art (SOTA) methods, achieving an average power reduction of 6.89\% and a timing delay improvement of 27.48\%. Furthermore, post-place-and-route validation shows a 99.59\% reduction in design rule check (DRC) violations, highlighting its effectiveness in accelerating design convergence.

## Metadata
- **Published**: 2026-09-03T09:46:02Z
- **Authors**: Jingyi Zhou, Zhengyuan Shi, Ziyang Zheng, Qiang Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03594v1)