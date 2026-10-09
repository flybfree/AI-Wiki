---
title: Trajectory-Guided Fault Localization for Agent Skill Evolution
published: 2026-10-08T12:38:51Z
authors: Yu Ge, Linna Xie, Zhong Li, Yu Pei, Tian Zhang
url: http://arxiv.org/abs/2610.11858v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory-Guided Fault Localization for Agent Skill Evolution

## Abstract
Agent skills provide reusable guidance for code agents, but incomplete or unsuitable guidance can impair task execution. To reduce the manual effort of skill refinement, recent approaches use LLMs to generate revisions from execution feedback. However, grounding these revisions in explicit behavioral evidence remains challenging. To address this gap, we propose SkillMorph, a skill-evolution approach based on trajectory-guided fault localization in agent skills. Its core idea is to link execution evidence to specific skill contents before generating revisions. Specifically, SkillMorph compares failure and success evidence in abstracted trajectories across repeated runs and tasks, incorporating changes between evolution loops to identify suspicious actions. It then uses these suspicious actions to localize edit sites in the skills and generate corresponding revisions. Experiments on SWE-Skills-Bench and CannBot show that the skills evolved by SkillMorph consistently achieve higher trial-level accuracy and execution consistency than the original skills and those from four existing skill-evolution methods. We have also applied SkillMorph to automated kernel generation with an AI operator-development team, which has accepted 6 skill-revision pull requests.

## Metadata
- **Published**: 2026-10-08T12:38:51Z
- **Authors**: Yu Ge, Linna Xie, Zhong Li, Yu Pei, Tian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11858v1)