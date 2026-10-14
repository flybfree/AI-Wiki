---
title: Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents
published: 2026-10-13T09:41:12Z
authors: Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
url: http://arxiv.org/abs/2610.18052v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents

## Abstract
Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval, and organization, so whether agents can forget at the user's explicit request remains under-evaluated. To address this gap, we propose Bemula, the first benchmark dedicated to memory unlearning. It comprises 50 multi-session dialogue instances, 135 forget requests of six types, and 1,742 test questions. Each dialogue has a control version without the requests, so that only systems that have stored the target can earn credit for forgetting. Across the paired versions, five test suites measure storage, removal of the requested information, preservation of unrelated memories, relearning of similar facts, and resistance to extraction attacks. On Bemula, we evaluate six mainstream memory systems under three backbone LLMs, together with the Full Context LLM on two of them. The results are negative. Across all evaluated systems and backbones, no system passes more than 1.5% of forget requests end to end, and most pass none at all. These systems either leave the requested information extractable under simple attacks or delete far more than requested. Memory unlearning therefore remains an open challenge for agent memory design. We release our data and code at https://github.com/Nboxff/bemula-benchmark.

## Metadata
- **Published**: 2026-10-13T09:41:12Z
- **Authors**: Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18052v1)