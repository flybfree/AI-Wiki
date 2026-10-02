---
title: Self-Evolving Coding Rules for AI Coding Agents
published: 2026-09-30T19:51:41Z
authors: Zhengyuan Jiang, Reachal Wang, Yuepeng Hu, Yupu Wang, Yuqi Jia, Neil Zhenqiang Gong
url: http://arxiv.org/abs/2610.00650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Coding Rules for AI Coding Agents

## Abstract
The performance of AI coding agents is highly dependent on their underlying coding rules. However, existing coding rules are typically hand-crafted and fixed, making the process labor-intensive and often suboptimal. In this work, we propose RuleEvolve, a self-evolving framework for coding rules. RuleEvolve maintains a pool of candidate coding rules and iteratively improves them. In each iteration, it employs an LLM-powered mutator module to generate variants from existing candidates, and then uses a judge module to evaluate these variants and update the pool with the best-performing ones. Extensive evaluations across two coding-agent frameworks, four backbone LLMs, and three benchmarks demonstrate that RuleEvolve outperforms both manual engineering and existing prompt optimization baselines in terms of functional correctness of the generated code, code length, and/or generation cost (e.g., tokens used).

## Metadata
- **Published**: 2026-09-30T19:51:41Z
- **Authors**: Zhengyuan Jiang, Reachal Wang, Yuepeng Hu, Yupu Wang, Yuqi Jia, Neil Zhenqiang Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00650v1)