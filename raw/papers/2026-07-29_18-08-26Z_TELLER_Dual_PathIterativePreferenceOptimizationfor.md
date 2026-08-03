---
title: TELLER: Dual-Path Iterative Preference Optimization for Table Entity Linking
published: 2026-07-29T18:08:26Z
authors: Yixin Peng, Kehao Li, Stefan Decker
url: http://arxiv.org/abs/2607.28680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TELLER: Dual-Path Iterative Preference Optimization for Table Entity Linking

## Abstract
Entity linking in tables matches short and ambiguous cell mentions to their corresponding knowledge-base entities. Existing approaches typically rely on data preprocessing pipelines that retain either compact or extensive table content as contextual evidence, and then formulate entity linking as a language generation task for instruction-tuned models; recent systems further incorporate explicit reasoning to disambiguate challenging mentions. However, their training supervision is usually static: fixed preference data cannot adapt to the residual errors of an evolving model, while variations in reasoning length can bias sequence-level preference learning. To address these limitations, we present TELLER: Table Entity Linking through Learning from Errors and Reasoning. We first retrieve and rank Wikidata candidates and retain reduced table evidence in the prompt. The direct-answer path applies iterative direct preference optimization and refreshes its preference data with residual errors from the updated model. The reasoning path uses filtered and compressed chain-of-thought rationales for supervised fine-tuning, followed by our iterative length-normalized regularized preference optimization. On the TableInstruct entity-linking subset, the direct-answer path improves accuracy from 94.35\% to 94.50\%; on the MammoTab V2 evaluation set, it improves accuracy from 87.59\% to 88.20\%. The reasoning path improves accuracy from 92.90\% to 92.95\% on TableInstruct and from 79.09\% to 81.85\% on MammoTab V2, while maintaining high rates of complete reasoning generation. These results show that iterative preference learning benefits both concise entity prediction and explicit reasoning.

## Metadata
- **Published**: 2026-07-29T18:08:26Z
- **Authors**: Yixin Peng, Kehao Li, Stefan Decker
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28680v1)