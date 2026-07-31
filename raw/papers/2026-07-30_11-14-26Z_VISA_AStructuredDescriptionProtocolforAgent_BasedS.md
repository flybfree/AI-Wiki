---
title: VISA: A Structured Description Protocol for Agent-Based Simulation Models Towards Machine Reproducibility
published: 2026-07-30T11:14:26Z
authors: Zhou He
url: http://arxiv.org/abs/2607.28027v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VISA: A Structured Description Protocol for Agent-Based Simulation Models Towards Machine Reproducibility

## Abstract
Agent-based models (ABMs) are difficult to reproduce: their behavior is spread across prose narratives, platform-specific code, and implicit assumptions, so that two readers routinely reconstruct different models from the same documentation. We present VISA, a structured, symbol-based description protocol that specifies a model in eight interconnected tables---four at the agent level (Agent, Variable, Sensing, Internal Function) and four at the model level (Associated Data, Input/Output, Schedule, Validation)---under the principle of minimality with completeness. VISA makes a model machine-parseable and unambiguous via two artifacts: nineteen executable consistency rules that turn model validity into a checkable property, and three reusable LLM-executable skills (authoring, checking, and code generation) that operationalize the full author--check--code--reproduce loop. We validate the protocol on three external, independently authored ABMs spanning three platforms: we reproduce two cross-language (NetLogo to Python) directly from their VISA specifications, and we capture a third, an industrial AnyLogic model, in eight tables (passing all nineteen rules) while honestly demarcating where reproduction is blocked by a proprietary movement library and unavailable data---itself a transparency contribution. VISA moves the reproduction barrier from the model, where it is invisible, to a named, localized dependency, where it is actionable.

## Metadata
- **Published**: 2026-07-30T11:14:26Z
- **Authors**: Zhou He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28027v1)