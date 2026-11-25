---
title: Consumer-Time Validity in Stateful AI Runtimes: Verifying Recovered State and Deferred Authority
url: http://arxiv.org/abs/2611.29004v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-21_19-31-58Z_Consumer_TimeValidityinStatefulAIRuntimes_Verifyin.md
generated_at: 2026-11-24 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper identifies "consumer-time validity" as the missing check in stateful LLM serving engines and agent runtimes, where a cancellation, rollback, or approval recorded by one component is relied on by another even though the downstream consumer may read state or dispatch an action whose identity, production status, allocation, or target revision has since changed. It separates two forms: state validity (what a consumer reads) and authority freshness (what a consumer executes), and shows that output equality cannot detect state-validity failures—a fault-free run diverges at token 30 through BF16 batching alone while attended-KV digests match. The authors specify consumer-bound recovery contracts requiring exclusion, retention, and task completion, and realize an admissible-witness GPU-free offline trace verifier over scheduler metadata and persisted tool artifacts that agrees with reference verdicts in 42/42 frozen GPU-matrix scenarios.

## Key Takeaways
- On vLLM with LMCache, an interrupted KV load leaves unwritten blocks indexed and a host-only counter rewind desynchronizes the GPU position; a second tenant then generates a schema-valid tool call naming the wrong tenant in 10/10 native-fault runs, and the call is recorded rather than executed.
- Authority freshness is distinct from state validity: on a multi-session approval runtime, an unrevoked deferred grant overwrote a newer revision in one admitted live execution.
- An allocation-aware repair satisfies 7/7 triggered vLLM fault predicates on a pinned scheduler-case matrix (upstream PR 61769 satisfies only 2/7), and revision-bound dispatch blocks all 160 deterministic conflicting overwrites in a separate dispatcher cohort; recovery must be checked where state and authority are consumed, with evidence bound to the consuming request.

## Context
Stateful LLM serving and agent runtimes increasingly reuse execution state and deferred permissions across components and sessions, so correctness depends on whether a later consumer can safely rely on earlier recorded events. This is especially relevant as serving stacks such as vLLM with LMCache and multi-session approval/agent systems become more interconnected and production-critical. The paper argues that recording an event is not equivalent to making its later use valid, a gap that output-level checks and digest comparisons cannot close.

## Implications
Practitioners should treat recovery verification as a consumer-bound, request-scoped check rather than a one-time post-hoc validation, and should bind evidence to the consuming request. For the field, this shifts the reliability bar from "the run completed" to "the state and authority consumed were still valid at consumption time," motivating GPU-free trace verifiers, allocation-aware repairs, and revision-bound dispatch in production serving and agent infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29004v1)
