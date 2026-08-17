---
title: Coverage Aware Active Evaluation for Failure Discovery with Paired Systems
url: http://arxiv.org/abs/2608.13719v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_19-26-25Z_CoverageAwareActiveEvaluationforFailureDiscoverywi.md
generated_at: 2026-08-16 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an adaptive failure discovery method that uses proxy system evaluations together with a few target system results to select testing scenarios efficiently. By learning a local predictor of risk through residual modeling and combining it with a support-aware mutual information objective, the approach finds both likely and diverse failures. Experiments on autonomous driving, manipulation, and quadruped velocity‑tracking tasks show up to twice as many failures compared with random or active-learning baselines.

## Key Takeaways
- The method learns a local predictor of target risk by correcting proxy failure signals using control-variate-inspired residual modeling.
- It uses a support-aware mutual information objective that favors realistic, well-supported regions while expanding coverage across failure modes.
- Across three autonomous driving tasks the approach discovers up to two times as many failures as random sampling and active-learning baselines.

## Context
Failure discovery in complex systems is challenging because proxies such as simulators often fail to capture real-world behavior due to sim-to-real gaps. Current approaches either rely on expensive target testing or generate biased proxy results, limiting the diversity of discovered failures. This work addresses those limitations by integrating limited high-fidelity observations with cheap proxy data.

## Implications
The findings suggest that hybrid evaluation strategies can dramatically improve coverage without proportional cost increases, offering a practical path for safety-critical AI deployment. Practitioners can adopt this framework to prioritize testing where it matters most, reducing risk while uncovering hidden failure modes early in development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13719v1)
