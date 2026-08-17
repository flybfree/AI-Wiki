---
title: MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Verification-Guided Refinement
published: 2026-08-14T11:51:12Z
authors: Lushi Pu, Weiming Zhang, Xinheng Xie, Zixuan Fu, Bingxiang He, Hengyu Zhao, Hongya Lyu, Xin Li, Jie Zhou, Yudong Wang
url: http://arxiv.org/abs/2608.14221v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Verification-Guided Refinement

## Abstract
Autoformalization is commonly framed as translating natural-language mathematical statements into machine-verifiable formal languages such as Lean 4. However, faithful formalization requires more than translation. Models must map mathematical concepts to the complex hierarchy of types and definitions in formal libraries such as Mathlib, while ensuring that generated statements preserve the meaning of the source propositions. Existing approaches struggle because they rely heavily on the model's parametric memory for library-specific knowledge, while common data construction pipelines often resort to filtering single-pass outputs and lack mechanisms for feedback-driven revision. To address these challenges, we introduce MathForm, an autoformalization framework for constructing verified training data through Mathlib knowledge retrieval and verification-guided iterative refinement. Before generation, a retrieval planner gathers relevant definitions and existing formalizations from Mathlib to guide the formalization generator. Generated statements are then revised using compiler diagnostics and semantic-consistency feedback. Using this framework, we construct FormalVerse, a Lean 4 dataset containing approximately 367K verified examples across diverse mathematical domains and sources. We then train MathForm-8B through supervised fine-tuning followed by reinforcement learning. Across six benchmarks, MathForm-8B achieves average Pass@8 rates of 88.06% under Syntax Check (SC) and 72.37% under Consistency Check (CC), outperforming multiple specialized 32B autoformalizers. On the challenging FATE-H and FATE-X subsets, it attains CC pass rates of 63% and 37%, exceeding the strongest specialized baselines in both cases.

## Metadata
- **Published**: 2026-08-14T11:51:12Z
- **Authors**: Lushi Pu, Weiming Zhang, Xinheng Xie, Zixuan Fu, Bingxiang He, Hengyu Zhao, Hongya Lyu, Xin Li, Jie Zhou, Yudong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14221v1)