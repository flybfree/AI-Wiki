---
title: Benchmarking Hybrid Deep Research Across Database Querying and Web Search
published: 2026-09-08T20:05:09Z
authors: Ruofan Wu, Peiran Xu, Xiaolong Li, Fan Shu, Soyoung Yoon, Yite Wang, Xiaodong Yu, Boyi Liu, Feng Yan, Debiao Li, Yuxiong He, Zhewei Yao
url: http://arxiv.org/abs/2609.09410v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Hybrid Deep Research Across Database Querying and Web Search

## Abstract
While autonomous agents have made significant strides in "deep research" by iteratively navigating the open web to synthesize information, real-world problem-solving is rarely confined to a single environment. Complex analytical tasks inherently require agents to weave together evidence from both ambiguous unstructured text (e.g., the open web) and highly precise structured data (e.g., relational databases). However, existing benchmarks evaluate these modalities in isolation, failing to capture the critical "handoff" - the ability to preserve constraints when moving evidence between systems. We introduce HybridDeepResearch, to our knowledge the first deep-research benchmark that requires both web search and SQL to form a complete, verifiable answer. The benchmark contains 380 tool-dependent tasks grounded in LiveSQLBench-Base-Lite databases and public web corpora, validated through automated checks and human review, and covering three reasoning patterns: SQL2S, S2SQL, and Parallel. Evaluations across proprietary and open-weight models under various agentic scaffolds reveal that even state-of-the-art models like GLM-5.2, Claude-Sonnet-4.6 and GPT-5 achieve only about 50-54% Pass@8 on the hard subset. Notably, results show that directional reasoning is substantially more difficult than parallel intersection, highlighting that bridging structured and unstructured information spaces without losing constraints remains a major open challenge for agentic systems. Code and datasets are publicly available at GitHub (https://github.com/Snowflake-AI-Research/HybridDeepResearch) and Hugging Face (https://huggingface.co/datasets/Snowflake/HybridDeepResearch).

## Metadata
- **Published**: 2026-09-08T20:05:09Z
- **Authors**: Ruofan Wu, Peiran Xu, Xiaolong Li, Fan Shu, Soyoung Yoon, Yite Wang, Xiaodong Yu, Boyi Liu, Feng Yan, Debiao Li, Yuxiong He, Zhewei Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09410v1)