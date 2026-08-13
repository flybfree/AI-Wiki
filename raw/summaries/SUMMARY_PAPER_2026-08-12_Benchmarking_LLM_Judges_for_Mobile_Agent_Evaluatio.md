---
title: Benchmarking LLM Judges for Mobile Agent Evaluation
url: http://arxiv.org/abs/2608.11434v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_21-00-46Z_BenchmarkingLLMJudgesforMobileAgentEvaluation.md
generated_at: 2026-08-12 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MobileJudgeBench, a systematic benchmark for evaluating LLM‑based judges on mobile agent trajectories, and finds that simple baseline methods often outperform elaborate pipelines. Experiments across nine hundred human‑annotated trajectories reveal three main findings: a basic judge with sampled screenshots competes well or exceeds purpose‑built approaches; quality metrics reliably predict real‑world utility both in ranking fidelity and as reward signals for reinforcement learning; and two LLM backbones exhibit qualitatively opposite failure patterns linked to their precision‑recall trade‑offs.

## Key Takeaways
- A simple baseline judge that samples screenshots is competitive with or exceeds more complex pipelines, suggesting that elaborate judge designs do not always improve quality. 
- Benchmark metrics such as ranking fidelity and downstream RL performance correlate strongly with real‑world usefulness of LLM judges, indicating they are good predictors of utility. 
- Two different LLM backbones fail in opposite ways—one is overly conservative while the other is permissive—highlighting that backbone precision‑recall characteristics shape judge behavior.

## Context
Mobile agents rely on automated evaluation to guide learning and deployment, yet most benchmarks assume judges are reliable. This work challenges that assumption by exposing how model choices affect performance, providing a more honest view of LLM usefulness in mobile AI systems.

## Implications
For practitioners building mobile AI agents, the findings suggest focusing on simple, well‑designed evaluation pipelines rather than overcomplicating them with multiple stages. It also underscores the need to monitor judge behavior across different model backbones to avoid hidden biases that could degrade agent learning or user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11434v1)
