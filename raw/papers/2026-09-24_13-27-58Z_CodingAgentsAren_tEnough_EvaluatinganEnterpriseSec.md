---
title: Coding Agents Aren't Enough! Evaluating an Enterprise Security Brain for Agentic Cloud Investigations
published: 2026-09-24T13:27:58Z
authors: Leon Goldberg, Gal Engelberg, Eden Yavin, Elad Elouz, Ariel Zadok, Konstantin Koutsyi
url: http://arxiv.org/abs/2609.30345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coding Agents Aren't Enough! Evaluating an Enterprise Security Brain for Agentic Cloud Investigations

## Abstract
Cloud-security investigation is dominated by population tasks: which identities can read a data store, how many resources fail a control, which assets are reachable from another account. These resolve against a complete inventory, not a named object. A partial answer to one is not a partial result. It is a different result. General-purpose coding agents can now be given read-only cloud credentials and asked to investigate directly, which raises the question of what a purpose-built security context layer still contributes. We evaluate the Sola Security Brain, a security intelligence layer whose relational substrate is resolved offline and whose security logic is evaluated against it at query time, against Claude Code operating the same live AWS environment through a read-only CLI, over 28 cloud-security investigation tasks. Answers are scored by a blinded, tier-weighted, grounding-gated relative recall over the joint claim pool, averaged across three independent grading draws. The Sola Security Brain reaches 0.693 coverage against 0.387, a gap of 0.306 that varied by $\pm 0.018$ across three grading draws, or a relative gain of $79.2\%$. It leads on 25 of 28 tasks from the weaker model tier, at $17.7\times$ lower reasoning cost per task and $31.6\times$ lower cost per unit of coverage. Beyond the aggregate, we describe an answer-level pattern we term sample-and-generalise: under a turn budget the live agent enumerates a fraction of a large population, asserts an unhedged universal negative, and discloses the sample size only in answer metadata rather than in the answer. In one task it reported that no bucket policies exist after checking four bucket families, in a sweep that sampled 40 of roughly 5{,}000 buckets, in an account where 65 buckets carry a wildcard-principal read grant.

## Metadata
- **Published**: 2026-09-24T13:27:58Z
- **Authors**: Leon Goldberg, Gal Engelberg, Eden Yavin, Elad Elouz, Ariel Zadok, Konstantin Koutsyi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30345v1)