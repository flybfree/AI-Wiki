---
title: SkillForge: Compositional Skill Synthesis with Verification-in-the-Loop for Generating Formally Verified Dafny Programs
published: 2026-08-30T15:15:00Z
authors: Yanming Liu, Xinyue Peng, Jiannan Cao, Xinyi Wang, Jinbo Su
url: http://arxiv.org/abs/2608.29841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillForge: Compositional Skill Synthesis with Verification-in-the-Loop for Generating Formally Verified Dafny Programs

## Abstract
Generating formally verified programs from natural language remains challenging: existing approaches either produce code in a single pass without recourse when verification fails, or rely on open-ended agentic reasoning that is non-deterministic and opaque. We introduce SKILLFORGE, a framework that decomposes formal code synthesis into a library of atomic, reusable skills, each targeting a specific subtask such as specification inference, body synthesis, invariant generation, error diagnosis, or targeted repair, and defined by a prompt template, tool binding, and decidable success criterion. A verification-driven harness orchestrates these skills: it submits candidates to the Dafny verifier, diagnoses failures into structured categories, deterministically routes to the appropriate repair skill, and iterates until formal correctness is proved or a budget is exhausted. On a curated benchmark of natural language to Dafny specification pairs, SKILLFORGE substantially outperforms both state-of-the-art agentic approaches (including ReAct-style agents, MCTS-based repair, and RL-guided verification) and traditional iterative baselines, while requiring fewer tokens and lower latency. Ablation studies confirm that every skill contributes measurably, and the harness converges rapidly with the majority of programs verified on the first attempt.

## Metadata
- **Published**: 2026-08-30T15:15:00Z
- **Authors**: Yanming Liu, Xinyue Peng, Jiannan Cao, Xinyi Wang, Jinbo Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29841v1)