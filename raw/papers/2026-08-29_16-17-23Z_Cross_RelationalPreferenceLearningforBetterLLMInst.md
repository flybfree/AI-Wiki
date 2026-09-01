---
title: Cross-Relational Preference Learning for Better LLM Instruction Following
published: 2026-08-29T16:17:23Z
authors: Runsheng Li, Kai Sun, Bin Shi, Bo Dong
url: http://arxiv.org/abs/2608.29352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Relational Preference Learning for Better LLM Instruction Following

## Abstract
Large Language Models (LLMs) still exhibit limited capability in following complex instructions. While existing approaches often rely on preference learning to enhance this ability, they typically overlook the relationships between the permissible response spaces of different instructions, which restricts a model to align with subtle and diverse constraint variations. To address this, we propose Cross-Relational Preference Learning (CRPL), a novel framework for constructing preference data that explicitly models inter-instruction relationships through two key techniques: Cross-Relationship Perturbation and Cross-Region Pair Sampling. This enables the generation of more diverse preference data that captures a wide spectrum of constraint variations. Additionally, we introduce an atomic constraint-based verification mechanism to rigorously assess response satisfaction, ensuring high-quality preference pair construction. Extensive experiments across multiple preference learning methods (e.g., DPO, KTO), LLM backbones and four instruction-following benchmarks demonstrate that our approach achieves substantial improvements over prior baselines and exhibits strong generalization.

## Metadata
- **Published**: 2026-08-29T16:17:23Z
- **Authors**: Runsheng Li, Kai Sun, Bin Shi, Bo Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29352v1)