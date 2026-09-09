---
title: ResidualAuth: What Authorization State Must Language Agents Preserve under Revocable Delegation?
url: http://arxiv.org/abs/2609.08062v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_00-05-05Z_ResidualAuth_WhatAuthorizationStateMustLanguageAge.md
generated_at: 2026-09-08 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a formal concept called residual authorization state to capture the subtle differences between two delegation histories that may appear identical in current permissions and reachability yet demand opposite decisions after a direct-edge revocation. Experiments demonstrate that exponentially many future-distinct states can share a single transitive closure, while a fixed 256‑token summary solves most of the paired language‑agent episodes across multiple models.

## Key Takeaways
- Two different authorization histories can have identical current permissions and all‑pairs reachability yet require opposite decisions after the same direct‑edge revocation.  
- Exponentially many future‑distinct states can share one fixed transitive closure, showing that the exact state needed for monitoring may be highly redundant.  
- A 256‑token summary solves 0–2 out of 16 pairs across four open‑weight models, whereas exact ledger serializations fit all 128 four‑coordinate pairs at both 768 and 1,024 token caps.

## Context
Language agents often delegate tasks to external services and must revoke permissions dynamically. Accurate monitoring of these delegations is essential for security and reliability, yet existing approaches struggle with the complexity introduced by overlapping or redundant authorization histories.

## Implications
This work clarifies what minimal information a monitor must retain to make correct decisions under delegation redundancy, guiding designers toward more efficient state‑maintenance strategies in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08062v1)
