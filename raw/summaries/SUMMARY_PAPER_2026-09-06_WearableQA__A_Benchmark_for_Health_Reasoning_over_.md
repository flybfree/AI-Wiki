---
title: WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
url: http://arxiv.org/abs/2609.05405v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_17-52-37Z_WearableQA_ABenchmarkforHealthReasoningoverReal_Wo.md
generated_at: 2026-09-06 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces WearableQA, a benchmark that tests AI reasoning on real wearable data collected from 200 users over up to 500 days of daily measurements. It evaluates both computation over longitudinal measurements and physiological interpretation through multiple question types.

## Key Takeaways
- The dataset includes 4,084 questions derived from 500‑day daily measurements of 200 real users, preserving device noise and inter‑individual variability.  
- Evaluation shows models range from 19.6% to 72.9% accuracy versus a 10% chance baseline, yet most stay below 60%, indicating the task remains unsolved.  
- WearableQA distinguishes reasoning axes: data vs health and single‑vs cross‑signal, enabling assessment of both computation and integration abilities.

## Context
Real‑world wearable monitoring generates massive longitudinal signals that challenge AI systems to extract meaningful insights. Current benchmarks often lack realistic noise and variability, limiting their diagnostic value.

## Implications
This benchmark forces developers to prioritize robustness over raw performance metrics. It guides research toward models capable of reasoning across heterogeneous signals in authentic user contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05405v1)
