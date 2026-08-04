---
title: Bridging the English-Arabic Medical Knowledge Gap: Targeted Low-Rank Adaptation via Causal Layer Selection
published: 2026-07-31T18:43:07Z
authors: Chaimae Abouzahir, Musa Khan, Hala Ali-Hassan, Congbo Ma, Khaled Saleh, Yousra Sadqi, Jihad Mallat, Walid Al-Eisawi, Nizar Habash, Farah E. Shamout
url: http://arxiv.org/abs/2608.00207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bridging the English-Arabic Medical Knowledge Gap: Targeted Low-Rank Adaptation via Causal Layer Selection

## Abstract
Large Language Models (LLMs) perform strongly in English medical tasks but degrade substantially in Arabic, a gap widely attributed to limited training data. We systematically investigate this assumption via tuned lens probing and causal activation patching, and find that Arabic medical knowledge is present in intermediate model representations but fails to surface at the output. This mechanistic insight motivates a targeted adaptation strategy: rather than fine-tuning the full network, we propose Targeted Low-Rank Adaptation (TLoRA), restricted to the layer window where cross-lingual representations diverge, upstream of the output layers where the failure manifests. We evaluate TLoRA on multiple-choice medical QA, where our approach outperforms full-network LoRA, zero-shot, and few-shot baselines. We further evaluate it on short-answer generation and multi-turn clinical dialogue, where it performs competitively without the need for task-specific finetuning. We additionally introduce AraClinicDialog, a clinician-constructed Arabic medical dialogue benchmark in MSA with validated variants across four Arabic dialects. Together, these contributions demonstrate that mechanistic diagnosis can serve as a practical guide for targeted adaptation in underrepresented-language medical LLMs.

## Metadata
- **Published**: 2026-07-31T18:43:07Z
- **Authors**: Chaimae Abouzahir, Musa Khan, Hala Ali-Hassan, Congbo Ma, Khaled Saleh, Yousra Sadqi, Jihad Mallat, Walid Al-Eisawi, Nizar Habash, Farah E. Shamout
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00207v1)