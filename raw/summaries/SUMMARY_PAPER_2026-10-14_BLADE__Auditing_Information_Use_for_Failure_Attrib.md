---
title: BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems
url: http://arxiv.org/abs/2610.18780v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_17-34-34Z_BLADE_AuditingInformationUseforFailureAttributioni.md
generated_at: 2026-10-14 01:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
BLADE (Blame Localization via Audited Dependency Evidence) is a training-free framework designed to identify the responsible agent and decisive error step in LLM multi-agent systems by auditing how information is actually used at decision handoffs, rather than merely tracing where information originated. Using structured probabilistic judgments via Jev, BLADE selects relevant source-decision handoffs and examines whether receiving agents use their sources faithfully and within task requirements, distinguishing between error introduction, propagation, and repair. The framework achieves the best or tied-best step accuracy among eight competing strategies across 1,228 failed runs on five Who&When and Who&When Pro subsets, outperforming the All-at-once baseline by 2.2 to 11.1 percentage points without requiring reference answers.

## Key Takeaways
- BLADE shifts the failure attribution paradigm from dependency tracing to dependency auditing. Prior methods identify where information came from, but BLADE goes further by evaluating whether downstream agents faithfully and appropriately use that information within the constraints of the task, enabling it to distinguish three distinct failure modes: error introduction (the first agent that makes a mistake), error propagation (agents that carry the mistake forward), and error repair (agents that correct earlier errors). This three-way classification provides a more nuanced and actionable diagnosis than simple source tracing.
- The framework operates without reference answers and without training, making it broadly applicable to real-world multi-agent deployments where ground-truth solutions are unavailable. It uses Jev to produce structured probabilistic judgments and dependency probabilities, which guide the selection of relevant source-decision handoffs for targeted auditing. This training-free design means BLADE can be applied to arbitrary agent architectures and workflows without fine-tuning or labeled failure data.
- Empirical validation across 1,228 failed runs spanning five subsets of the Who&When and Who&When Pro benchmarks demonstrates that BLADE achieves the best or tied-best step-level accuracy among eight strategies evaluated under a shared Jev decision interface, surpassing the All-at-once strategy by 2.2 to 11.1 percentage points. The consistent performance across multiple benchmark subsets suggests robustness across different failure scenarios and agent configurations.

## Context
LLM multi-agent systems have become a dominant paradigm for tackling complex tasks by distributing work across specialized agents with distinct roles, tools, and workflows. However, the very collaboration that enables these systems to surpass single-agent capabilities also makes diagnosing failures significantly harder, since a single misinterpretation by one agent can cascade through the entire pipeline. Existing failure attribution methods focus on dependency tracing, mapping the flow of information between agents, but this approach conflates knowing where information originated with knowing where it was misused. BLADE addresses this gap by introducing an auditing layer that evaluates the quality and faithfulness of information use at each handoff, representing a meaningful advance in making multi-agent systems diagnosable and debuggable.

## Implications
For practitioners deploying multi-agent LLM systems in production, BLADE offers a practical, training-free diagnostic tool that can pinpoint which agent introduced an error and how it propagated, enabling targeted fixes rather than wholesale system redesign. By making responsibility evidence explicit, the framework supports more interpretable and auditable agentic pipelines, which is critical for domains requiring accountability such as finance, healthcare, and legal reasoning. More broadly, the distinction between error introduction, propagation, and repair opens a path toward automated repair mechanisms and self-correcting agent architectures, moving the field closer to truly reliable autonomous multi-agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18780v1)
