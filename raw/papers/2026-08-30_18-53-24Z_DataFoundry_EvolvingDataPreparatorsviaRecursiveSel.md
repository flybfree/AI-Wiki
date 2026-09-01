---
title: DataFoundry: Evolving Data Preparators via Recursive Self-Improvement
published: 2026-08-30T18:53:24Z
authors: Cehao Yang, Xiaojun Wu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Hui Xiong, Jian Guo
url: http://arxiv.org/abs/2608.29966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DataFoundry: Evolving Data Preparators via Recursive Self-Improvement

## Abstract
Domain adaptation of large language models increasingly depends on constructing high-quality training data, yet existing data-preparation pipelines typically address quality only after generation through post-hoc filtering. This creates a fundamental mismatch: data-quality issues often originate from the construction process itself, while quality control is applied only to its outputs. We introduce \textsc{DataFoundry}, a framework for \textbf{evolving data preparators through recursive self-improvement} before large-scale data production. \textsc{DataFoundry} represents a data preparator as an evolvable runtime specification and instantiates its evolution with a \textsc{Skills-as-Modules} architecture, in which a central \textsc{Controller} orchestrates modular skills to compile executable runtimes, diagnose deficiencies on small pilot sets using domain-appropriate criteria, and translate diagnostic feedback into adapters that revise individual preparation components while preserving stable interfaces. We evaluate \textsc{DataFoundry} on DataPrep-Bench across mathematics, finance, law, and medicine, and find that recursively evolved preparators produce training data with higher downstream utility than baselines. Experiments across different backbones further demonstrate that these improvements are not tied to a particular model, while analyses and case studies further reveal the framework's optimization dynamics and illustrate how its evolution unfolds in practice.

## Metadata
- **Published**: 2026-08-30T18:53:24Z
- **Authors**: Cehao Yang, Xiaojun Wu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Hui Xiong, Jian Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29966v1)