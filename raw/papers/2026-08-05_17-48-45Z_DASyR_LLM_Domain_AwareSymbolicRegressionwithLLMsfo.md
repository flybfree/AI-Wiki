---
title: DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery
published: 2026-08-05T17:48:45Z
authors: Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona
url: http://arxiv.org/abs/2608.05120v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery

## Abstract
Kinetic model discovery is a central challenge in chemical engineering, as accurate rate expressions are essential for understanding and controlling chemical and biological processes. Symbolic regression (SR) has emerged as a powerful data-driven approach for identifying interpretable kinetic models, but usually operates without domain knowledge, often exploring physicochemically implausible models. Large language models (LLMs) offer a promising avenue for injecting domain expertise into this search. Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery. The LLM performs two roles at each iteration: (1) a qualitative physicochemical critique of the best SR candidates, and (2) the proposal of new candidate rate expressions guided by the SR-generated models and embedded chemical knowledge. Our framework is evaluated on four in silico case studies of increasing complexity, spanning heterogeneous catalysis and bioprocess systems. Results show the LLM-guided framework reduces iterations to identify the ground-truth model by $41.7-79.3\%$ versus a state-of-the-art SR framework, with the LLM directly proposing the correct model structure in over half of the guided runs. In practical settings, where each iteration typically requires a new wet-lab experiment, this translates into a substantial reduction in experimental effort. Predictive performance on an independent validation set is equivalent between both approaches, with $R^2>0.98$ in all case studies. Ablation studies indicate that both the SR component and the LLM scale contribute to this performance, with a reduced-size LLM largely retaining discovery efficiency. These findings demonstrate that LLMs can effectively inject domain knowledge into scientific model discovery, paving the way toward fully automated, domain-aware kinetic modelling pipelines.

## Metadata
- **Published**: 2026-08-05T17:48:45Z
- **Authors**: Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05120v1)