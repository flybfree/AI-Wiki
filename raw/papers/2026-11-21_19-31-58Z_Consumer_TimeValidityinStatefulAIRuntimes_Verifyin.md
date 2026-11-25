---
title: Consumer-Time Validity in Stateful AI Runtimes: Verifying Recovered State and Deferred Authority
published: 2026-11-21T19:31:58Z
authors: Guijia Zhang, Huihao Jing, Bing Li, Shing-Chi Cheung, Harry Yang, Ziqi Zhang
url: http://arxiv.org/abs/2611.29004v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Consumer-Time Validity in Stateful AI Runtimes: Verifying Recovered State and Deferred Authority

## Abstract
Stateful LLM serving engines and agent runtimes reuse execution state and deferred permissions across components and sessions. A cancellation, rollback, or approval is recorded by one component and relied on by another, and recording it does not make the later use valid: a downstream consumer may read state or dispatch an action whose identity, production status, allocation, or target revision has since changed. We call the missing check consumer-time validity and separate two forms. State validity governs what a consumer reads. On vLLM with LMCache, an interrupted KV load leaves unwritten blocks indexed, and a host-only counter rewind desynchronizes the GPU position, so a second tenant generates a schema-valid tool call naming the wrong tenant in 10/10 native-fault runs; the call is recorded and not executed. Authority freshness governs what a consumer executes: on a multi-session approval runtime, an unrevoked deferred grant overwrote a newer revision in one admitted live execution. Output equality cannot test state validity: a fault-free run diverges at token 30 through BF16 batching alone while attended-KV digests match. We therefore specify consumer-bound recovery contracts that, for state recovery, jointly require exclusion, retention, and task completion, and an admissible-witness standard realized as a GPU-free offline trace verifier over scheduler metadata and persisted tool artifacts. On recorded traces the verifier agrees with the reference verdicts in 42/42 frozen GPU-matrix scenarios. An allocation-aware repair satisfies 7/7 triggered vLLM fault predicates on a pinned scheduler-case matrix, where upstream PR 61769 satisfies 2/7, and revision-bound dispatch blocks all 160 deterministic conflicting overwrites in a separate dispatcher cohort. Recovery must be checked where state and authority are consumed, with evidence bound to the consuming request.

## Metadata
- **Published**: 2026-11-21T19:31:58Z
- **Authors**: Guijia Zhang, Huihao Jing, Bing Li, Shing-Chi Cheung, Harry Yang, Ziqi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.29004v1)