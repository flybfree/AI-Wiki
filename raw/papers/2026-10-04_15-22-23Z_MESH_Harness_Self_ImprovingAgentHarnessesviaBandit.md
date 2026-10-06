---
title: MESH-Harness: Self-Improving Agent Harnesses via Bandit-Guided Compositional Evolution
published: 2026-10-04T15:22:23Z
authors: Zhiwei Shang, Yu Huo, Mingrong Gong, An Yan, Zikun Qu, Junhao Dong, Bryan Kian Hsiang Low, Chenglin Wu, Zhongxiang Dai
url: http://arxiv.org/abs/2610.05300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MESH-Harness: Self-Improving Agent Harnesses via Bandit-Guided Compositional Evolution

## Abstract
An agent harness is the code that organizes context, maintains state, and coordinates tool calls for a language model. We study how to improve the harness under a limited evaluation budget while keeping model weights fixed. Our method, MESH-Harness, organizes each harness into functional modules with explicit role-specific interfaces, allowing alternative implementations of each module to be substituted and recombined. It uses shared module representations and full-covariance LinUCB to score candidate combinations based on predicted performance and exploration value. Mixed-start coordinate ascent selects complete configurations for evaluation without enumerating the combinatorial space. Validation traces then guide local code edits, and the resulting candidates are incorporated into fixed-capacity role-specific pools for subsequent recombination. On text tasks, retrieval-augmented mathematical reasoning, code generation, and interactive scientific tasks, MESH-Harness outperforms Meta-Harness by 5.70, 7.01, 2.00, and 5.00 points, respectively, under matched candidate-evaluation budgets. Iterative harness optimization improves MESH-Harness by 5.63-7.79 points over its first-round configurations. For the reported configurations, aggregate test-time cost is 44.2% lower than that of Meta-Harness, while total cost including search is 14.6% lower. These results show that combining module-level design reuse with feedback-driven compositional search can systematically improve agent harnesses while keeping overall optimization cost under control.

## Metadata
- **Published**: 2026-10-04T15:22:23Z
- **Authors**: Zhiwei Shang, Yu Huo, Mingrong Gong, An Yan, Zikun Qu, Junhao Dong, Bryan Kian Hsiang Low, Chenglin Wu, Zhongxiang Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05300v1)