---
title: Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks
url: http://arxiv.org/abs/2610.17609v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_02-29-40Z_Verifier_HarnessCo_EvolutionforTraining_FreeSelf_I.md
generated_at: 2026-10-14 00:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Unified Co-Evolution (UCoE), a training-free method that simultaneously evolves an executable verifier program and an agent's harness state without updating any model parameters. The core innovation is a mechanism where candidate verifier programs are synthesized, tested against "response contrasts" (paired responses differing in one declared property), and selected based on a metric called "driving capacity" that measures discrimination on the weakest contrast family. Across six open-ended benchmarks, UCoE achieves 59.00% preference over direct generation with Qwen3-8B and 57.19% with Qwen3.8-27B, representing margins of 9.00 and 7.19 percentage points respectively.

## Key Takeaways
- UCoE addresses a fundamental failure mode in training-free self-improvement: static model-based verifiers become stale as agent responses improve and task demands shift, while incorrect verifier feedback can degrade responses and propagate misleading experience across a task stream. By co-evolving the verifier alongside the harness state, the system maintains alignment between evaluation criteria and the agent's evolving capabilities.
- The method uses "response contrasts"—pairs of responses that differ in one declared property with a known preferred side—as the testing substrate for candidate verifier programs. The selection criterion, "driving capacity," prioritizes the candidate that performs best on its weakest contrast family, ensuring robust discrimination rather than overfitting to easy cases. The selected verifier then diagnoses one weakness per draft, guides a single repair, and gates whether accepted repairs enter the persistent harness state.
- Task completion diagnostics seed new candidate verifiers that must outperform the current verifier on the same contrasts before adoption, creating a principled evolutionary loop. On verifiable benchmarks, the same method raises mean performance from 36.06% to 38.48%, demonstrating transferability beyond preference-based evaluation.

## Context
This work sits at the intersection of agent self-improvement, program synthesis, and open-ended evaluation—three areas where current approaches rely heavily on supervised fine-tuning or fixed reward models. As large language models are increasingly deployed as autonomous agents handling creative writing, planning, and multi-step reasoning tasks where no ground-truth answer exists, the quality of the feedback loop becomes the bottleneck. UCoE contributes a principled alternative to static verifiers by treating evaluation as a co-evolving artifact rather than a fixed oracle, aligning with broader trends in evolutionary computation and self-play methods applied to language agents.

## Implications
For practitioners building agentic systems on open-ended tasks, UCoE offers a path to continuous self-improvement without the computational cost of model fine-tuning, making it accessible for teams that cannot retrain large models after every deployment. The co-evolutionary design suggests that evaluation infrastructure should be treated as a first-class, updatable component of agent systems rather than a static dependency, which has practical implications for production agent pipelines, safety monitoring, and the design of benchmark suites that must adapt as model capabilities advance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17609v1)
