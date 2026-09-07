---
title: From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents
url: http://arxiv.org/abs/2609.04869v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-29-45Z_FromInteractionTracestoPersistentSkills_OnlineEvol.md
generated_at: 2026-09-06 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an online skill‑evolution framework that turns interaction traces and evaluator feedback into a persistent, versioned library of reusable procedures for computer‑use agents. Across four OSWorld domains the evolving library improves agent performance after a warm‑up period, outperforming a configuration‑matched empty library by up to 18.6 percentage points in some tasks.

## Key Takeaways
- The framework creates a frozen snapshot of skill knowledge at each iteration, allowing later iterations to draw on accumulated procedural memory without altering the underlying model parameters.  
- Evaluation shows that full libraries consistently raise evaluator scores after five warm‑up steps, with gains ranging from 5.7 to 18.6 percentage points depending on the application domain.  
- Provenance analysis in GIMP reveals that repeated accepted edits can lead to revision churn, where later tasks cannot reliably retrieve the original task’s skill state.

## Context
Computer‑use agents must retain and refine procedural knowledge across multiple sessions, yet current approaches treat each rollout as independent. This work addresses the gap by formalizing a shared memory of skills that persists through iterations, providing a baseline for measuring incremental learning in graphical interfaces.

## Implications
The results suggest that persistent skill libraries can serve as an auditable form of procedural memory for fixed AI stacks, offering measurable benefits when interaction is repeated. Practitioners should monitor revision churn to avoid loss of original task knowledge and consider versioned snapshots for reliable skill reuse.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04869v1)
