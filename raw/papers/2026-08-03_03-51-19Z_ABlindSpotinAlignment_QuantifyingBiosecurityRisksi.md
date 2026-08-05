---
title: A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models
published: 2026-08-03T03:51:19Z
authors: Shu Quan, Tianfang Hao, Sitong Fang, He Geng, Jiayi Zhou, Boyuan Chen, Kaile Wang, Donghai Hong, Juntao Dai, Yaodong Yang, Jiaming Ji
url: http://arxiv.org/abs/2608.02684v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models

## Abstract
Large Language Models (LLMs) are accelerating biological research, yet this same capability poses a critical biosecurity threat: models that assist in protein engineering can equally be prompted to generate predicted toxin-like sequences, potentially lowering the barrier to biological misuse. Current safety evaluations, however, operate in natural language and cannot determine whether a model-generated amino acid sequence is biological gibberish or a computational risk signal. To address this evaluation blind spot, we introduce SPIKE-Bench, coupling 631 curated toxin-design prompts across seven functional categories with the SPIKE funnel, a three-stage protocol that filters output through compliance, biological plausibility, and predicted toxicity, producing stage-level diagnostics and an aggregate function-aware metric: the Functional Harmfulness Rate (FHR). An audit of 32 LLMs reveals that most models freely comply with toxin-design requests; FHR is driven primarily by biological generation capability rather than safety alignment, reaching 50.7%; and Refusal Rate fails to predict functional risk. As a first step toward mitigation, we provide BioSafe-Guard, a domain-specialized classifier that substantially reduces predicted functional risk while preserving benign utility. We release SPIKE-Bench and BioSafe-Guard at https://github.com/PKU-Alignment/SPIKE-Bench to support more rigorous biosecurity evaluation of LLMs.

## Metadata
- **Published**: 2026-08-03T03:51:19Z
- **Authors**: Shu Quan, Tianfang Hao, Sitong Fang, He Geng, Jiayi Zhou, Boyuan Chen, Kaile Wang, Donghai Hong, Juntao Dai, Yaodong Yang, Jiaming Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02684v1)