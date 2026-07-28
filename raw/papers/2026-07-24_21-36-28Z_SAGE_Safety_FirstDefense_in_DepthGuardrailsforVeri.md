---
title: SAGE: Safety-First Defense-in-Depth Guardrails for Verified Lifecycle Control of High-Impact Generative AI
published: 2026-07-24T21:36:28Z
authors: Mahdi Eslamimehr
url: http://arxiv.org/abs/2607.22926v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: Safety-First Defense-in-Depth Guardrails for Verified Lifecycle Control of High-Impact Generative AI

## Abstract
High-impact generative AI makes catastrophic misuse a lifecycle-control problem, not merely a prompt-filtering problem. SAGE is a safety-first, authorization-separated architecture in which credible catastrophic-enablement risk constrains admissibility before utility, latency, or commercial objectives are considered. It combines signed release manifests, diverse detectors, robust risk envelopes, least-risk defaults, output checking, three-valued monitoring, protected audit chains, containment, and rollback. Formal results establish safety priority, conservative detector bounds, monotone release gating, tamper-evident records, and an authorization cut; two PRISM abstractions verify authorization separation and lifecycle invariants under explicit assumptions.   A frozen, vendor-symmetric study sent 84 cases to each of four GPT, four Claude, and two Gemini snapshots: 840 calls yielded 794 target responses, 46 provider errors, and 449 successful judgments covering 375 responses. Eight snapshots had complete judged domain coverage. Harmful-compliance estimates were low; variation arose mainly from benign utility and safe redirection. Seven multiplicity-adjusted contrasts involving Claude, Gemini, or GPT-5 snapshots and the GPT-5 mini and GPT-5 nano snapshots were supported, while no tested contrast between the Claude or Gemini snapshots and GPT-5 or GPT-5.5 survived correction.   The observed harmful-compliance range is a conservative, protocol-bound view from one generation per prompt with no tools, retrieval, history, or human adjudication; it is not an upper bound on operational assistance. A preregistered extension specifies how to test a wider best-worst gap using a locked split, repeated sampling, multi-turn and sandboxed-tool conditions, and domain-expert scoring.

## Metadata
- **Published**: 2026-07-24T21:36:28Z
- **Authors**: Mahdi Eslamimehr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22926v1)