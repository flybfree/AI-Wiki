---
title: Logos: An Agent Harness on a Cross-Process Bus
url: http://arxiv.org/abs/2608.28553v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_17-30-10Z_Logos_AnAgentHarnessonaCross_ProcessBus.md
generated_at: 2026-08-30 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Logos, a ROS‑like harness that enables agents to be composed across multiple processes while preserving a formal spatiotemporal composability calculus. The authors demonstrate that the model is stateless and fault‑tolerant, allowing sessions to resume after process kills without repeating effects.

## Key Takeaways
- Agents are modeled as plugins that share only an append‑only transcript, keeping all cross‑step state external to the language model.
- Faults interrupt every session at a single point in the tool‑call cycle, but under Logos one fault affects only its own process node.
- The calculus’s soundness invariant is defined solely on the state space, independent of which process hosts the component.

## Context
The work addresses a longstanding challenge in dynamic agent composition: ensuring that agents remain composable and resilient across processes. By formalizing spatiotemporal composability, Logos contributes to a broader AI research agenda focused on modular, fault‑tolerant systems.

## Implications
For practitioners, Logos provides a practical framework for building distributed agent pipelines without sacrificing safety or state integrity. In industry, this could enable scalable deployment of AI agents across microservices while handling failures gracefully.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28553v1)
