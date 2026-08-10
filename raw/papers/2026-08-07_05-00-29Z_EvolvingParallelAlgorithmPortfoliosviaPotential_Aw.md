---
title: Evolving Parallel Algorithm Portfolios via Potential-Aware Instance Generation with LLMs
published: 2026-08-07T05:00:29Z
authors: Shaofeng Zhang, Shengcai Liu, Zhiyuan Wang, Ke Tang
url: http://arxiv.org/abs/2608.06808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evolving Parallel Algorithm Portfolios via Potential-Aware Instance Generation with LLMs

## Abstract
The Automatic Construction of Portfolios via Large Language Models (LLM-ACP) suffers from poor generalization in practical few-shot scenarios when solving complex combinatorial optimization problems. Instance and algorithm co-evolution frameworks address this by expanding the training dataset with generated hard instances on which the current algorithm portfolio underperforms, thereby enhancing generalization. However, this paradigm faces two critical limitations: evaluating instance hardness relies on high-quality reference solutions, and single-mode generation patterns limit instance diversity. To overcome these limitations, we introduce the Potential-aware Instance and Algorithm Co-evolution (PIAC) framework. Our core contribution is twofold. First, we propose potential gain, a novel metric that eliminates the need for reference solutions. This metric estimates generalization gain by perturbing the generated algorithms and assessing their improvement potential on generated problem instances. Second, PIAC leverages LLMs to synthesize diverse instance mutators, exploring a broader region of the problem-instance space and thereby enhancing the portfolio's generalization capabilities. Given that perturbation spaces vary across different algorithms, we instantiate our framework on Greedy Constructive, Ant Colony Optimization, and Guided Local Search algorithmic backbones. Comprehensive evaluations on the Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP) across six distinct data distributions demonstrate that PIAC consistently outperforms state-of-the-art LLM-ACP baselines, notably achieving a 19.76% relative improvement for TSP Greedy Constructive portfolios.

## Metadata
- **Published**: 2026-08-07T05:00:29Z
- **Authors**: Shaofeng Zhang, Shengcai Liu, Zhiyuan Wang, Ke Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06808v1)