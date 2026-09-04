---
title: CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning
published: 2026-09-03T08:24:22Z
authors: Bo Zeng, Linfeng Gao, Peiqin Lin, Yu Zhao, Mingyan Zeng, Yu Tong, Xintong Wang, Linlong Xu, Longyue Wang, Weihua Luo, Qinggang Zhang, Jinsong Su
url: http://arxiv.org/abs/2609.03526v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning

## Abstract
Multimodal language models achieve near-ceiling scores on food recognition benchmarks, yet it remains unclear whether this success reflects genuine cultural understanding or mere visual matching. To probe this distinction, we introduce CulturalMenuBench, a benchmark of 4,870 items in 10 languages across 18 regions; its 10 tasks pair final-dish and step-by-step cooking images with ingredients, procedural text, and regional labels, spanning basic recognition to process-grounded cultural attribution. Evaluating 12 models exposes a substantial knowledge-application gap: models exceeding 94% on standard multiple-choice tasks drop to at most 56% when attributing dishes to Chinese regional cuisines, despite an identical four-way format. Diagnostic analyses explain why: error patterns are consistent with random guessing, accuracy tracks visual distinctiveness rather than cultural structure, and models classify cuisines more accurately from dish names alone than from images (+7-18 points). The knowledge is thus present but cannot be activated through visual input. An ablation confirms these tasks genuinely require procedural evidence: removing sequential cooking images selectively degrades process-grounded tasks while others remain stable. Overall, CulturalMenuBench shows that near-perfect recognition can conceal an inability to apply cultural knowledge, motivating training that explicitly connects perception, procedure, and cultural context. Code and data are publicly available.

## Metadata
- **Published**: 2026-09-03T08:24:22Z
- **Authors**: Bo Zeng, Linfeng Gao, Peiqin Lin, Yu Zhao, Mingyan Zeng, Yu Tong, Xintong Wang, Linlong Xu, Longyue Wang, Weihua Luo, Qinggang Zhang, Jinsong Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03526v1)