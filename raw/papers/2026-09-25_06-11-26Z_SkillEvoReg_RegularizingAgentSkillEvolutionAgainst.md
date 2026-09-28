---
title: SkillEvoReg: Regularizing Agent Skill Evolution Against Overfitting
published: 2026-09-25T06:11:26Z
authors: Guanyu Nie, Fangzhou Zhu, Shixiong Kai, Xiongwei Han, Tao Zhong, Mingxuan Yuan
url: http://arxiv.org/abs/2609.30861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillEvoReg: Regularizing Agent Skill Evolution Against Overfitting

## Abstract
Language-model agents increasingly improve by converting execution experience into reusable external skills. Yet repeated skill updates form a learning process of their own: locally useful edits can accumulate into redundant or task-specific instructions, while new updates can disrupt behavior that previously worked. We study this problem as skill-evolution overfitting and introduce SkillEvoReg, a general regularization framework for skill evolution inspired by anti-overfitting techniques in neural-network training. SkillEvoReg combines training-time skill dropout, which perturbs update generation, and complexity-aware local regularization, which controls unnecessary structural growth, with causal counterexample validation (CCV), which provides targeted behavioral validation of candidate-specific regressions. We instantiate the framework across heterogeneous skill-evolution systems while retaining each system's native skill evolver and task evaluator. Across SkillOpt, SkillEvolBench, and ContinualSkillBench, SkillEvoReg consistently controls skill-state growth while preserving competitive downstream capability, improves several transfer and later-stage evolution outcomes, and identifies update-level regressions that structural metrics alone cannot reveal. These results suggest that explicit regularization is a useful complement to increasingly capable skill updaters.

## Metadata
- **Published**: 2026-09-25T06:11:26Z
- **Authors**: Guanyu Nie, Fangzhou Zhu, Shixiong Kai, Xiongwei Han, Tao Zhong, Mingxuan Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30861v1)