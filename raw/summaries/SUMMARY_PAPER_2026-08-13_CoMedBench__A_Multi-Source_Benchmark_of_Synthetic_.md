---
title: CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility
url: http://arxiv.org/abs/2608.12805v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_04-24-52Z_CoMedBench_AMulti_SourceBenchmarkofSyntheticMedica.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoMedBench, a benchmark that tests synthetic medical data generators across static and temporal ICU tasks using real datasets. It shows that state-of-the-art generators preserve most downstream performance, with AUROC ratios near 90% for tabular tasks and higher for temporal tasks.

## Key Takeaways
- The benchmark spans 37 dataset-task pairs covering both static tabular and temporal ICU time-series data from seven public sources.
- Synthetic training data retains a mean AUROC utility of about 90.6% compared to real data, with the best generator achieving up to 97.3% for tabular tasks.
- Temporal ICU tasks are more sensitive: CoMed-CTGAN drops to 81.6% AUROC and 64.0% AUPRC under imbalance-sensitive evaluation, while CoMed-TVAE maintains ~95% AUROC.

## Context
The need for synthetic data in healthcare AI is growing due to privacy constraints, but existing benchmarks lack comparability across generators and tasks. This work provides a unified framework that can guide developers on when synthetic data remains useful.

## Implications
Clinicians and researchers will benefit from clear performance metrics that distinguish generator quality, helping allocate resources to the most reliable tools. The benchmark also supports regulatory confidence in synthetic data use for model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12805v1)
