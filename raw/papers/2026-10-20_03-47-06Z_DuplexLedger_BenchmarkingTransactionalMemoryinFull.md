---
title: DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents
published: 2026-10-20T03:47:06Z
authors: Yuxuan Li, Xiangchen Guan, Kunrong Li, Jin Wang, Kaiwen Luo, Yang Xiao, Yufei Guo, Zhisheng Chen, Liang Lin, Kun Wang
url: http://arxiv.org/abs/2610.27581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents

## Abstract
Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer. We introduce DuplexLedger, a bilingual benchmark of 1,094 persistent sessions aligning four full-duplex scenarios with event-level Write/Update/Ignore/Retain supervision, explicit pre/post memory states, and 6,564 same-session questions and checks. Evaluating five full-duplex models reveals an interaction-memory gap: no system combines strong boundary control with coherent final-state memory, and the best final-state fact coverage is 2.01%. We propose ACT-Mem, an 8.92M-parameter sidecar comprising an event controller, a versioned transactional ledger, and a typed retriever coupled with a frozen MiniCPM-o 4.5 backbone. On 219 held-out sessions, ACT-Mem increases latest-value accuracy from 4.11% to 8.68% while reducing stale assertions and distractor adoption. It improves interaction boundaries but slows interruption stopping. These results motivate selective, auditable full-duplex memory rather than indiscriminate transcript retention. Code is available at https://github.com/lyx-researcher/DuplexLedger.

## Metadata
- **Published**: 2026-10-20T03:47:06Z
- **Authors**: Yuxuan Li, Xiangchen Guan, Kunrong Li, Jin Wang, Kaiwen Luo, Yang Xiao, Yufei Guo, Zhisheng Chen, Liang Lin, Kun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27581v1)