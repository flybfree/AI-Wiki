---
title: One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI
url: http://arxiv.org/abs/2610.19818v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_08-58-24Z_OneMonitorDoesNotFitAll_Formalism_AgnosticRuntimeV.md
generated_at: 2026-10-14 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces AgenticRV, a runtime-verification architecture designed for agentic AI systems that decouples execution-boundary observations from the monitoring formalism used to evaluate them. The core finding is that a single monitoring formalism cannot adequately cover the heterogeneous observation points (model decisions, mutable state, tool calls, delegation) inherent in agentic systems, and that a layered architecture with adapters, per-monitor projections, and normalized verdicts enables formalism-agnostic enforcement. The authors formalize conditions under which observations suffice, monitor replacement preserves decisions, and blocking prevents unsafe effects, while distinguishing rejected attempts from completed effects to avoid permanent violation states.

## Key Takeaways
- AgenticRV separates execution boundaries from monitoring formalism through a three-layer pipeline: adapters emit canonical events, each monitor receives its own projection and abstraction tailored to its formalism, and a decision policy selects reactions using normalized verdicts supported by the responsible adapter. This architecture means that temporal monitors, programmatic monitors, and other verification methods can coexist without requiring a unified specification language.
- The paper formalizes critical correctness properties: conditions under which a given set of observations is sufficient for a monitor to make sound decisions, the preservation of decisions when a monitor is replaced or updated, and the guarantee that blocking an operation prevents its unsafe effect from materializing. It also introduces the distinction between rejected attempts and completed effects, preventing the flawed assumption that a blocked request must leave every monitor in a permanent violation state.
- The Python implementation supports LangGraph, MCP, and A2A protocols, and a controlled LangGraph experiment combining an external Reelay temporal monitor with a programmatic report monitor demonstrates through ablation studies that both monitoring types are necessary for the selected safety requirements. Differential checks, cross-adapter tests, and an LLM-driven incident-response example provide integration evidence, while microbenchmarks isolate framework overhead costs.

## Context
Agentic AI systems increasingly orchestrate multi-step workflows involving language model reasoning, external tool invocations, mutable memory, and delegation to sub-agents, creating multiple execution boundaries where unsafe behavior can emerge. Existing runtime verification approaches typically assume a single formalism and a single observation point, which is insufficient for the heterogeneous and dynamic nature of agentic pipelines. This paper addresses a gap in the formal verification and AI safety literature by providing a principled architecture that accommodates diverse monitoring methods at explicit control boundaries, building on prior work in runtime verification, temporal logic, and AI safety evaluation.

## Implications
For practitioners deploying agentic AI in production, AgenticRV offers a reusable enforcement path that allows teams to plug in domain-specific monitors (temporal, programmatic, or LLM-driven) without rewriting the verification infrastructure, reducing integration friction across frameworks like LangGraph, MCP, and A2A. For the research community, the formalization of observation sufficiency, monitor replacement invariance, and the rejected-attempt versus completed-effect distinction provides a foundation for building composable, formally verified safety layers in agentic systems. Industry adopters gain a structured approach to meeting compliance and safety requirements across heterogeneous agent architectures while keeping monitoring overhead measurable through isolated microbenchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19818v1)
