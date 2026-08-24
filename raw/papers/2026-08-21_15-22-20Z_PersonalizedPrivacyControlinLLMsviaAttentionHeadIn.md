---
title: Personalized Privacy Control in LLMs via Attention Head Intervention
published: 2026-08-21T15:22:20Z
authors: Junseok Kim, Nakyeong Yang, Kyomin Jung
url: http://arxiv.org/abs/2608.21209v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personalized Privacy Control in LLMs via Attention Head Intervention

## Abstract
The rise of agentic AI enables LLMs to access diverse user data, raising critical privacy concerns. Prior work on contextual privacy studies whether LLMs regulate information disclosure according to context-dependent norms. However, acceptable disclosure boundaries may vary across users even within the same context. To address this limitation, we introduce \textit{personalized privacy}, which incorporates user-specific disclosure preferences into privacy control. We further present P3Bench~(\textbf{P}ersonalized \textbf{P}rivacy \textbf{P}reservation \textbf{Bench}mark), a novel benchmark extending contextual privacy policies with personalized disclosure policies. Experiments show that prompt-based policies fail to reliably enforce personalized privacy policies, with Qwen2.5-7B and Gemma3-4B showing average policy ignorance ratios of 51.25\% and 74.28\%, respectively. Finally, to address this problem, we propose \textsc{Repair}, a robust inference-time attention head intervention method that adjusts disclosure behavior toward policy-consistent responses. Our method significantly improves adherence to user-specific privacy preferences by reducing cases where the model fails to follow the given policy.

## Metadata
- **Published**: 2026-08-21T15:22:20Z
- **Authors**: Junseok Kim, Nakyeong Yang, Kyomin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21209v1)