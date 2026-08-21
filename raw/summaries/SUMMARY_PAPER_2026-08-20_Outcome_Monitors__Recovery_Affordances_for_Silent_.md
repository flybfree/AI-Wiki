---
title: Outcome Monitors: Recovery Affordances for Silent Tool Failures
url: http://arxiv.org/abs/2608.19303v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_17-35-30Z_OutcomeMonitors_RecoveryAffordancesforSilentToolFa.md
generated_at: 2026-08-20 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Outcome Monitors, a mechanism that detects when an agent’s tool call violates pre‑defined outcome contracts and supplies nonbinding receipts naming the broken property and recovery tools. Experiments show that adding these monitors raises ToolMaze completion rates from 10.9% to 28.1% across multiple models and providers, with gains concentrated where faults block task execution.

## Key Takeaways
- Outcome Monitors preserve the failed result while issuing a receipt that lists the violated property and available recovery tools, allowing the agent to continue without halting.  
- In frozen evaluations with injected failures, completion improves significantly (10.9% → 28.1%) across four models and two provider families, indicating strong utility of the monitors.  
- The effect disappears when the recovery‑tool list is removed or restored, showing that the monitors’ benefit depends on having a valid receipt.

## Context
Outcome Monitors address a common problem in AI agents: silent tool failures that break task completion without obvious error signals. By mining outcome contracts from task traces and public schemas, the approach integrates failure detection into the normal flow of reasoning rather than relying on explicit exception handling.

## Implications
For practitioners, Outcome Monitors offer a lightweight way to surface latent errors and enable graceful recovery in production‑grade agents. The method also highlights that expanding detection beyond existing vocabulary limits performance gains, suggesting future work on richer contract vocabularies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19303v1)
