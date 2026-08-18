---
title: Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents
url: http://arxiv.org/abs/2608.15939v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_21-49-38Z_AbortedbutNotForgotten_KV_CacheRetentionBreaksRoll.md
generated_at: 2026-08-17 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper demonstrates that the KV‑cache retention mechanism used by language agents can violate rollback consistency when a logical abort is performed, allowing the model to continue attending to content that the application believes has been discarded. The authors formalize this issue and show it persists across seven open‑weight model families, highlighting a cross‑layer failure between logics and cached inference state.

## Key Takeaways
- Retained KV alone flips a protected effect in 25 of 63 audited cells while attacker tokens are absent from the served request.  
- Rebuilding the cache restores consistency, proving that transaction‑local restoration is sufficient without global flushes.  
- The channel reproduces in end‑to‑end sessions and LangGraph time‑travel, indicating a structural problem with attended‑state integrity.

## Context
Stateful language agents rely on transparent rollbacks to discard branches, yet the underlying KV cache can retain information that contradicts this expectation. This gap undermines the reliability of agents that must preserve user expectations across logical operations.

## Implications
For developers integrating LangGraph or similar frameworks, ensuring cache‑aware rollback is critical to maintain trustworthy behavior. Ignoring this issue could lead to subtle bugs where users perceive actions as successful while internal state remains inconsistent.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15939v1)
