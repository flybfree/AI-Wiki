---
title: FreeEvolve: Learning to Evolve Beyond Fixed Loops
published: 2026-10-06T22:47:19Z
authors: Lecheng Kong, Like Hui, Nikos Kanakaris, Prithwish Jana, Sahika Genc, Narayanan Sadagopan
url: http://arxiv.org/abs/2610.09197v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FreeEvolve: Learning to Evolve Beyond Fixed Loops

## Abstract
Agent evolvers automate the design of the prompts, skills and workflows around language model agents, yet the optimization process they follow is still designed by hand: a fixed search loop decides how candidates are evaluated, which are kept and when the search stops. We propose FREEEVOLVE, which automates this process as well. An environment specifies the goal, target agent, evaluator, data and resource limits; within these limits, the evolver itself decides what to test, how much evidence to collect, which candidates to pursue and when to stop. These decisions follow an editable evolution skill, which we improve through meta-evolution by scoring each candidate skill on the fresh target agent it produces. The optimization process thus becomes a capability learned from experience rather than a loop engineered in advance. On tau3-bench, ARC-AGI-2, ARC-AGI-3 and Terminal-Bench 2.1, FREEEVOLVE controls the evolution campaign by itself, yet improves the primary held-out metric by 13.6 points on average and matches or exceeds hand-designed evolvers. The learned process keeps improving with experience: meta-evolved skills add 6.9 points over the seed skill on fresh target agents, demonstrating transferability across environments.

## Metadata
- **Published**: 2026-10-06T22:47:19Z
- **Authors**: Lecheng Kong, Like Hui, Nikos Kanakaris, Prithwish Jana, Sahika Genc, Narayanan Sadagopan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09197v1)