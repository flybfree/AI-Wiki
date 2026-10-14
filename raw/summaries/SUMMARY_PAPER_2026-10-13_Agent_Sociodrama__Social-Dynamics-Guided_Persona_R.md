---
title: Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams
url: http://arxiv.org/abs/2610.15788v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_17-23-24Z_AgentSociodrama_Social_Dynamics_GuidedPersonaRecas.md
generated_at: 2026-10-13 21:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Agent Sociodrama, a framework for modeling and validating evolving social dynamics within LLM agent teams by tracking emotional states and directed asymmetric relationships updated each round via an external LLM judge. Building on these validated social trajectories, the authors propose Trajectory-Guided Persona Recasting (TPR), a method that diagnoses group-dynamic failures from interaction transcripts and recasts agent personas before rerunning tasks, achieving up to 83.3 percentage points of accuracy improvement and outperforming SOTOPIA and AgentVerse in three of four benchmark comparisons.

## Key Takeaways
- Agent Sociodrama models social dynamics in LLM agent teams under fixed personas by updating agents' emotional states and directed, asymmetric relationships every interaction round through a unified external LLM judge. This approach captures characteristic social failure modes such as information holders staying silent, dominant speakers anchoring groups on incorrect answers, and norm violations going unsanctioned, and validates these trajectories against classical social-theory patterns and human judgments across six LLM backbones and five social scenarios.
- Trajectory-Guided Persona Recasting (TPR) uses diagnosed group-dynamic failures extracted from interaction transcripts and social trajectories to recast agent personas before rerunning collaborative tasks. Across four collaborative benchmarks, TPR improves performance from both heterogeneous and randomly initialized agent persona compositions, yielding up to 83.3 percentage points of accuracy improvement over the initial casting, demonstrating that social trajectory signals are actionable repair mechanisms rather than mere diagnostic artifacts.
- On representative distributed-information cooperation and mixed-motive bargaining tasks, the proposed approach outperforms SOTOPIA and AgentVerse in three of four comparisons, achieving up to 37.5 percentage points improvement in Pareto rate. This establishes that structured social trajectory modeling provides a concrete, measurable advantage over existing multi-agent coordination frameworks in tasks requiring genuine cooperation and negotiation.

## Context
As LLM agents are increasingly deployed in multi-agent teams for collaborative reasoning, negotiation, and distributed problem-solving, their failures often mirror well-documented human group-dynamics pathologies rather than simple capability gaps. Existing multi-agent frameworks such as SOTOPIA and AgentVerse treat agent interactions as largely static or persona-fixed, leaving social dynamics unmodeled and uncorrectable. Agent Sociodrama bridges classical social psychology with LLM agent design by providing a validated, round-by-round social modeling layer that makes group-dynamic failures observable and addressable, representing a shift from treating agent teams as collections of independent reasoners to treating them as evolving social systems.

## Implications
For practitioners building multi-agent LLM systems, this work demonstrates that persona assignment is not a one-time design decision but an iteratively correctable parameter guided by observable social trajectory signals, offering a concrete debugging and optimization loop for agent team performance. For the broader field, the validated connection between classical social-theory patterns and LLM agent behavior suggests that social psychology provides a principled foundation for diagnosing and repairing coordination failures in AI systems, potentially informing safer and more effective deployment of agent teams in enterprise, research, and public-sector applications where group reasoning quality directly affects outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15788v1)
