---
title: cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents
url: http://arxiv.org/abs/2609.40284v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_17-48-06Z_cua_speedrun_StandardizedBenchmarkingoftheSpeedofC.md
generated_at: 2026-09-30 21:56
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces cua-speedrun, a standardized benchmarking framework designed to address the reproducibility crisis in evaluating computer-use agents by providing uniform infrastructure and execution pipelines. The authors evaluate speed, efficiency, and cost across four CUA benchmarks, revealing that no single model family dominates all metrics and that counterintuitive dynamics exist, such as increased reasoning effort sometimes accelerating task completion or faster environment I/O potentially slowing overall performance. Additionally, the study demonstrates that evaluation task sets can be significantly reduced without losing statistical power, enabling more efficient benchmarking for the development of fast and cost-effective CUAs.

## Key Takeaways
- cua-speedrun establishes a reproducible benchmarking standard by implementing a uniform virtual machine configuration, a consistent execution pipeline, and a common agent interface that allows seamless operation across different benchmarks, thereby eliminating infrastructure variability that previously confounded speed evaluations.
- Empirical analysis reveals that no single model family is universally optimal for balancing performance, speed, and cost; notably, open-weight models lag behind frontier capabilities, and counterintuitive effects emerge where increased reasoning effort may accelerate task completion or optimized environment input-output latency can paradoxically increase overall execution time.
- The framework demonstrates that the evaluation task sets for most CUA benchmarks can be effectively reduced while maintaining statistical power, facilitating more efficient and scalable benchmarking processes to accelerate progress toward fast, deployable agents.

## Context
As computer-use agents increasingly demonstrate superhuman capabilities on complex GUI-based tasks, the field faces a critical bottleneck where deployment is hindered by prohibitive latency and operational costs rather than functional competence. Current evaluation methods suffer from significant reproducibility issues due to heterogeneous infrastructure setups, making it difficult to isolate agent performance from environmental noise or compare speed improvements reliably across different research efforts.

## Implications
By providing

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40284v1)
