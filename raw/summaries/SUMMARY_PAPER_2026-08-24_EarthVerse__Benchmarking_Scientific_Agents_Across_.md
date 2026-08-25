---
title: EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards
url: http://arxiv.org/abs/2608.23525v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_17-29-16Z_EarthVerse_BenchmarkingScientificAgentsAcrossDynam.md
generated_at: 2026-08-24 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EarthVerse, a benchmark for evaluating scientific agents in dynamic Earth‑system analysis and natural hazard studies. Across 405 reproducible tasks, the best model achieved an average answer‑unit accuracy of 84.65%, while the highest strict evaluation at 95% was only 34.81%, highlighting persistent gaps in evidence handling and reasoning.

## Key Takeaways
- The benchmark reveals that agents often perform individual steps correctly but fail to maintain a coherent chain across evidence, scales, units, calculations, and physical interpretation.
- The discrepancy between mean accuracy (84.65%) and strict evaluation (34.81%) underscores the importance of end‑to‑end scientific reliability rather than isolated task success.
- EarthVerse provides reproducible ground truth with fine‑grained answer units and rubrics that allow multiple valid research pathways.

## Context
Earth‑system modeling requires agents to integrate heterogeneous observational data, reconcile differing scales, and produce physically meaningful results. Current AI systems frequently treat each step in isolation, leading to unreliable scientific conclusions. This paper contributes a structured evaluation framework that captures these complexities.

## Implications
For researchers developing Earth‑system simulation tools, EarthVerse offers a reliable metric to gauge whether agents can handle real‑world data integration challenges. Practitioners can use the benchmark to prioritize improvements in evidence access and reasoning before deploying models for hazard forecasting or climate analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23525v1)
