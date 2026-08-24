---
title: Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol
published: 2026-08-21T04:21:28Z
authors: Guodong Xu
url: http://arxiv.org/abs/2608.20729v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol

## Abstract
Language-model agents can improve after failure or carry text across episodes without revising what counts as success. We study the narrower attribution problem of criterion revision: when criterion K0 accepts an outcome violating a broader commitment B, what observations justify saying that the system formed and persistently used K1? We require five non-compensatory conditions: criterion-failure detection, a model-emitted proposal, new-episode transfer, intervention sensitivity on the claimed carrier, and preservation.   We evaluate CMB-0.1 on twelve cross-domain cases and four arms: stateless inference, append-only history, model-generated but harness-committed state, and evaluator-written oracle state. Seven mechanism fixtures yield 84 deterministic scorer trials; four local quantized artifacts yield 96 calls and 192 model-case-arm trials. No model trial satisfies all five conditions, but this zero does not establish general capability absence. Eleven calls remain invalid after one retry; several commitments disclose the target distinction; the harness performs commits; deletion reuses a stateless call; and conflict changes multiple factors. Qwen2.5-7B answers every transfer and preservation item without revision state, exposing zero-state reconstruction.   These failures make CMB-0.1 an instrument-calibration result rather than a model ranking. We derive a prospective, trace-anchored CMB-0.4 protocol requiring concealed transfer, explicit WRITE/NO-WRITE/ESCALATE actions, a separately logged policy-selected commit, matched interventions, repeated hidden items, and a frozen executable oracle. It is a successor design, not a completed confirmatory result. The paper contributes a measurement chain, an empirical diagnosis of its first implementation, and a more discriminating protocol for future tests of criterion revision.

## Metadata
- **Published**: 2026-08-21T04:21:28Z
- **Authors**: Guodong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20729v1)