---
title: MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data
published: 2026-10-18T16:24:33Z
authors: Sen Gao, Yongan Li, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich, Shixuan Sun
url: http://arxiv.org/abs/2610.25373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data

## Abstract
Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold. Such state is usually a derived state. No record states it, and it must be computed by rules from multiple records of an evolving history. Existing memory benchmarks score only the final answer, with no reference for the intermediate states behind it. A wrong answer therefore cannot be traced to the state that was missed, and a state that silently became outdated goes undetected. We present MemDerive, a diagnostic benchmark for agent memory over evolving data. It specifies each scenario symbolically, derives exact gold answers with Datalog, records the gold derivation DAG and the supporting events of every query, and renders the history in natural language with fictional entities and distractors. Its 10 scenarios contain 4,692 events and 1,503 queries whose difficulty varies along access, evolution, and composition. On this ground truth, MemDerive evaluates answer reliability, diagnoses failures by probing the nodes of the gold derivation DAG, and tracks whether answers stay correct as events arrive. Our evaluation of four memory systems reveals failures that final-answer benchmarks hide. On derived state, every memory system falls behind simple BM25 retrieval, although the same answer model reaches 96.01% when given the supporting events. Most failures are ungathered, as a system holds the missing intermediate state but does not retrieve it for the question that needs it. Memory systems also rarely propagate implicit changes, which no new record states. These results suggest three principles for memory design. Gather inputs along the derivation, store rules with their versions, and maintain derived states through recorded dependencies.

## Metadata
- **Published**: 2026-10-18T16:24:33Z
- **Authors**: Sen Gao, Yongan Li, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich, Shixuan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25373v1)