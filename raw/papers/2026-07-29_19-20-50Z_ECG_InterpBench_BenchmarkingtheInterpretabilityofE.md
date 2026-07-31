---
title: ECG-InterpBench: Benchmarking the Interpretability of ECG Foundation Models with Matched-Scale Sparse Autoencoders
published: 2026-07-29T19:20:50Z
authors: Yixuan Duan, Wei Qiu
url: http://arxiv.org/abs/2607.27404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECG-InterpBench: Benchmarking the Interpretability of ECG Foundation Models with Matched-Scale Sparse Autoencoders

## Abstract
Existing benchmarks for electrocardiogram foundation models primarily evaluate downstream predictive performance, providing limited insight into whether their internal representations can be faithfully decomposed, clinically interpreted, or reproduced across independent analyses. We introduce ECG-InterpBench, a benchmark designed to systematically evaluate the interpretability of ECG foundation-model representations. ECG-InterpBench uses sparse autoencoders as standardized measurement instruments and matches their capacity across models to enable controlled comparisons. We evaluate six frozen ECG foundation models across five standardized encoder depths, five matched dictionary widths, and three random seeds, producing a 450-cell interpretability atlas comprising 75 exactly matched six-model comparison blocks. The benchmark evaluates complementary dimensions of representation interpretability, including sparse reconstruction fidelity, single-feature accessibility and coverage of 49 clinically meaningful ECG measurements, and cross-seed feature reproducibility. The evaluation further quantifies patient-sampling uncertainty, depth- and seed-dependent variation, and sensitivity to the sparsity parameterization. The benchmark reveals that ECG foundation models exhibit distinct interpretability profiles. A matched replication on MIMIC-IV-ECG confirms that reconstruction fidelity and clinical accessibility identify different leading models. The benchmark is accompanied by executable evaluation code, standardized manifests, cell-level metrics, and reproducibility audits. ECG-InterpBench complements performance-centered ECG benchmarks by providing a capacity-controlled and reproducible framework for comparing ECG foundation models across distinct dimensions of representation interpretability.

## Metadata
- **Published**: 2026-07-29T19:20:50Z
- **Authors**: Yixuan Duan, Wei Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27404v1)