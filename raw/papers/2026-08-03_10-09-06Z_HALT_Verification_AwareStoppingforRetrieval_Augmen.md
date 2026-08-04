---
title: HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents
published: 2026-08-03T10:09:06Z
authors: Daeyoung Roh, Donghee Han
url: http://arxiv.org/abs/2608.02009v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents

## Abstract
Retrieval-augmented search agents answer multi-hop questions by repeatedly issuing search queries and accumulating evidence. This creates a stopping problem: after the necessary evidence has appeared, further retrieval often adds cost, latency, and distracting context rather than useful information. We frame stopping as evidence coverage rather than generator confidence, and introduce HALT, a lightweight verification-aware policy that leaves the search agent unchanged. Given expected hop claims, HALT stops only when cumulative evidence supports each required claim. Across three multi-hop QA benchmarks, HALT reduces redundant search while largely preserving exact match. We separate a deployable setting, where hop claims are generated from the question, from a diagnostic upper bound that uses gold supporting-fact annotations: generated claims give smaller but still exact-match-preserving savings, while gold claims show the larger savings available when hop targets are clean. Baseline comparisons and ablations show that this behavior is driven by claim-evidence alignment rather than generic sufficiency, fixed stop positions, or lexical overlap. Open-corpus pilots further suggest that HALT abstains when coverage cannot be reliably verified. Overall, evidence coverage provides a practical runtime control signal for improving retrieval-augmented agents without retraining or modifying the host agent.

## Metadata
- **Published**: 2026-08-03T10:09:06Z
- **Authors**: Daeyoung Roh, Donghee Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02009v1)