---
title: Self-Evolving Beyond Human-Crafted Experience for EDA Scripting
published: 2026-11-19T23:55:30Z
authors: Yang Liu, Shengbo Tong, Xiyuan Chen, Shiwei Hou, Sen Yuan, Hao Wang, Yanfeng Li, Hongwen Li, Yiming Zhu, Zhuolun He, Wenjian Yu
url: http://arxiv.org/abs/2611.26912v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Beyond Human-Crafted Experience for EDA Scripting

## Abstract
The growing complexity of electronic systems demands efficient design flows, yet EDA scripting remains a bottleneck: proprietary APIs are sparsely documented, and errors often appear as silent failures or cryptic exceptions. Hand-crafted knowledge helps but is difficult to maintain as toolchains evolve. We present ZhuLong-SE (Self-Evolution), an execution-grounded LLM agent that learns reusable knowledge from prior task traces. Building on ZhuLong, it enhances the task-level harness with API retrieval, documentation responses, isolated sandbox execution, and static checking, then adds governed cross-task self-evolution. Beyond solving individual tasks, ZhuLong-SE distills past execution traces into a three-tier memory store governed by ground-truth anchoring, disconfirmation filtering, held-out rollback, and anti-leakage retrieval. On the 158-task EDA-Eval-PyAether benchmark, the full task-level harness, with self-evolution disabled, achieves 92.4% pass@1 and outperforms ZhuLong on all five tested LLM backbones. On a harder instance-disjoint test set, self-evolution from the bare configuration surpasses a human-crafted-experience baseline by 2.5 percentage points (80.0% vs. 77.5% pass@1).

## Metadata
- **Published**: 2026-11-19T23:55:30Z
- **Authors**: Yang Liu, Shengbo Tong, Xiyuan Chen, Shiwei Hou, Sen Yuan, Hao Wang, Yanfeng Li, Hongwen Li, Yiming Zhu, Zhuolun He, Wenjian Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.26912v1)