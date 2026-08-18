---
title: Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations
published: 2026-08-17T06:50:12Z
authors: Jun He, Deying Yu
url: http://arxiv.org/abs/2608.16178v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations

## Abstract
Operational telemetry is predominantly engineered for human reading: systems repeatedly serialize verbose prose, static keys, and redundant context across billions of log lines. As autonomous AI agents become primary operational consumers, feeding them traditional logs wastes scarce context capacity parsing lexical syntax rather than reasoning over system state changes -- all while lacking cryptographic guarantees of provenance or collection completeness.   This paper introduces agent-native telemetry, an operational evidence architecture for autonomous machine operators founded on verifiable state deltas rather than human prose. We present the Agent Telemetry Protocol (ATP) and the State-Delta Evidence Ledger, an implementation that structures operational facts into four core evidence primitives (Transitions, Observations, Relations, and State Checkpoints) governed by content-addressed schemas, while isolating uncurated text as digest-verified opaque references. Producers sign and hash-chain batches for atomic collector append. Verified records feed two parallel agent access paths: a stateless protocol decoder emitting compact positional rows, and a stateful semantic gateway serving bounded graph capsules. We prove an information-preservation lower bound and formalize a ledger-relative verified negative theorem for provable event non-occurrence. On distributed microservice benchmarks (AIOpsLab and OpenTelemetry Astronomy Shop), ATP reduces raw wire payload and modeled cloud query scan costs by 96.4% relative to OpenTelemetry JSON, reduces LLM context tokens by 88.8% and query operations by 66.2%, detects all 500 tested adversarial storage mutations, and yields zero successful prompt injections across 50 adversarial trials per ATP configuration.

## Metadata
- **Published**: 2026-08-17T06:50:12Z
- **Authors**: Jun He, Deying Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16178v1)