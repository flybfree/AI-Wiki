---
title: MeanField Surrogate Modeling for Scalable Runtime Scheduling of Concurrent Heterogeneous AI Inference on Shared GPUs
url: http://arxiv.org/abs/2609.02109v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-52-22Z_MeanFieldSurrogateModelingforScalableRuntimeSchedu.md
generated_at: 2026-09-02 20:54
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a MeanField surrogate model that predicts the performance of individual AI models running concurrently on a shared GPU without requiring exhaustive joint profiling. Experiments demonstrate high predictive accuracy and that the required sample budget grows linearly with the number of concurrent models, unlike combinatorial full profiling. The surrogate is integrated into a genetic algorithm scheduler, enabling scalable runtime decisions.

## Key Takeaways
- The MeanField surrogate predicts per‑model performance using only local configuration and aggregate GPU state, avoiding explicit modeling of all joint interactions.
- Experimental results show predictive accuracy of about 0.96 (R² ≈ 0.96) with a sample budget that scales linearly in N, contrasting sharply with the exponential cost of full joint profiling.
- Integrated into a genetic algorithm scheduler, the surrogate handles up to five concurrent models with 78,732 feasible configurations while remaining within 0.10% of exhaustive search and achieving zero SLA violations across eight dynamic workloads.

## Context
Concurrent execution of heterogeneous AI models on shared GPUs is common in data‑center environments where latency and resource constraints are critical. Traditional profiling approaches that enumerate every possible joint configuration become intractable as the number of co‑running models increases, limiting real‑time scheduling capabilities.

## Implications
This work provides a practical path to scalable runtime scheduling for AI workloads, reducing computational overhead without sacrificing accuracy. Practitioners can adopt MeanField surrogates to design efficient schedulers that handle complex, dynamic AI pipelines on limited GPU resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02109v1)
