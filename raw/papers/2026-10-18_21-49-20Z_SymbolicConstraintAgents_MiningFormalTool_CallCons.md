---
title: Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors
published: 2026-10-18T21:49:20Z
authors: Jinu Lee, Shraddha Barke
url: http://arxiv.org/abs/2610.25552v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors

## Abstract
Symbolic constraints (programmatic, deterministic checks for tool calls) enable deterministic verification of LLM agents' tool calls, but existing approaches primarily enforce predefined safety policies rather than tool dependencies in complex tool environments. We explore whether symbolic constraints can be mined from environments and observations beyond predefined policies, and whether they can improve end-to-end task performance. We present Symbolic Constraint Agents (SCA), a framework that mines symbolic constraints from API documentation, refines them against execution traces, and checks the agent's tool calls with an SMT solver at runtime. A violation triggers a natural-language warning or, when the valid replacement is uniquely determined, an automatic repair. On AppWorld, refinement raises error-detection F1 from 37.0 to 58.3 on GPT-5.5 traces and from 39.3 to 61.9 on Qwen3.5-27B traces. At runtime, repair raises GPT-5.4-mini's task success by 5.4 points under a 40-call budget and 9.8 points when environment errors are hidden, while removing 59--87\% of failed calls across models, and transfers to $τ^2$-bench with gains of up to 5.6 points. These findings show that automatically acquired symbolic constraints can improve tool-calling reliability and task completion, particularly when failures are costly or difficult to diagnose.

## Metadata
- **Published**: 2026-10-18T21:49:20Z
- **Authors**: Jinu Lee, Shraddha Barke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25552v1)