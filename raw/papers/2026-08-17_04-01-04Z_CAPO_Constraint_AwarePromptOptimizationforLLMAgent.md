---
title: CAPO: Constraint-Aware Prompt Optimization for LLM Agents
published: 2026-08-17T04:01:04Z
authors: Victor Ye Dong, Reid Pryzant, Yi Liu, Jian Jiao
url: http://arxiv.org/abs/2608.16068v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAPO: Constraint-Aware Prompt Optimization for LLM Agents

## Abstract
Large language models (LLMs) are increasingly deployed as agents that rely on system prompts to use tools and complete tasks. Such deployments impose distinct operational requirements, including appropriate tool use, concise prompts and solution paths, and compliance with safety and formatting policies. For many practitioners, however, assembling domain-specific supervised data to post-train models to meet these requirements is infeasible. We introduce CAPO (Constraint-Aware Prompt Optimization), a primal-dual method that combines pool-based rewrites with adaptive constraint weighting to optimize system prompts under explicit operational constraints. Across agentic benchmarks, CAPO more reliably reaches empirically feasible operating points while improving task performance. CAPO also generalizes beyond agentic settings, achieving strong results on assistant-style evaluations with output-format and safety/privacy constraints. We further introduce DCAPO (Dynamically Trained CAPO), which trains a feedback- and dual-conditioned rewriter with pool-based GRPO while keeping the task agent frozen. Across task agents of different sizes, DCAPO produces a feasible prompt in every evaluated domain and matches or improves the task accuracy achieved by the evaluated baselines. A surrogate analysis characterizes how finite-pool and discrete-rewrite errors enter the inexact primal-dual procedure.

## Metadata
- **Published**: 2026-08-17T04:01:04Z
- **Authors**: Victor Ye Dong, Reid Pryzant, Yi Liu, Jian Jiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16068v1)