---
title: AID-Guard: Stateful Authorization for Delegated Agent Effects
published: 2026-08-21T14:31:29Z
authors: Yingzhe Tong, Leyu Dai, Songhui Guo
url: http://arxiv.org/abs/2608.21159v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AID-Guard: Stateful Authorization for Delegated Agent Effects

## Abstract
Tool-using AI agents turn delegated tasks into provider effects, yet authorization often ends at admission while provider state, delivery, retry, and recovery evolve. A request may change before commit, or response loss may cause a replacement to create a second effect from one approval. We present AID-Guard, a stateful authorization-to-effect closure protocol. It revalidates the approved request and provider state at commit, retains one reservation under ambiguity, and permits release or one successor only after a terminal result or certified no effect with a delivery fence. For supported provider contracts, one reservation yields at most one effect across retry and recovery. To our knowledge, it is the first evaluated agent-authorization protocol to unify these controls in one lifecycle.   We implement a Python/SQLite prototype. In a declared loopback MCP domain, 13 live mutations caused no unauthorized provider effects, three concurrent histories were linearizable, and evidence bundles supported public verification and replay. All 210 Stripe provider-contract trials matched predeclared outcomes. Across Stripe and Resend, 40 terminalize-successor schedules, 30 overlapping races, and 10 crash-recovery schedules completed without duplicate effects. Under complete proposer compromise, AID-Guard blocked 44/44 attacks and admitted 44/44 matched legitimate proposals. Its strict exact-manifest profile reduced benign utility by 35.4 to 43.8 percentage points; a typed frontier recovered 9-10 completions without observed unsafe effects. A composition study blocked 20/20 post-admission lifecycle attacks and preserved 8/8 valid or exact-retry executions. The results support authorization-to-effect binding under the evaluated effect-path inventory, provider contracts, and failure schedules.

## Metadata
- **Published**: 2026-08-21T14:31:29Z
- **Authors**: Yingzhe Tong, Leyu Dai, Songhui Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21159v1)