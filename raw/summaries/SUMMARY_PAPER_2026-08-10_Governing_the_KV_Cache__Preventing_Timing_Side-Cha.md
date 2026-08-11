---
title: Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference
url: http://arxiv.org/abs/2608.09225v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_07-47-57Z_GoverningtheKVCache_PreventingTimingSide_ChannelLe.md
generated_at: 2026-08-10 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KVGov, a governance layer that protects multi‑tenant LLM inference from timing side‑channel attacks exploiting the shared key‑value cache. By seeding each principal’s block hash with a cryptographic salt derived from its identity, the attack surface is isolated, and an audit scheduler reduces adversary utility while preserving most of the caching benefit.

## Key Takeaways
- The per‑principal HMAC salt sigma_p creates cryptographically disjoint cache keys, making prefix reuse invisible to other tenants. - An ORIGAMI scheduler with Stackelberg water‑filling cuts expected attacker utility by 12.6% under realistic heterogeneity (Gini 0.63). - Evolutionary stability analysis shows a tipping point below which global caching remains stable.

## Context
Modern LLMs rely on KV caches to reuse token sequences across requests, dramatically improving throughput. In shared environments the cache becomes a timing vector that can leak private prompts, prompting new research into cryptographic isolation and scheduling mechanisms.

## Implications
For practitioners, KVGov demonstrates that security and performance are compatible through targeted salt injection at prompt divergence points. The approach offers a scalable defense for cloud‑hosted LLM services, reducing risk of data leakage without sacrificing the primary throughput gains of caching.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09225v1)
