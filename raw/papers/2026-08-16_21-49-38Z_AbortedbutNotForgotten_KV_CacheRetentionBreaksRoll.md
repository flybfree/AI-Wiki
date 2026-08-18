---
title: Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents
published: 2026-08-16T21:49:38Z
authors: Guijia Zhang, Harry Yang
url: http://arxiv.org/abs/2608.15939v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents

## Abstract
Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript. We show this breaks when the serving session retains key/value (KV) state across the logical abort: the model can continue attending to content the application believes it discarded. We formalize the missing guarantee as rollback consistency: a complete abort must restore the state the model attends, not just the transcript. The key failure is cross-layer: a correct logical rollback need not compose with retained inference state, and the gap can remain invisible to the application. To isolate cache effects from text effects, we introduce a same-token/different-cache audit that holds decision-step tokens identical while varying only whether the cached prefix is stale or rebuilt from committed state. Across seven open-weight families (3.8B-36B), retained KV alone flips a typed protected effect in 25 of 63 audited cells, while attacker tokens are absent from the served request in all 63; rebuilding the cache closes every cell. The channel reproduces in an end-to-end session application, on the default Hugging Face Transformers cache-reuse path, and under LangGraph time-travel, where verified logical rollback can still leave attended KV stale. Susceptibility varies across models, but the underlying attended-state integrity violation is structural. We rule out position and length confounds, generalize across protected effects, policy structures, and a cache-isolated Mixture-of-Experts model, and show that transaction-local cache restoration closes the channel without requiring a global cache flush. All headline results are deterministic and reproducible from released artifacts.

## Metadata
- **Published**: 2026-08-16T21:49:38Z
- **Authors**: Guijia Zhang, Harry Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15939v1)