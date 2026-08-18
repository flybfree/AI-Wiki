---
title: Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory
url: http://arxiv.org/abs/2608.16889v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-59-57Z_Don_tDroptheBATON_Long_HorizonRobotManipulationvia.md
generated_at: 2026-08-17 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces BATON, a method for long‑horizon robot manipulation that combines agentic subtask exploration with transition‑aware memory. By freezing vision‑language‑action models and delegating planning to an LLM, BATON reduces the exponential cost of whole‑task learning and provides clear attribution of failures to individual stages.

## Key Takeaways
- Competence is derived from exploring each subtask in a short horizon, storing solutions additively so that a K‑stage task costs T·K instead of T^K, and any failure points to a single stage.  
- The VLA primitive lacks an entry condition; BATON adds transition‑aware memory with verifier agents that confirm scene readiness before invoking the VLA and restore entry states across subtasks.  
- No parameters are updated; all adaptation is handled by language memory and transition logic, enabling composition of long trajectories from short‑horizon solutions.

## Context
Current VLA systems excel at isolated manipulation tasks but struggle when skills are chained because errors compound and transitions are opaque. BATON addresses this by treating subtasks as atomic units and embedding transition constraints directly into the planning pipeline, aligning with trends toward modular, composable AI agents.

## Implications
For robotics engineers, BATON offers a scalable framework that can be integrated without retraining large models, lowering development time for complex manipulators. Practitioners may adopt this approach to build reliable multi‑stage systems where each component is robust and failures are traceable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16889v1)
