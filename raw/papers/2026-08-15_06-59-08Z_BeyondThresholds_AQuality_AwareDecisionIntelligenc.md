---
title: Beyond Thresholds: A Quality-Aware Decision Intelligence Framework for Cold Chain IoT Systems
published: 2026-08-15T06:59:08Z
authors: Aashna Sofat, Balwinder Sodhi
url: http://arxiv.org/abs/2608.15082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Thresholds: A Quality-Aware Decision Intelligence Framework for Cold Chain IoT Systems

## Abstract
Cold chain logistics has advanced technologically, yet most deployed systems remain reactive monitors, not decision-making agents: thresholds trigger alerts, but nothing relates violations to cumulative product degradation or converts degradation signals into logistics decisions. We address this gap with a Quality-Aware Decision Intelligence (QADI) framework combining three capabilities: a structured quality state representation, $S_q = [L, Q, U, R]$ -- remaining shelf life, degradation rate, estimation uncertainty, and operational risk, all derived and computable from the framework equations; a hybrid quality modeling layer combining physics-based microbial kinetics with a data-driven correction term; and a reasoning layer built on Microsoft Phi-4~\cite{Phi4} with retrieval-augmented generation over a structured domain knowledge base.   We benchmark against five baselines -- threshold monitoring, physics-only, physics-plus-noise, optimisation-based decisions, and a rule-based expert system -- across eight cold chain scenarios, using pasteurised milk as the primary case, with ground truth shelf-life drawn from published dairy studies~\cite{Singh1994, Smigic2015} independent of our model. Comparisons use Wilcoxon signed-rank tests with Holm correction. Across milk and broccoli scenarios, the framework attains mean absolute shelf-life error of 7.2 hours (versus 30.9 hours, physics-only; $p<0.001$), spoilage rate of 14.5% (versus 16.6%, physics-only and rule-based; p=0.08), and oracle-optimal decisions in 99.5% of scenarios. Removing the LLM reasoning component drops optimality to 45.5% ($p<0.001$). Expert-rated explanation quality reaches 83% ($κ= 0.71$). Ablations show hybrid modeling and LLM reasoning contribute distinct gains, while RAG retrieval mainly drives explanation quality. Code: https://bit.ly/4d6t44C.

## Metadata
- **Published**: 2026-08-15T06:59:08Z
- **Authors**: Aashna Sofat, Balwinder Sodhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15082v1)