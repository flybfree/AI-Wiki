---
title: Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches
url: http://arxiv.org/abs/2610.22016v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_14-56-53Z_CloseEnoughisNowhereNear_Fidelity_ConsumabilityDec.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether a frozen LLM can directly consume another model's KV cache as a substitute for its own, a proposed mechanism for efficient communication in multi-agent systems. The authors demonstrate that this substitution fundamentally fails: frozen transformers can only process caches that closely resemble what they would have generated themselves, and no amount of geometric fidelity improvement rescues the approach. They redirect the field toward a promising alternative—augmenting the reader's own cache with the sender's as additional context while adapting only the reader's queries.

## Key Takeaways
- Frozen transformers possess a "tolerable set" of KV caches they can actually use, defined as caches geometrically close to what the model would have written itself. Geometric similarity to the target cache does not predict whether the reader can functionally consume it, and the failure mode is abrupt rather than gradual, meaning incremental improvements in cache fidelity do not yield incremental usability gains.
- The authors test eight diverse substitution methods against two measured anchors—an uninformative cache baseline and the reader's own accuracy after reading the passage—and all eight methods land at the baseline level, collapsing a scattered literature of negative results into a single unified outcome with a clearly stated condition for overturning it.
- A structurally different design succeeds: the reader retains its own KV cache and attends over the sender's cache as supplementary context, adapting only its query projections. This approach beats the reader's own baseline and also clears the baseline when eight senders are pooled, whereas undirected attention over the same union of caches falls below it.

## Context
Multi-agent LLM systems typically communicate through generated text, which discards the interpretive work already performed by the sender. A growing body of work proposes transmitting KV caches directly to avoid this lossy bottleneck. This paper addresses the most attractive variant—zero-training substitution where both models remain frozen—and provides a rigorous negative result that explains why prior attempts failed, while simultaneously proposing a constructive alternative. It matters because it redirects a significant research effort away from a dead-end design toward a viable architectural pattern.

## Implications
For practitioners building multi-agent pipelines, this work signals that investing engineering effort in making one model's cache "more faithful" to another's is a misdirected optimization; the productive path is architectural, preserving the reader's own cache and grafting the sender's as auxiliary context with minimal query adaptation. For the broader field, the paper's unified negative result and explicit overturning condition provide a clear boundary for future KV-cache-sharing research, preventing wasted effort on incremental fidelity improvements and steering the community toward query-adaptive fusion designs that respect each model's internal attention structure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22016v1)
