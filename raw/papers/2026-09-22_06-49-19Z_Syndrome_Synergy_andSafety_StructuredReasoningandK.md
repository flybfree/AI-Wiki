---
title: Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation
published: 2026-09-22T06:49:19Z
authors: Zheng Chen, ZhiCheng Du, Haoxuan Li, Peiwu Qin
url: http://arxiv.org/abs/2609.25755v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation

## Abstract
Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $\to$ K-RL) that addresses each gap: PG-CoT constrains CoT distillation under the li-fa-fang-yao paradigm to produce auditable diagnostic chains, Dynamic SFT models patient trajectories with explicit transition reasoning, and K-RL encodes deterministic pharmacological rules as rule-based DPO preference signals. Across 12 fine-tuned models and 6 zero-shot baselines, our framework substantially improves prescription quality over zero-shot baselines---with a 7B model (Mistral-7B) surpassing zero-shot GPT-5 on all three TCM evaluation metrics.

## Metadata
- **Published**: 2026-09-22T06:49:19Z
- **Authors**: Zheng Chen, ZhiCheng Du, Haoxuan Li, Peiwu Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25755v1)