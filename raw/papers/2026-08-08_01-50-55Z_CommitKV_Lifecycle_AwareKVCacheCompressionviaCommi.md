---
title: CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents
published: 2026-08-08T01:50:55Z
authors: Weizhong Huang, Jinchao Zhang, Xiawu Zheng
url: http://arxiv.org/abs/2608.07855v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents

## Abstract
Multi-turn Reasoning-and-Acting (ReAct) agents accumulate growing trajectories of reasoning, tool calls, and observations. Their key-value (KV) caches grow accordingly, increasing memory use and attention cost during model inference. Existing KV cache compression methods reduce these costs by evicting states with low attention scores. However, low attention in the current turn does not imply future irrelevance, as temporarily inactive information may become important later. Snapshot-based eviction methods therefore do not explicitly distinguish temporarily dormant information from information that appears to have completed its role. In this paper, we present CommitKV, which identifies KV lifecycles through commit transitions. Specifically, CommitKV first divides completed agent events into token pages and compares each eligible page's deletion effect before a tool-call commit and after the commit's returned observation has been incorporated. Based on these paired measurements, CommitKV distinguishes dormant pages from high-to-low completion candidates. It then applies a greedy joint test, accepting candidates for retirement only when their combined post-commit effect remains bounded. Finally, at a later compression checkpoint, accepted pages are excluded, a bounded set of pages awaiting post-commit measurement is protected, and the remaining KV states are retained within the cache budget using the same token indices for keys, values, and absolute positions. These mechanisms ensure that CommitKV can distinguish dormant information from information that has completed its observed role and can be safely removed. Experiments on various benchmarks show that CommitKV reduces agent memory use, accelerates end-to-end inference, and achieves higher accuracy than existing KV cache compression methods.

## Metadata
- **Published**: 2026-08-08T01:50:55Z
- **Authors**: Weizhong Huang, Jinchao Zhang, Xiawu Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07855v1)