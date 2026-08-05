---
title: EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners
url: http://arxiv.org/abs/2608.03206v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-47-26Z_EduClaw_Bench_ALong_HorizonBenchmarkforPedagogical.md
generated_at: 2026-08-05 01:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EduClaw-Bench, a benchmark that simulates a 30‑day tutoring relationship between an LLM agent and a learner whose knowledge is tracked by a knowledge tracing model. Evaluation of ten adapter configurations across three base models shows that tutoring quality emerges from the combination of both components rather than either alone, and no configuration maintains high performance over the full horizon.

## Key Takeaways
- The combined effect of the base LLM and the agent harness determines learning outcomes, indicating synergy is essential.  
- None of the tested combinations sustain good tutoring quality across all 55 scenarios for the entire 30‑day period.  
- Calibration metrics (ECE=0.049) and a live‑classroom study confirm that simulated learner progress aligns with real measurements.

## Context
Current AI education tools are often designed for isolated tasks, ignoring the long‑term dynamics of learning where knowledge accumulates over time. Benchmarks like EduClaw-Bench address this gap by modeling sustained interaction and probing both learning gain and pedagogical quality.

## Implications
For educators and developers, this work highlights the need to evaluate LLM tutors as integrated systems rather than isolated components. It also suggests that long‑term performance is challenging, prompting research into more robust curriculum design and adaptive agent strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03206v1)
