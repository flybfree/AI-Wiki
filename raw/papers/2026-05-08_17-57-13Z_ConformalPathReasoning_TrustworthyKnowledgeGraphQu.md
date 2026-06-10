---
title: 'Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration'
published: 2026-05-08T17:57:13Z
authors: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
url: http://arxiv.org/abs/2605.08077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration

## Abstract
Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.

## Metadata
- **Published**: 2026-05-08T17:57:13Z
- **Authors**: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.08077v1)