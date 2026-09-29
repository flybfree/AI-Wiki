---
title: Vestrum: Improving Agent Harnesses by Adapting Their Verification, Structure and Memory
published: 2026-09-27T18:20:51Z
authors: Jayant Parashar, Eugene F. Douglass, William C. Bastian, Suchendra M. Bhandarkar
url: http://arxiv.org/abs/2609.33822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vestrum: Improving Agent Harnesses by Adapting Their Verification, Structure and Memory

## Abstract
An agent harness controls how a language model accesses information, uses tools, preserves memory, and checks its work. Improving this software is costly when each evaluation requires a long interaction with an environment. We introduce Vestrum, a framework that turns failures in execution traces into scoped harness changes without training the task model. Its organizing overhypothesis is that tasks of a shared kind may exhibit recurring failures whose remedies transfer within that kind. Vestrum expresses failures as recognizable classes, proposes changes across verification, retrieval, decomposition, and knowledge synthesis, and screens their scope before evaluating them as a bundle. A persistent lessons file informs subsequent proposals. Across five settings and two baseline harnesses, the frozen harnesses improve held-out performance: UltraHorizon rises from 47.6 to 59.8 over GAM, Terminal-Bench 4 Hard from 63.7% to 70.3% of checks passed over Claude Code on eight held-out tasks at 1.03x test cost, and cell-type annotation agreement from 67.5% to 77.8% on held-out sections of one slide, alongside gains on LoCoMo and AMA-Bench. Across our searches, verification grounded in evidence helped both intermediate steps and final answers, at lower cost at intermediate steps, while critics asked to rebuild finished answers broke more than they repaired. On the three memory benchmarks, Vestrum also scores above the evaluated GEPA configurations in every paired evaluation.

## Metadata
- **Published**: 2026-09-27T18:20:51Z
- **Authors**: Jayant Parashar, Eugene F. Douglass, William C. Bastian, Suchendra M. Bhandarkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33822v1)