---
title: Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding
published: 2026-09-28T11:25:52Z
authors: Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin
url: http://arxiv.org/abs/2609.34924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding

## Abstract
An auditor who checks whether a system's weights are frozen is checking the wrong thing. Our stationarity dichotomy says that iterative self-modification hits strict diminishing returns whenever the agent's reachable set of edits stays fixed, and can escape only if that set expands. Rewriting scaffolding (tools, verifiers, decomposition) expands what an agent reaches without touching a weight, so frozen weights buy an eventual ceiling but no stationarity along the way. The criterion also separates three regimes usually merged: search within a fixed class, test-time training that raises the ceiling itself, and scaffold rewriting between them. Audit the scaffold, not the checkpoint.   The same ceiling binds sideways. Best-of-$k$ orchestration realizes the best worker's ceiling exactly: width buys rate, not budget. Re-consulting a fixed pool has a horizon computable in advance, decided by the pool alone, and the one arrangement that would beat it, a weighted vote, needs diversity real workers lack: on 30 same-family workers the failure overlap sits at its maximum, and a majority fails 23/55 (42%) of tasks.   We obtain the criterion by reading refinement as gradient boosting on the residual error between draft and target, a patch or git diff, and then measuring where that reading breaks: patches compose instead of standing beside each other to be voted on, and failures overlap. What we measure is saturation. Per-round improvement decays toward zero on SWE-bench, and churn decays geometrically across 401 production sessions, a shape shared with a pre-AI human baseline that establishes the regime without identifying its cause. Both breaks are engineering choices rather than laws about code, so together they specify a harness worth building.

## Metadata
- **Published**: 2026-09-28T11:25:52Z
- **Authors**: Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34924v1)