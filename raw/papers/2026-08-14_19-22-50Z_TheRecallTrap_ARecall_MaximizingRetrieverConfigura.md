---
title: The Recall Trap: A Recall-Maximizing Retriever Configuration Reduces Issue Resolution in Fixed-Budget Code Context
published: 2026-08-14T19:22:50Z
authors: Alexander Adkins, Teimuraz Trapaidze
url: http://arxiv.org/abs/2608.14838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Recall Trap: A Recall-Maximizing Retriever Configuration Reduces Issue Resolution in Fixed-Budget Code Context

## Abstract
Retrieval components for code assistants are tuned against retrieval metrics: a configuration that raises recall@k is adopted, and downstream task success is assumed to follow. We report a controlled case study in code repair, not a new phenomenon but a deployed-flag, execution-graded instance of the known relevance-diversity and objective-mismatch tradeoff (Levy et al., 2025). On SWE-bench Verified we inject a retriever's hits as a fixed 12-slot context pack with no search tools and toggle one flag (one-chunk-per-file deduplication) on an otherwise identical stack. The flag is the higher-recall configuration (gold file present in 0.878 of served packs against 0.806 disabled), yet disabling it, trading file breadth for within-file depth, raises the single-shot resolve rate: gpt-5.6-sol +7.6pp (39.2% to 46.8%, n=500, McNemar exact p=0.0003), and a pre-registered open-weights replication any reviewer can re-run (Qwen3.6-27B, +3.6pp, n=499, p=0.0133); both survive repository-clustered inference. The gain tracks within-file anchor dose, and a random-chunk control refutes an argmax-selection artifact. We map where it holds: it reverses on a lexical BM25 retriever (-3.2pp, significant cross-paradigm interaction), is not detected under unrestricted-Read agents (a powered null), and across four languages (SWE-PolyBench, N=617) is positive but not significant (+2.6pp, p=0.056), a mapped boundary rather than a confirmed extension. Operationally, at a tight fixed budget: do not hard-deduplicate by file, and A/B packing policies against the task, not the metric the flag was tuned to.

## Metadata
- **Published**: 2026-08-14T19:22:50Z
- **Authors**: Alexander Adkins, Teimuraz Trapaidze
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14838v1)