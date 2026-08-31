---
title: Logos: An Agent Harness on a Cross-Process Bus
url: http://arxiv.org/abs/2608.28553v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_17-30-10Z_Logos_AnAgentHarnessonaCross_ProcessBus.md
generated_at: 2026-08-31 15:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Logos, a ROS‑like harness that enables agents to run across multiple processes while sharing only an append‑only transcript as state. The authors demonstrate that the spatiotemporal composability calculus can be applied without binding agents to a single process, and they show eighty sessions resume correctly after faults placed at tool‑call boundaries. Their analysis also shows that under peer‑process construction one fault interrupts only one node, unlike a single‑process reference where every session is halted.

## Key Takeaways
- The calculus treats capabilities as components with tracked inverses, allowing agents to be assembled as plugins independent of the host process.
- Stateless language‑model inference keeps all cross‑step state outside the model, enabling soundness invariants defined purely on the state space.
- Logos uses an append‑only transcript as the sole shared data structure, ensuring that after a fault only one session is affected per node.

## Context
The paper builds on recent advances in formalizing dynamic agent composition and spatiotemporal composability, which have traditionally assumed a single process context. By decoupling agents from host processes and isolating state to an append‑only log, the authors address longstanding limitations of existing agent frameworks that suffer from global failures.

## Implications
For practitioners, Logos offers a practical way to build resilient multi‑process agent systems without sacrificing composability or safety. Industry adoption could lead to more robust AI agents that survive crashes and maintain continuity across distributed components.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28553v1)
