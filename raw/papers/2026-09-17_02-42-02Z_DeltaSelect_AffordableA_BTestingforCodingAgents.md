---
title: DeltaSelect: Affordable A/B Testing for Coding Agents
published: 2026-09-17T02:42:02Z
authors: Nicholas J. Conn
url: http://arxiv.org/abs/2609.19607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeltaSelect: Affordable A/B Testing for Coding Agents

## Abstract
Coding-agent benchmarks are built for broad and comprehensive comparisons, not frequent development decisions. Individual runs vary, full suites are expensive, and the benchmark harness may differ from the harness used in practice. In a resampling analysis of DeepSWE's published trials, only 19.5% of tasks (22 of 113) had a fifth-percentile Pearson correlation of at least 0.50 with full-benchmark performance. The paper presents DeltaSelect, an open-source method that identifies tasks whose one-run results consistently track full-benchmark performance using Pearson correlation, maps fractional verifier results to a common score using linear regression, and selects a fixed task set within a dollar budget. DeltaSelect is intended for repeated baseline-versus-candidate comparisons during development, not model rankings. In a gpt-5.6-luna low-reasoning case study, DeltaSelect was used to revise custom skills and instructions. Across 13 evaluations, the recorded cost was USD 27.86 at rates published August 16, 2026. The adopted version cost 58.1% less than the initial version (USD 1.75 versus USD 4.18; p=0.008), while the calibrated score was higher (42.36% versus 36.46%; published-analog variance p=0.326).

## Metadata
- **Published**: 2026-09-17T02:42:02Z
- **Authors**: Nicholas J. Conn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19607v1)