---
title: VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning
published: 2026-10-09T06:51:59Z
authors: Yingbo Ma, Kuangshi Ai, Gordon Dai, Chenglong Yu, Chaoli Wang, Hua Shen
url: http://arxiv.org/abs/2610.13098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning

## Abstract
Visual agents for symbolic graphics reasoning depend on executable world representations, yet continued improvement remains bottlenecked by ambiguous supervision from final renders. Recent agentic systems refine scenes through repeated interaction, but they lack mechanisms to recursively extract actionable evidence from execution traces, overlooking which proposed symbolic edits survived, disappeared, or interfered during program execution. To address this, we propose VETR (Verified Execution Trajectories for Refinement), a framework that enables agentic recursive self-improvement over executable world representations for symbolic graphics reasoning. Within each task, VETR retains aligned program/render records with bounded runtime observations and introduces an execution refiner that compiles observed writes and state changes into constrained alternative programs. The refiner validates their endpoints and preservation conditions against captured runtime state; the ordinary visual verifier then assesses goal relevance. Repair construction makes no additional language-model calls, but can require additional executions. Evaluations on BlenderGym (280 tasks) and BlenderBench (27 released tasks) with GPT-5.6-luna and Qwen3.8-27B show that VETR consistently outperforms existing refinement strategies, including BlenderAlchemy and VIGA. Controlled ablations evaluate the contributions of execution refinement and role-asymmetric evidence organization under fixed generator-interaction caps.

## Metadata
- **Published**: 2026-10-09T06:51:59Z
- **Authors**: Yingbo Ma, Kuangshi Ai, Gordon Dai, Chenglong Yu, Chaoli Wang, Hua Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13098v1)