---
title: BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells
published: 2026-08-06T11:58:29Z
authors: Yuhao Wang, Zelin Zang, Yuxuan Liu, Zhen Lei, Stan Z. Li
url: http://arxiv.org/abs/2608.05928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells

## Abstract
Single-cell transcriptomes are sparse observations of coordinated biological programmes, yet most self-supervised models learn by reconstructing individual genes. Here we present BioM-JEPA, a joint-embedding predictive architecture that instead predicts aggregate representations of graph-connected gene blocks defined by protein-association and corpus-derived coexpression evidence. A student network infers each target-block representation from the remaining genes in a cell, while a slowly updated teacher supplies the corresponding target from the full observed gene set. Under the reported extraction procedure, block-level prediction produced embeddings with higher effective rank and weaker association with detected-gene depth in the tested diagnostics than token-prediction, random-block and reconstruction controls. Across CellBench tasks, frozen BioM-JEPA embeddings retained expression, pathway and neighbourhood information and achieved the lowest aggregate perturbation-response error among the evaluated models. Representation diagnostics were also consistent with canonical pancreatic programmes and compositional relationships between genetic perturbations. Linear attention avoids constructing a quadratic gene-by-gene attention matrix; in a matched one-epoch hPancreas experiment at batch size 8, BioM-JEPA provided 5.75-fold higher fine-tuning throughput and 3.76-fold higher held-out embedding throughput than scFoundation. Together, these results support graph-connected gene blocks as useful prediction units for JEPA-style representation learning in single-cell biology.

## Metadata
- **Published**: 2026-08-06T11:58:29Z
- **Authors**: Yuhao Wang, Zelin Zang, Yuxuan Liu, Zhen Lei, Stan Z. Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05928v1)