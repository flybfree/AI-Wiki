---
title: AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework
published: 2026-09-24T20:49:53Z
authors: Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier
url: http://arxiv.org/abs/2609.30541v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework

## Abstract
Optimizing embedding systems for production recommendation pipelines demands systematic exploration that consumes disproportionate engineering effort at scale. We apply Andrej Karpathy's AutoResearch paradigm -- a large language model that iteratively edits a training script and retains modifications that improve a held-out scalar metric -- to automate this exploration. We report on twelve weeks of running this paradigm at production scale, where iterations consume hours of multi-GPU compute, evaluation involves competing criteria, and campaigns span weeks across many training jobs. Across two independently developed representation-learning systems for a book recommendation pipeline, we ran 220+ experiments and observed five recurring failure modes absent from the original setting: infrastructure fragility, agent memory decay, search-direction stagnation, iteration-cost asymmetry, and metric fixation. We contribute a three-principle scaffolding design -- prevent, persist, redirect -- that maps each failure mode to a structural remedy and whose instantiation scales with iteration cost. The framework produced a 1.82x Recall@6 lift and a 2.1x coherence lift over hand-tuned baselines, and the agent autonomously designed a text-only fallback that expanded catalog coverage by 5.8x. The two systems span nearly three orders of magnitude in per-iteration cost yet exhibit the same failure modes, suggesting these are structural properties of production-scale autonomous research rather than artifacts of either application.

## Metadata
- **Published**: 2026-09-24T20:49:53Z
- **Authors**: Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30541v1)