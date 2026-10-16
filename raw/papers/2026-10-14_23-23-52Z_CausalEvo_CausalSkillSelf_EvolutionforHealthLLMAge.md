---
title: CausalEvo: Causal Skill Self-Evolution for Health LLM Agents
published: 2026-10-14T23:23:52Z
authors: Yuchen Zhang
url: http://arxiv.org/abs/2610.21016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CausalEvo: Causal Skill Self-Evolution for Health LLM Agents

## Abstract
Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty generalizations propagate errors. We propose CausalEvo, a method for causal skill self-evolution that estimates the relative effects of deliberately changed skill sets while holding the model weights, feedback cases, and rule count fixed. At each evolution step, a frozen LLM proposes candidate rules, which are pooled with the incumbent skills so that the current skill set remains a feasible choice. Paired skill replacements against shared background rules are scored on the same feedback cases; least squares converts the score differences into relative skill values, and the top-ranked rules are retained, favoring incumbents on ties. A decision-loss bound separates candidate support, approximation, and estimation errors. On six MedCalc-Bench-Verified tasks with 120 held-out cases, CausalEvo achieves 60.00% accuracy, compared with 55.83% for SkillOpt and 51.67% without skills. Across the recorded training configurations, which use different optimization budgets, it consumes 55.6% fewer training tokens than SkillOpt. Gains concentrate in particular calculations alongside regressions on others, and paired accuracy intervals include zero. CausalEvo turns task feedback into controlled decisions about skill retention and replacement. Project repository: https://github.com/txbrook/CausalEvo

## Metadata
- **Published**: 2026-10-14T23:23:52Z
- **Authors**: Yuchen Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21016v1)