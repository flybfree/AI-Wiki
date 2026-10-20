---
title: EvoSkill v2: Fully Agentic Skill Evolution from Benchmark Adaptation to a Stateful Evolver
url: http://arxiv.org/abs/2610.25931v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_07-29-21Z_EvoSkillv2_FullyAgenticSkillEvolutionfromBenchmark.md
generated_at: 2026-10-19 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EvoSkill v2 introduces a three-agent architecture—comprising a benchmark adaptor, a solver, and a stateful evolver—that iteratively rewrites the instructions (skills) an agent receives without altering its underlying model or evaluation harness. The system demonstrates that a persistent, tool-equipped coding agent can outperform prior skill-optimization methods by 7.7 percentage points on SpreadsheetBench v2 and 5.4 points on τ³-bench banking, while also enabling a weaker model like Claude Haiku 5.5 to improve its own skills by up to 21.5 percentage points.

## Key Takeaways
- The evolver is implemented as a single stateful coding agent with a bash tool spanning the entire training run, contrasting sharply with SkillOpt's sequence of isolated model calls and SkillBoost's fresh-start-per-round design. This persistent state allows the evolver to accumulate context across epochs, reducing redundant exploration and enabling more coherent skill rewrites over time.
- The authors explicitly measure inter-attempt variance in the solver's rollouts, provide the evolver multiple attempts per training task, and accept every epoch's generated skills rather than selecting among candidates on noisy validation scores. This design choice mitigates the instability caused by stochastic solver behavior and prevents the optimizer from overfitting to high-variance score signals.
- EvoSkill v2 achieves a lower cost per percentage point of held-out pass-rate improvement than either SkillOpt or SkillBoost across both benchmarks and both feedback settings, and it demonstrates self-improvement capability: when Claude Haiku 5.5 serves as both solver and evolver, the system still yields gains of up to 21.5 percentage points on the τ³-bench banking task, showing that skill evolution does not require a stronger model to supervise a weaker one.

## Context
This work sits at the intersection of automated prompt optimization, agentic tool use, and self-improving AI systems. Prior methods such as SkillOpt and SkillBoost treat skill editing as a stateless or semi-stateless procedure, which limits their ability to build on accumulated insight across training iterations. By reframing the optimizer as a persistent coding agent with shell access, EvoSkill v2 aligns skill evolution with the broader trend toward long-horizon, tool-augmented agents, and it provides a concrete benchmark for comparing optimizer architectures on realistic task suites like SpreadsheetBench v2 and τ³-bench.

## Implications
For practitioners deploying agents on domain-specific benchmarks, EvoSkill v2 offers a cheaper and more stable path to improving task performance without retraining or swapping the base model, which is particularly valuable in cost-sensitive production environments. The demonstration that a smaller model can bootstrap its own skill improvements suggests a scalable recipe for self-improving agent pipelines in enterprise settings, where access to frontier models may be restricted by budget or compliance constraints. The cost-efficiency findings also signal that stateful, tool-equipped optimizers could become the default architecture for future automated skill-tuning frameworks, shifting the field away from single-shot prompt-editing heuristics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25931v1)
