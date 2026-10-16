---
title: MemScope: Evolving Agent Memory Architectures through Localized Code Repair
published: 2026-10-15T03:27:34Z
authors: Miao Su, Yucan Guo, Zixuan Li, Long Bai, Zhongni Hou, Xiaolong Jin, Jiafeng Guo
url: http://arxiv.org/abs/2610.21170v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemScope: Evolving Agent Memory Architectures through Localized Code Repair

## Abstract
Agent memory architectures define how LLM agents store and reuse experience across tasks, but they are typically fixed after deployment, limiting their adaptability across task types. Recent self-evolving approaches instead adapt these memory architectures using execution feedback, typically represented as evaluation scores or compressed summaries. However, such coarse-grained feedback is insufficient for precise failure localization in current agent systems, where long-horizon task execution involves multiple interacting components. Without a precise failure location, existing approaches lack a clear code-level target for modification, leaving the update scope weakly constrained and often leading to large-scale rewrites of an otherwise capable memory architecture. We propose MemScope, a framework for evidence-grounded, localized evolution of an existing memory architecture. Its tool-using Patch Agent jointly inspects raw execution traces, runtime memory state, and current architecture code to identify repair targets and apply bounded, in-place edits under provider-identity and memory-compatibility constraints. On GAIA, the trace-and-memory inspection variant achieves 86.67% accuracy, compared with 70.00% for trace-only and 63.33% for summary-only feedback. Under xBench tasks, the evolved memory architecture improves over its original version from 49 to 55 correct answers with DeepSeek V3.2 and from 50 to 53 with Kimi K2.7 Code. On disjoint ALFWorld unseen tasks, success rises from 50.75% to 71.64%. Across archived architecture-snapshot transitions, the median code-change ratio is 4.4%. These results support fine-grained execution evidence as a basis for localized, in-place memory-architecture evolution.

## Metadata
- **Published**: 2026-10-15T03:27:34Z
- **Authors**: Miao Su, Yucan Guo, Zixuan Li, Long Bai, Zhongni Hou, Xiaolong Jin, Jiafeng Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21170v1)