---
title: FunL2O: LLM-Guided Feature Function Design for Learning to Optimize
published: 2026-07-29T18:52:44Z
authors: Bingheng Li, Junyang Cai, Yupeng Zhang, Bistra Dilkina, Jayant Kalagnanam, Dzung T. Phan
url: http://arxiv.org/abs/2607.27389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FunL2O: LLM-Guided Feature Function Design for Learning to Optimize

## Abstract
Learning-to-optimize (L2O) methods accelerate repeated optimization by training models to predict solutions, warm starts, branching decisions, or other forms of solver guidance. A critical yet largely overlooked component of these pipelines is the feature function that maps problem instances to inputs for machine learning models. Existing L2O methods typically rely on hand-crafted features, making representation design manual and largely fixed across domains. We introduce FunL2O, the first unified framework for automating feature design through LLM-driven program evolution for L2O. In a FunSearch-style loop, an LLM proposes executable feature functions, while a fixed evaluation process retrains the original L2O model and measures downstream optimization performance. We evaluate FunL2O on linear and quadratic programming tasks involving solution prediction and warm-starting, as well as on mixed-integer optimization tasks using GNN-guided backdoor branching and Predict-and-Search. Across continuous and discrete optimization tasks and four LLMs, the evolved features consistently outperform hand-crafted representations. These results establish LLM-driven feature evolution as a general and effective approach to automating representation design in L2O.

## Metadata
- **Published**: 2026-07-29T18:52:44Z
- **Authors**: Bingheng Li, Junyang Cai, Yupeng Zhang, Bistra Dilkina, Jayant Kalagnanam, Dzung T. Phan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27389v1)