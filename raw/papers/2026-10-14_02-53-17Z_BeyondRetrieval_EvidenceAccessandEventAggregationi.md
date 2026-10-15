---
title: Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory
published: 2026-10-14T02:53:17Z
authors: Zerui Yang, Quan Xue, Chaorui Zhang, Xueyan Niu, Xuanyu Zheng, Xiyuan Wang, Haolin Ruan, Guangcheng Song, Weixi Zhang, Wei Han, Bo Bai
url: http://arxiv.org/abs/2610.19474v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory

## Abstract
Questions about an agent's history often require aggregating events, which retrieval alone does not resolve. We combine source-preserving evidence access with executable aggregation. Trajectory Memory (TM) retains the original trajectory and constructs a source-addressable reading view at question time. TallyMem augments it with a reusable event ledger, model-generated event specifications and deterministic execution. With a commit-specific adaptation on 776 questions from 99 held-out MINTEval repositories, TallyMem raises Qwen3-32B exact match from 35.2% to 49.0%, a 13.8-point gain over TM; gains span 12.8-13.9 points across three readers. A controlled probe with event sets parsed independently from raw logs shows an 11.0-point gain, from 82.8% to 93.8%, without routing. On full AMA-Bench, the routed system yields a smaller 1.3-point gain, from 69.8% to 71.1%. These results support executable aggregation on tasks that require combining events, with benefits dependent on the task and event specification, the largest residual system-error category in our diagnostic analysis.

## Metadata
- **Published**: 2026-10-14T02:53:17Z
- **Authors**: Zerui Yang, Quan Xue, Chaorui Zhang, Xueyan Niu, Xuanyu Zheng, Xiyuan Wang, Haolin Ruan, Guangcheng Song, Weixi Zhang, Wei Han, Bo Bai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19474v1)