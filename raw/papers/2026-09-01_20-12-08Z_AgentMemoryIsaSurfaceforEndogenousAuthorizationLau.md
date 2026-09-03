---
title: Agent Memory Is a Surface for Endogenous Authorization Laundering
published: 2026-09-01T20:12:08Z
authors: Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol
url: http://arxiv.org/abs/2609.01836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Memory Is a Surface for Endogenous Authorization Laundering

## Abstract
Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.   We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their provenance is washed away. We then introduce EAL-Bench, which measures how accurately persistent memory preserves evolving authorization state and whether errors propagate to downstream unauthorized actions.   We evaluate five LLMs as memory writers and two as executors across procurement, cybersecurity, and finance. We find that under incremental memory updates, writers create false authority for up to 50.2% of unauthorized requests; once false authority is present, executors act on it in 98.6% of trials. Two safeguards, requiring stored permissions to be backed by valid source events, and tracking permission changes through bounded event sourcing, substantially reduce laundering, but both also reject more legitimate actions, exposing a safety-utility tradeoff. Persistent memory is therefore not merely a performance component, but a part of an LLM agent's effective authorization policy.

## Metadata
- **Published**: 2026-09-01T20:12:08Z
- **Authors**: Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01836v1)