---
title: Deny Without Disabling: Authorization-Paired Evaluation and Control for Multi-Agent Systems
url: http://arxiv.org/abs/2610.00371v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_06-55-18Z_DenyWithoutDisabling_Authorization_PairedEvaluatio.md
generated_at: 2026-10-01 21:40
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the safety challenge in multi-agent systems where individually admissible actions can combine to enable prohibited uses without necessitating the blocking of all sensitive actions. It introduces authorization-paired evaluation and the FlowReview framework, which jointly optimize for denying harmful compositions while preserving authorized capabilities through deterministic enforcement and permission ranking. Controlled experiments demonstrate that reviewing combined artifacts eliminates denied-commit rates entirely without sacrificing the supply of authorized information flows, proving that collaboration can remain functional under strict safety governance.

## Key Takeaways
- Authorization-paired evaluation establishes a joint success criterion where blocking prohibited uses and completing required authorized uses are optimized simultaneously, implemented via FlowReview to connect object resolution, permission ranking, and deterministic enforcement for balanced multi-agent control.
- Empirical results show that reviewing combined artifacts reduces the denied-commit rate from 86.0% to zero with no loss of authorized supply, indicating that composition-aware review is superior to isolated action blocking in maintaining utility while ensuring safety.
- The findings reveal that preserving information and lineage alone does not guarantee correct permission attribution; object identity must remain connected to execution through components whose outputs can be verified, establishing a fundamental system-level requirement for governing composed information flows.

## Context
As multi-agent systems increasingly rely on evidence sharing and task delegation to solve complex problems, the risk of emergent safety violations from composing benign actions remains an unresolved challenge in AI alignment. This research tackles the critical tension between enabling effective collaboration and preventing prohibited joint behaviors, offering a structured approach to authorization that scales with system complexity rather than relying on coarse-grained restrictions.

## Implications
Practitioners designing multi-agent architectures must move beyond isolated action filtering to implement dynamic evaluation of composed information flows and verifiable permission tracking to prevent emergent risks. Industry adoption of frameworks like FlowReview can facilitate the deployment of robust collaborative AI systems by preserving operational utility while rigorously mitigating the potential for prohibited uses arising from agent interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00371v1)
