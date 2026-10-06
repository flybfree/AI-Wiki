---
title: AECG: Asymmetric Experience Consolidation and Governance In Multi-Agent Systems
published: 2026-10-04T12:38:03Z
authors: Ao Tian, Jialong Liu, Daqi Zheng, Xin Sun, Mengting Li, Zhizhao Xiao, Zijian Huang, Honglei Wang, Zijian Hei, Yukun Yan
url: http://arxiv.org/abs/2610.05176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AECG: Asymmetric Experience Consolidation and Governance In Multi-Agent Systems

## Abstract
Large language model (LLM)-based multi-agent systems increasingly rely on memory to transform execution trajectories into reusable procedural knowledge. Yet repeated retrieval also makes memory errors persistent: memory pollution arises when outdated, weakly supported, or spuriously successful procedures become recurring components of future reasoning. Multi-agent execution introduces an additional structural risk. Scope collapse occurs when procedural knowledge escapes the coordination scope in which it was shown effective and is repeatedly reused at incompatible decision levels, allowing local errors to influence cascades of downstream decisions. Meanwhile, task-level failures provide ambiguous supervision because they rarely reveal which recalled knowledge was responsible. We introduce AECG, a framework for asymmetric experience consolidation and governance for multi-agent systems. AECG turns memory from static experience storage into a dynamic reliability-governance loop, preserving coordination scope and using multi-scale, confidence-aware reliability to detect degradation. It then combines degradation with downstream impact to prioritize high-risk knowledge under a bounded review budget, applies targeted interventions, and reactivates revised skills only after paired replay. Across three multi-agent frameworks and four benchmarks, AECG achieves the best score in 11 of 12 framework--benchmark settings and improves over the strongest competing memory method by as much as 10.23 percentage points; removing scope preservation reduces accuracy by up to 16.89 points. AECG thereby reframes multi-agent memory from passive accumulation into auditable reliability governance. Code is available at https://github.com/fenhg297/AECG

## Metadata
- **Published**: 2026-10-04T12:38:03Z
- **Authors**: Ao Tian, Jialong Liu, Daqi Zheng, Xin Sun, Mengting Li, Zhizhao Xiao, Zijian Huang, Honglei Wang, Zijian Hei, Yukun Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05176v1)