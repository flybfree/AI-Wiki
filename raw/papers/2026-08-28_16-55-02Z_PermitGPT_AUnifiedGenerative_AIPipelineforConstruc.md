---
title: PermitGPT: A Unified Generative-AI Pipeline for Construction Hazard Forecasting, Permit Prediction, and Community Impact
published: 2026-08-28T16:55:02Z
authors: Mohd Ruhul Ameen, Farjana Aktar, Akif Islam, Momen Khandoker Ope, Abu Saleh Musa Miah, Jungpil Shin
url: http://arxiv.org/abs/2608.28728v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PermitGPT: A Unified Generative-AI Pipeline for Construction Hazard Forecasting, Permit Prediction, and Community Impact

## Abstract
Urban construction governance requires early decisions that connect workplace safety, permitting requirements, and community impact, yet the relevant evidence is often scattered across separate municipal and regulatory data sources. This paper presents PermitGPT, a unified generative artificial intelligence framework for converting unstructured construction permit descriptions into structured decision-support outputs across three domains: safety hazard identification, permit requirement specification, and community impact assessment. To address data fragmentation, we spatially and temporally align records from the New York City Department of Buildings, Occupational Safety and Health Administration, and NYC 311 service requests, producing 90,000 structured prompt-response pairs derived through rule-based alignment and domain-informed spot checking. We fine-tune three open-weight language models using parameter-efficient adaptation and evaluate them on 2,833 held-out test cases. The results show complementary model behavior: Gemma-3-1B provides the most efficient inference at 3.07 samples per second with low memory usage, Llama-3.2-3B gives the highest lexical overlap for regulatory-style outputs with a BLEU score of 0.0091, and 4-bit Mistral-7B-Instruct-v0.3 achieves the strongest semantic alignment with a BERTScore-F1 of 0.7747. Because the task involves open-ended structured generation, low BLEU values are interpreted alongside semantic metrics and qualitative output structure rather than as standalone indicators of utility. Overall, PermitGPT provides an initial step toward AI-assisted construction governance while identifying directions for stronger task-level evaluation and real-world validation.

## Metadata
- **Published**: 2026-08-28T16:55:02Z
- **Authors**: Mohd Ruhul Ameen, Farjana Aktar, Akif Islam, Momen Khandoker Ope, Abu Saleh Musa Miah, Jungpil Shin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28728v1)