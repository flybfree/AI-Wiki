---
title: SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing
published: 2026-07-26T19:59:48Z
authors: Shuyu Chen, Chen Zhu, Ye Zhang, Yang Li, Qiqi Xie, Haohan Wang
url: http://arxiv.org/abs/2607.23821v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing

## Abstract
Identifying therapeutic target genes from single-cell RNA sequencing (scRNA-seq) data remains a fundamental challenge in translational biology. Unlike bulk assays, scRNA-seq captures heterogeneous cellular states and rare subpopulations, but this same heterogeneity makes target discovery highly sensitive to analytical choices throughout the pipeline, including preprocessing, cell population selection, differential expression analysis, and downstream biological interpretation. As a result, existing workflows and general-purpose analysis agents often produce unstable or difficult-to-interpret target hypotheses, limiting their reliability for disease-focused discovery. We present SCTA (Single-Cell Target Agent), a decision-centric agentic framework for stable and interpretable target gene discovery from scRNA-seq data. Rather than treating analysis as a single general-purpose reasoning task, SCTA decomposes target discovery into specialized agents aligned with key decision points in the single-cell pipeline and constrains downstream reasoning with structured biological evidence. In a representative ablation study on hereditary chronic pancreatitis, we demonstrate that SCTA's full evidence integration yields the most stable target selection across independent runs among the tested configurations, while recovering biologically coherent, disease-relevant mechanisms validated in prior studies. These results suggest that decision-aware agent orchestration tailored to the structure of single-cell analysis can improve the robustness, interpretability, and practical utility of target discovery in precision medicine.

## Metadata
- **Published**: 2026-07-26T19:59:48Z
- **Authors**: Shuyu Chen, Chen Zhu, Ye Zhang, Yang Li, Qiqi Xie, Haohan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23821v1)