---
title: Physics-Informed Condition Monitoring of SiC Power Modules
published: 2026-08-08T23:20:52Z
authors: Mattia Scarpa, Evgeny Kusmenko, Francesco Toso, Mattia Bruschetta, Ruggero Carli, Simon Achatz
url: http://arxiv.org/abs/2608.08363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Informed Condition Monitoring of SiC Power Modules

## Abstract
Silicon carbide (SiC) power modules are increasingly deployed in automotive traction inverters, where condition monitoring is essential to prevent in-service failures. Despite extensive qualification under AQG 324, no consolidated approach exists for in-field health state estimation: physics-of-failure lifetime models lack real-time applicability, purely data-driven architectures require large labeled datasets and generalize poorly, and physics-informed frameworks remain too demanding for embedded deployment.   We address SiC MOSFET modules assembled with sintered packaging, which suppresses solder degradation and produces aging behavior distinct from previously studied devices. Instead of the smooth quasi-exponential drift of solder-based modules, the forward voltage drop $V_{DS}$ exhibits multi-regime profiles, with wirebond liftoff events introducing abrupt, non-monotonic perturbations.   We propose a condition monitoring framework combining three elements. First, physics-informed features replace raw sensor signals with cumulative damage indicators derived from junction temperature swing, mean junction temperature and a Miner rule accumulator, encoding degradation history in an interpretable form. Second, a monotonicity constraint enforced by gradient penalty regularization embeds the expected degradation direction as a physics-guided prior. Third, a heavy-tailed output distribution replaces the point estimate, giving calibrated uncertainty robust to the out-of-distribution variance introduced by liftoff.   On an industrial power cycling dataset from Infineon Technologies, several neural architectures are compared under a strict cross-validation protocol. The full configuration reduces mean absolute error by approximately 70% over purely data-driven baselines and stays stable across all folds, while remaining lightweight enough for embedded deployment.

## Metadata
- **Published**: 2026-08-08T23:20:52Z
- **Authors**: Mattia Scarpa, Evgeny Kusmenko, Francesco Toso, Mattia Bruschetta, Ruggero Carli, Simon Achatz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08363v1)