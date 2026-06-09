---
title: Picid: A Modular Evaluation Infrastructure for Reproducible PHM Across Tasks and Domains
published: 2026-05-27T11:50:52Z
authors: Lev Telyatnikov, Raffael Theiler, Leandro Von Krannichfeldt, Olga Fink
url: http://arxiv.org/abs/2605.28345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Picid: A Modular Evaluation Infrastructure for Reproducible PHM Across Tasks and Domains

## Abstract
Progress in Prognostics and Health Management (PHM) is hindered by the lack of standardized and reusable evaluation practices across tasks, datasets, and application domains. Reported results are often difficult to reproduce and compare, as key protocol choices, such as data splits, preprocessing, label alignment, temporal windowing, and metrics, are often implicit or implemented ad hoc. We introduce \picid, a modular evaluation infrastructure that formalizes the PHM evaluation pipeline as an explicit, executable, and reproducible protocol. Through well-defined abstractions, \picid enforces deterministic, leakage-safe dataset construction while remaining flexible across diverse PHM settings. The framework supports fault detection, diagnostics, and prognostics through a unified interface and can be extended to new datasets and model classes without violating protocol invariants. By standardizing data contracts and evaluation boundaries, \picid also enables fair cross-task comparisons across diagnostics (classification) and prognostics (regression), allowing identical model families to be evaluated consistently across heterogeneous settings. We demonstrate \picid through an empirical evaluation of thirteen models on twelve datasets spanning batteries, bearings, turbofan engines, hydraulics, filtration systems, and buildings. This work establishes a reusable foundation for standardized, fair and reproducible evaluation in PHM.

## Metadata
- **Published**: 2026-05-27T11:50:52Z
- **Authors**: Lev Telyatnikov, Raffael Theiler, Leandro Von Krannichfeldt, Olga Fink
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28345v1)