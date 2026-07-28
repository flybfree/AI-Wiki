---
title: NeurGO: Learning to Generate Elite Candidates for Meta-Black-Box Expensive Optimization
published: 2026-07-26T01:47:10Z
authors: Jintao He, Huixiang Zhen, Wenyin Gong
url: http://arxiv.org/abs/2607.23408v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeurGO: Learning to Generate Elite Candidates for Meta-Black-Box Expensive Optimization

## Abstract
Expensive black-box optimization is ubiquitous in science and engineering, where function evaluations are costly and the evaluation budget is limited. Traditional evolutionary algorithms and Meta-BlackBox Optimization (MetaBBO) approaches typically consume most evaluations on candidate selection, often wasting precious budget on inferior solutions. Although surrogate-assisted evolution and Bayesian optimization aim to reduce evaluations through surrogate models, constructing an accurate global model from limited data remains challenging, and model bias can easily trap the search in local optima. To overcome these limitations, we propose NeurGO, a generative MetaBBO framework that directly synthesizes elite candidates from historical population states. Specifically, we employ an attention-based encoder to capture the population-level search trend and condition a decoder on this representation to generate high-quality candidates, avoiding the expensive evaluation of large offspring pools. We then design a quality-diversity loss to maintain solution quality and population diversity throughout the search. Through extensive benchmarking on CEC 2008 and the COCO BBOB test suites, our method achieves better optimization performance under the same evaluation budget and exhibits faster convergence.

## Metadata
- **Published**: 2026-07-26T01:47:10Z
- **Authors**: Jintao He, Huixiang Zhen, Wenyin Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23408v1)