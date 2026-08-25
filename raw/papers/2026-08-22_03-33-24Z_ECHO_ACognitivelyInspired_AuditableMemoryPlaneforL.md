---
title: ECHO: A Cognitively Inspired, Auditable Memory Plane for Long-Horizon Agents
published: 2026-08-22T03:33:24Z
authors: Yu Qian, Hong Miao, Boyang Guo, Tingyi Jiang, Shan Zhao, Tianxing Le, Lintian Li, Meng Liu
url: http://arxiv.org/abs/2608.21755v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECHO: A Cognitively Inspired, Auditable Memory Plane for Long-Horizon Agents

## Abstract
Long-horizon agents need memory that identifies relevant experience, resolves revisions, and exposes checkable provenance. We present ECHO (Embodied Context and History Orchestration), an auditable memory architecture and service prototype inspired by episodic encoding, consolidation, contextual reinstatement, reconsolidation, and executive control. This is functional inspiration, not neural equivalence; the empirical analysis focuses on retrieval and context construction. Development runs reach 96.29% Hit@10 and 73.64% turn Recall@5 on 1,536 LoCoMo category 1-4 questions, and 97.60% Hit@10, 88.84% turn Recall@5, and 88.71% session Recall@5 on all 500 LongMemEval-S questions. A five-history BEAM gate fails, and in a separate matched 91-question QA sample Mem0 OSS scores 64.84% versus ECHO's 41.76% (exact McNemar p = 0.00107), with a history-cluster interval crossing zero. A post-hoc audit found source-specific phrases in the query-expansion rules. Although no gold answer field entered the runtime, expansion-enabled retrieval scores are therefore descriptive development measurements, not independent confirmation.

## Metadata
- **Published**: 2026-08-22T03:33:24Z
- **Authors**: Yu Qian, Hong Miao, Boyang Guo, Tingyi Jiang, Shan Zhao, Tianxing Le, Lintian Li, Meng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21755v1)