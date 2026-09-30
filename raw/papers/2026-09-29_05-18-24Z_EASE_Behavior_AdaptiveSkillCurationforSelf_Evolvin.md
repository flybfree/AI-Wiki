---
title: EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents
published: 2026-09-29T05:18:24Z
authors: Zhen Xiong, Qiaoyu Tan
url: http://arxiv.org/abs/2609.36746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents

## Abstract
Agent skills provide a lightweight mechanism for self-evolving agents to accumulate reusable procedural knowledge without updating model parameters. However, existing learned skill curators typically optimize curation without explicitly modeling downstream executor behavior. We show that this can cause systematic cross-executor degradation: curators trained with different executors perform best when paired with their own training executor, indicating that effective skill curation is executor-dependent. We formulate behavior-adaptive skill curation and introduce EASE, a framework that learns a single curator that adapts its decisions to different executor behaviors. EASE maintains an online behavioral profile of recent execution patterns and conditions the curator on this profile, the current trajectory, and retrieved skills to add, modify, or remove skills from an evolving repository. We train the shared curator jointly across multiple frozen executors with reinforcement learning, using retrieval-aware and behavior-aware temporal attribution to focus optimization on curation actions with observable downstream influence. Across ALFWorld, ScienceWorld, and WebShop, with executors ranging from Qwen3-8B/32B and GPT-OSS-120B to unseen Kimi K2.6, DeepSeek V4 Flash, and Gemini 3.5 Flash, EASE outperforms strong skill- and memory-based baselines without per-executor finetuning. EASE also maintains 34.5--41.0% fewer skills, improves skill retrieval by 36.3--38.7% and measured edit utility by 51.8--60.0%, and reduces deployment-time inference tokens by 9.1--14.5%. These results establish behavior-adaptive skill curation as an effective principle for building self-evolving agents.

## Metadata
- **Published**: 2026-09-29T05:18:24Z
- **Authors**: Zhen Xiong, Qiaoyu Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36746v1)