---
title: Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence
url: http://arxiv.org/abs/2608.06778v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_03-52-33Z_Retrieval_ConstrainedPolicyOptimizationforAttackTe.md
generated_at: 2026-08-09 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TTP-R1, a retrieval‑constrained policy optimization framework that improves CTI technique extraction from large label spaces. It achieves higher F1 scores than prior methods and runs faster as an 8B model. The best result is an average F1 improvement over Claude Sonnet 4.5.

## Key Takeaways
- Retrieval reduces the massive ATT&CK label space to a manageable candidate set, mitigating class imbalance and enabling supervised fine‑tuning.
- A fine‑tuned LLM selects correct techniques using reinforcement learning with verifiable rewards that directly penalize precision, recall, and output format errors.
- The combined approach yields a 7.4 percentage point gain in sub‑technique F1 while being 28× faster than the base model.

## Context
Automated threat analysis relies on mapping unstructured CTI to structured ATT&CK taxonomy, but label scarcity and large label spaces hinder progress. Retrieval‑augmented methods have shown promise yet lack direct supervision for set correctness. This work bridges that gap with a policy‑optimization framework.

## Implications
Practitioners can deploy TTP-R1 as an efficient service for real‑time CTI analysis, reducing annotation costs and improving detection coverage. The method sets a benchmark for retrieval‑constrained LLM fine‑tuning in security domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06778v1)
