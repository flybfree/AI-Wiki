---
title: HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification
published: 2026-08-07T13:19:40Z
authors: Zhenchao Wang, Xin Chen, Luoxi Zhang, Min Yang, Shiwen Ni
url: http://arxiv.org/abs/2608.07204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification

## Abstract
Scientific claim verification over a cited paper requires predicting the claim--paper relation and identifying the paragraphs that justify that prediction. This setting poses two linked challenges: within-paper distractors often resemble genuine evidence, while a classifier trained on gold evidence must operate on retrieved evidence at inference. We present HNR-DAC, a two-stage framework that trains each stage on the cases it will actually encounter. Hard-Negative Reranking (HNR) quantifies evidence confusability using a base reranker's scores on non-gold paragraphs and contrasts gold evidence against the most confusable candidates. Distribution-Aligned Classification (DAC) trains on the Top-1 paragraph produced by the same frozen HNR used to construct inference inputs, while HNR's Top-3 paragraph identifiers provide the evidence output. On the NLPCC 2026 Task 10 Track 2, the final configuration obtains 97.21% Hit@3, 95.79% Macro-F1, 94.47% Joint@3, and an average score of 95.13%. The corresponding submission ranks third on the official Track 2 leaderboard while achieving the highest overall Macro-F1 of 93.05%, alongside 70.16% Joint@3 and an average score of 81.61%.

## Metadata
- **Published**: 2026-08-07T13:19:40Z
- **Authors**: Zhenchao Wang, Xin Chen, Luoxi Zhang, Min Yang, Shiwen Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07204v1)