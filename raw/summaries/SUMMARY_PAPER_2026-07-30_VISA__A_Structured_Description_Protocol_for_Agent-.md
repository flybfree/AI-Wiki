---
title: VISA: A Structured Description Protocol for Agent-Based Simulation Models Towards Machine Reproducibility
url: http://arxiv.org/abs/2607.28027v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-14-26Z_VISA_AStructuredDescriptionProtocolforAgent_BasedS.md
generated_at: 2026-07-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VISA, a structured symbol‑based description protocol for agent‑based simulation models that aims to improve machine reproducibility by separating model components into eight interconnected tables and providing nineteen executable consistency rules plus three LLM skills (authoring, checking, code generation). It demonstrates the protocol by reproducing two cross‑language ABMs from their specifications and capturing an industrial AnyLogic model while noting where proprietary dependencies block reproduction. The work shows that VISA makes models machine‑parseable and unambiguous.

## Key Takeaways
- VISA organizes a model into eight tables (four agent level, four model level) to achieve minimality with completeness.
- The protocol includes nineteen executable consistency rules that turn model validity into a checkable property.
- Three reusable LLM skills automate the author‑check‑code‑reproduce loop.

## Context
Agent‑based simulation is widely used in AI research but reproducibility remains a challenge because models are documented across prose, platform code, and hidden assumptions. This fragmentation makes it difficult for independent researchers to rebuild or validate each other's work. VISA addresses this by providing a standardized, machine‑readable format that isolates dependencies.

## Implications
For practitioners, VISA lowers the barrier to reproducing complex ABMs, enabling automated validation pipelines and cross‑platform porting. For industry, it supports transparent model documentation while acknowledging proprietary constraints as a transparency contribution. The protocol aligns with broader AI reproducibility goals by making models visible, localized, and actionable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28027v1)
