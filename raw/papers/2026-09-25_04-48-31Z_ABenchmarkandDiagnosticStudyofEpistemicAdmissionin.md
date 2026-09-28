---
title: A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory
published: 2026-09-25T04:48:31Z
authors: Xiaoyang Li, Yiqi Wang, Chencheng Zhu, KE XU, Wencheng Yang, Zequn Sun, Pingan Song, Yiqun Duan, Taotao Cai
url: http://arxiv.org/abs/2609.30813v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory

## Abstract
Evaluating claim admission in shared agent memory is challenging because repeated claims may be mistaken for independent evidence. An agent may copy or paraphrase a retrieved belief, while admitting a false claim exposes subsequent agents to it. To study this problem, we introduce the Correlated Promotion Benchmark (CPB), which evaluates whether candidate claims should be admitted to shared memory.CPB-Static constructs a frozen test split from publicly annotated sources with fixed gold actions. CPB-Live runs multi-agent teams over a shared store, records all writes and retrievals, and tracks source lineage defined by each scenario. A separate consumer answers from the store alone. We evaluate eight admission policies across four agent families. Our results show that policies which deduplicate sources reject many true claims alongside false ones, whereas policies preserving answer coverage admit nearly as many false claims as unrestricted sharing. Gating on declared source type reduces false adoption to 0.06--0.09, compared with 0.22--0.47 for other answering policies. Once an uncontested false belief enters memory, the consumer asserts it in 0.97--0.99 of probes across all families. No non-oracle policy consistently rejects false claims across verbatim copies, paraphrases, and paraphrases declared authoritative. These findings reveal the limitations of admission policies without access to source lineage.

## Metadata
- **Published**: 2026-09-25T04:48:31Z
- **Authors**: Xiaoyang Li, Yiqi Wang, Chencheng Zhu, KE XU, Wencheng Yang, Zequn Sun, Pingan Song, Yiqun Duan, Taotao Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30813v1)