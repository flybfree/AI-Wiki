---
title: Mitigating Over-Optimization in PRM-Guided Search in Mathematical Reasoning by Optimizing the Guide
published: 2026-08-30T21:25:03Z
authors: Taejong Joo, Diego Klabjan
url: http://arxiv.org/abs/2608.30051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mitigating Over-Optimization in PRM-Guided Search in Mathematical Reasoning by Optimizing the Guide

## Abstract
Process reward models (PRMs) provide dense step-level guidance for search-based reasoning, enabling inference-time compute to be allocated toward promising partial solutions. However, recent evidence suggests that PRM-guided search can over-optimize imperfect process rewards, pruning viable trajectories while expanding spurious ones. In this work, we theoretically show that directly leveraging PRM score is vulnerable to verifier noise through an extreme-value effect: non-viable prefixes become more likely to receive spuriously high scores as reasoning depth increase. Therefore, we formulate the PRM-guided search as a robust optimization problem over plausible reward perturbations, termed maximin PRM-guided search, leading to a training-free robust process supervision method that preserves promising alternatives when step-level scores are noisy. Maximin PRM-guided search mitigates this failure mode by reducing sensitivity to over-optimized PRM outliers. Without fine-tuning or online adaptation, maximin search consistently improves the PRM-guided search by 17-35\% on average, outperforming outcome- and step-level baselines in 14 out of 16 settings. Our source code is available at https://github.com/tjoo512/maximin-search.

## Metadata
- **Published**: 2026-08-30T21:25:03Z
- **Authors**: Taejong Joo, Diego Klabjan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30051v1)