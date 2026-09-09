---
title: SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale
published: 2026-09-08T04:20:11Z
authors: Dawei Fu, Cheng Jiang, Sitian Qian, Huainan Wang, Zhongkai Hao
url: http://arxiv.org/abs/2609.08228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale

## Abstract
Modern LLM agents increasingly rely on reusable skills, yet as skill libraries scale to thousands of entries, effective retrieval becomes a bottleneck. Graph-of-Skills (GoS) addresses this challenge by exploiting dependency-aware graph structure for scalable skill retrieval, while SkillDAG further demonstrates that skill graphs can accumulate execution-backed structure online. However, these approaches leave open whether historical execution traces can be systematically distilled into a better retrieval graph that generalizes to unseen tasks. We present Self-Evolving Graph-of-Skills (SE-GoS), a training-free framework that evolves an existing GoS graph from execution traces while preserving the original retrieval pipeline. SE-GoS performs three complementary updates: topology evolution that discovers and prunes skill relationships from execution evidence, edge-weight evolution that reinforces retrieval-relevant relationships based on historical effectiveness, and description evolution that optimizes retrieval-facing skill descriptions using execution feedback. Across three LLMs on SkillsBench, SE-GoS consistently improves task reward while reducing input tokens relative to full skill loading, with gains varying across model families. In a representative setting, one evolution round improves reward from 52.4\% to 59.4\% while reducing input tokens by approximately one-third relative to full skill loading, and the resulting graph transfers to a disjoint held-out split with a 5.4-point improvement over the static GoS baseline. These results show that skill graphs can be improved from execution experience without model training, changes to the retrieval algorithm, or modifications to skill content, turning a static retrieval graph into an evolving retrieval infrastructure.

## Metadata
- **Published**: 2026-09-08T04:20:11Z
- **Authors**: Dawei Fu, Cheng Jiang, Sitian Qian, Huainan Wang, Zhongkai Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08228v1)