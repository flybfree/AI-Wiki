---
title: Keep the Process, Change the Supplier: Runtime Governance for Tool-Using AI Agents
url: http://arxiv.org/abs/2611.26966v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_01-40-57Z_KeeptheProcess_ChangetheSupplier_RuntimeGovernance.md
generated_at: 2026-11-22 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Open Process Control Plane (OPCP), a runtime governance mechanism that creates an execution boundary between AI agent proposals and business-controlled authority, context disclosure, and supplier selection for tool-using agents. The authors evaluate OPCP using scripted requests and synthetic suppliers across thousands of fault episodes, demonstrating that it and a conservative composition agree on all measured fault outcomes, while also characterizing latency costs and assumption boundaries of the execution mechanism. Notably, no language model or autonomous agent is evaluated, and the authors explicitly disclaim claims about improved task success, prompt-injection resistance, or real-vendor model portability.

## Key Takeaways
- OPCP mediates capability calls and records uncertain outcomes when a supplier may have acted without returning an acceptable reply, establishing a clear separation between agent-generated proposals and externally controlled authority. The evaluation spans 2,400 fault episodes across four policies, 60 process-termination/restart episodes, 19,000 timed calls across 19 configurations, five targeted mutations over 43 fixtures, and 160 substitution records, providing a thorough characterization of the runtime's behavior under failure conditions.
- Retry policies have critical safety implications: both OPCP and a conservative composition recover after definite refusal without cross-supplier duplication, but a retry-all policy duplicates effects in every tested lost-reply-after-commit case. Persistent runtime state prevents cross-supplier replay during restart experiments, though same-supplier duplicate prevention additionally requires supplier idempotency, highlighting that governance alone is insufficient without cooperation from external services.
- Performance tradeoffs are quantified: at 128 suppliers, best-score routing incurs a median latency of 1.411 ms versus 0.261 ms for pinned routing, a roughly 5.4x increase. All five selected mutations are detected by the system, and record enumeration exposes acceptance of an empty regression set, indicating the evaluation framework can identify gaps in test coverage.

## Context
As AI agents increasingly interact with external tools, APIs, and third-party services, the question of who authorizes actions, which supplier executes them, and how uncertain outcomes are handled becomes a governance problem rather than a purely algorithmic one. This paper addresses a gap in the agent safety and reliability literature by formalizing an execution boundary that is independent of the language model itself, treating the agent as a proposal generator and the runtime as an authority mediator. It matters because existing agent frameworks often conflate generation with execution, leaving ambiguous responsibility when external effects occur without confirmation.

## Implications
For practitioners building production agent systems, OPCP provides a concrete architectural pattern for separating agent reasoning from business authority and supplier management, with quantified costs and explicit assumption boundaries that help teams make informed tradeoffs between routing flexibility and latency. The findings caution that governance mechanisms must be paired with supplier idempotency guarantees to fully prevent duplicate side effects, and that evaluation frameworks must be designed to detect their own blind spots, such as empty regression sets. For the broader field, this work shifts attention from model-level safety to runtime-level safety, suggesting that agent governance is as much an infrastructure and policy engineering problem as it is a machine learning one.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.26966v1)
