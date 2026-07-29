---
title: Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents
url: http://arxiv.org/abs/2607.25408v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-07-06Z_ContextAssemblyastheControlledVariable_AControl_Th.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes treating context assembly — such as prompt template choice, few‑shot demonstrations, and retrieved information volume — as the controlled variable for frozen LLM agents. It formalizes a decomposition into an inner frozen policy πθ and an outer online controller πφ that learns via contextual bandit or REINFORCE. The work provides stability proofs showing non‑decreasing expected reward under bounded policy changes and uncertainty‑calibration analysis linking controller confidence to task outcomes.

## Key Takeaways
- The controlled variable is context assembly, not tool selection or raw actions, which the outer policy πφ optimizes online.  
- Stability is defined as a non‑decreasing expected reward when the outer policy changes within bounded bounds, aligning with prior control‑theoretic definitions.  
- The controller’s confidence in its predictions is calibrated against actual task results, offering an uncertainty metric for frozen agents.

## Context
Recent AI research has applied control theory to LLM agents, focusing on stability of tool selection and message routing (Prinos et al., 2026). This work narrows the scope to context assembly as a learnable variable, contributing to the broader effort of treating agent behavior as a dynamical system that can be stabilized.

## Implications
Practitioners can implement this controller framework across different model providers and domains, providing a reusable stability and calibration toolkit. The released dataset and deployment recipe enable systematic evaluation of how context assembly influences frozen LLM performance in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25408v1)
