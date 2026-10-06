---
title: PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents
published: 2026-10-05T03:31:51Z
authors: Yiqi Wang, Jiaqi Liu, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Taotao Cai
url: http://arxiv.org/abs/2610.05732v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents

## Abstract
LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons. Existing methods provide limited support for handling memories that become outdated as new observations or domain evidence arrive. Such outdated memories may remain semantically relevant, continue to affect dependent records, and retain value as historical evidence. This calls for two capabilities: dependency tracking to identify downstream effects and historical preservation to retain useful past records. We propose Provenance-Aware Cascading Memory Invalidation (PACMI), a framework that represents memories and new evidence in a provenance graph with typed dependency edges. PACMI assigns records to a four-state validity lattice, propagates validity changes to dependent memories, and uses the resulting states for retrieval and stale-premise detection. We also introduce a diagnostic benchmark with 100 cases and 300 queries across five domains. The evaluation separates node, context-, and answer-level performance. PACMI achieves the highest final-answer accuracy on this benchmark, and its paired difference from the strongest baseline is significant under an exact McNemar test. The premise checker achieves perfect precision, recall, and F 1 on the controlled query distribution. Cascading propagation primarily improves memorystate correctness: removing it increases final-answer errors from 3 to 11, but the paired difference does not reach the 0.05 significance threshold. Code and data will be made publicly available.

## Metadata
- **Published**: 2026-10-05T03:31:51Z
- **Authors**: Yiqi Wang, Jiaqi Liu, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Taotao Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05732v1)