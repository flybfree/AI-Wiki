---
title: Harness Evolution Hits a Ceiling: When Weight Training Should Begin
url: http://arxiv.org/abs/2610.11655v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_10-33-29Z_HarnessEvolutionHitsaCeiling_WhenWeightTrainingSho.md
generated_at: 2026-10-08 21:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the boundary between evolving a runtime harness around a frozen LLM and training the model's weights to improve long-horizon agent performance. The authors introduce a failure-composition diagnostic that separates process failures (blocked calls, loops, exhausted step budgets) from content failures (poor delivered plans), establishing that harness evolution repairs the former while weight training addresses the latter. Through experiments on DeepPlanning and WebArena-Lite across eight models from six families, they demonstrate that LoRA adapters trained on evolved-harness trajectories can internalize harness gains, effectively doubling held-out scores for smaller models and matching full evolution performance for larger ones.

## Key Takeaways
- The paper proposes a diagnose-then-intervene rule: by labeling failed trajectories by the first signal that fires, practitioners can determine whether a failure is a process failure (which harness evolution can repair) or a content failure (which requires weight training). This compositional analysis provides a principled decision framework rather than a trial-and-error approach to agent improvement.
- On DeepPlanning, a self-evolving harness loop lifts Qwen3.5-4B from 0.16 to 0.30 and Qwen3.5-9B from 0.32 to 0.44, with held-out delivery for the 4B model rising from 55% to 90%. LoRA adapters trained on evolved-harness trajectories add +0.13 on held-out tasks for both model sizes, and on 4B they stack with the harness to more than double the held-out score, while on 9B the adapter alone matches the full evolution line, reducing content failures from a quarter of trajectories to one in twenty.
- The method transfers to WebArena-Lite with a +0.09 gain on 117 unseen tasks, but notably the gain lives in what the model sees at runtime rather than in adapter weights, indicating that harness improvements do not always transfer into trainable parameters. A placebo adapter trained on answer-shuffled trajectories falls below the base model, confirming that the training signal must be genuine to produce gains.

## Context
This work sits at the intersection of two active research threads in LLM agent development: automated harness or scaffolding evolution (modifying prompts, tool-use patterns, and orchestration logic around a frozen model) and parameter-efficient fine-tuning such as LoRA. Prior work has treated these as separate improvement strategies without establishing when each is appropriate. By formalizing failure composition as a diagnostic tool, this paper provides a structured methodology for practitioners to allocate improvement effort between runtime engineering and model training, which is a practical gap in the current agent-building literature.

## Implications
For practitioners building agentic systems, this paper offers a concrete decision procedure: audit failure trajectories to classify them as process or content failures, apply harness evolution to the former, and reserve weight training for the latter. This can reduce wasted compute by avoiding fine-tuning models to fix orchestration bugs, and conversely avoids over-engineering harnesses when the model genuinely lacks planning competence. For the broader field, the finding that harness gains can be partially internalized into adapters but not always (as shown on WebArena-Lite) suggests that the boundary between runtime scaffolding and model capability is model-size-dependent, which has direct consequences for how organizations invest in agent infrastructure versus model training budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11655v1)
