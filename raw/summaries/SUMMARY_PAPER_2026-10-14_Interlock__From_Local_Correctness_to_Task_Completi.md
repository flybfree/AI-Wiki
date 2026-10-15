---
title: Interlock: From Local Correctness to Task Completion in Long-Horizon Agents
url: http://arxiv.org/abs/2610.19686v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_07-09-46Z_Interlock_FromLocalCorrectnesstoTaskCompletioninLo.md
generated_at: 2026-10-14 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Interlock, a framework designed to close the gap between local correctness and full task completion in long-horizon LLM agents operating in complex, fragmented environments. The authors represent tasks as typed completion graphs encoding relationships among evidence, decisions, and downstream effects, then synthesize these into trainable agent trajectories. Fine-tuning Qwen3.6 backbones on Interlock-generated accepted trajectories yields measurable improvements across three external benchmarks, demonstrating that structured task synthesis can meaningfully enhance agent training utility.

## Key Takeaways
- Interlock models each task as a typed completion graph with three distinct edge types: grounding edges link public evidence to decisions, coupling hyperedges enforce joint constraints across components, and realization edges connect decisions to all required downstream effects. This structure explicitly encodes the relational dependencies that cause agents to produce locally correct but globally incomplete outputs.
- The framework includes a dual-review quality gate: a source-coverage review verifies that original requirements survive the generation process, while a public-input review ensures the evaluation rubric is actually supported by materials available to the solver. An agent-as-judge then inspects execution artifacts and runs verification scripts, retaining only trajectories that satisfy all mandatory requirements, filtering out superficially plausible but incomplete solutions.
- Training on Interlock-synthesized trajectories produces consistent gains across three distinct benchmarks: AutomationBench pass rates improve by 4.00–4.50 percentage points, JobBench weighted scores increase by 3.20–6.64 points, and Harvey LAB criterion pass rates rise by 3.89–4.16 percentage points across two Qwen3.6 backbone variants, confirming that the synthesized experience transfers to external task environments.

## Context
Long-horizon agentic tasks in software automation, professional services, and legal workflows involve fragmented evidence, partially completed states, and cross-resource dependencies that current agent architectures handle poorly. Most existing training pipelines optimize for individual step correctness without enforcing the relational structure that binds steps into a coherent whole. Interlock addresses this structural blind spot by formalizing task completion as a graph problem, offering a principled method for generating high-quality training data that encodes inter-step dependencies rather than isolated actions.

## Implications
For practitioners building agentic systems in enterprise automation, legal research, or professional services, Interlock provides a reproducible recipe for synthesizing training data that teaches models to maintain cross-step consistency rather than merely executing isolated subtasks correctly. The approach suggests that future agent training pipelines should incorporate structured relational representations and multi-stage verification gates, shifting the field from step-level optimization toward holistic task-completion guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19686v1)
