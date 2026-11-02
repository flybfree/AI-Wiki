---
title: Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation
published: 2026-10-29T07:07:17Z
authors: Chengyu Yang, Yunxiang Zheng, Zongzheng Li, Jiamei Li, Boxun Lan, Xiaoyu Liu, Xiaoyu Zhang, Xiaohong Chen, Ming Hu
url: http://arxiv.org/abs/2610.39508v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation

## Abstract
Self-evolving agent skills enable AI agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. However, since such skills are typically represented as textual documents and executed through LLM reasoning, even previously learned procedures must be repeatedly interpreted and regenerated, introducing avoidable uncertainty into every execution. In contrast, program execution is deterministic and independently verifiable. Intuitively, transforming well-specified operations into executable programs can reduce reliance on LLM reasoning and, consequently, reduce execution uncertainty. Motivated by this intuition, we introduce SKillCompiler, a self-evolving skill framework that integrates programmatic compilation into the skill evolution process. Specifically, SkillCompiler adopts an executability-aware skill compilation strategy that decomposes skills into fine-grained operations, analyzes their executability, and constructs hybrid skill skeletons that retain LLM reasoning for context-dependent operations while compiling well-specified ones into validated programs. To avoid redundant program synthesis and enable executable knowledge to accumulate across evolving skills, we further design a program asset reuse mechanism that organizes validated programs as reusable assets, retrieves existing implementations whenever applicable, and synthesizes and verifies new programs only when necessary. Extensive experiments on five benchmarks and six model families demonstrate that SkillCompiler consistently outperforms state-of-the-art methods, achieving up to 32.33\% improvement in task performance.

## Metadata
- **Published**: 2026-10-29T07:07:17Z
- **Authors**: Chengyu Yang, Yunxiang Zheng, Zongzheng Li, Jiamei Li, Boxun Lan, Xiaoyu Liu, Xiaoyu Zhang, Xiaohong Chen, Ming Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.39508v1)