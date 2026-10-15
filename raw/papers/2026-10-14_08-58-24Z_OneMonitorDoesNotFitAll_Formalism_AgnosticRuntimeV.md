---
title: One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI
published: 2026-10-14T08:58:24Z
authors: Angelo Ferrando
url: http://arxiv.org/abs/2610.19818v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI

## Abstract
Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a runtime-verification architecture that separates these boundaries from the monitoring formalism. Adapters emit canonical events; each monitor receives its own projection and abstraction; and a decision policy uses normalised verdicts to select a reaction supported by the responsible adapter. We formalise when observations suffice, monitor replacement preserves decisions, and blocking prevents unsafe effects. We also distinguish rejected attempts from completed effects, avoiding the assumption that a blocked request must leave every monitor in a permanent violation state. The Python implementation supports LangGraph, MCP, and A2A. A controlled LangGraph experiment combines an external Reelay temporal monitor with a programmatic report monitor; ablations show why both are needed for the selected requirements. Differential checks and cross-adapter tests provide further integration evidence. An LLM-driven incident-response example illustrates the same enforcement path, while existing microbenchmarks isolate framework costs. The results support reuse of monitoring methods at explicit control boundaries, subject to the stated observation and deployment assumptions.

## Metadata
- **Published**: 2026-10-14T08:58:24Z
- **Authors**: Angelo Ferrando
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19818v1)