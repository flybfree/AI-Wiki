---
title: Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals
published: 2026-08-21T13:24:20Z
authors: Kavimayil P. Komarasamy, Saurabh Mathur, Ameet Soni, David M. Haas, Kristian Kersting, Sriraam Natarajan
url: http://arxiv.org/abs/2608.21079v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals

## Abstract
Adverse Pregnancy Outcomes (APOs) such as preterm birth and gestational diabetes can have long-term consequences for both the mother and child, yet an understanding of their causes remains elusive. Causal discovery in this domain is especially challenging due to a paucity of data and incomplete domain knowledge. As a result, pure data-driven methods fail, and Large Language Model (LLM) outputs remain inconsistent or contradictory. We introduce a neurosymbolic framework for generating plausible causal hypotheses that iteratively combines the broad prior knowledge of LLMs with empirical scoring on data. Our method treats the LLM as an adaptive proposal distribution, generating hypotheses that are scored against empirical data; the resulting high-scoring graphs are then used to update the LLM's context, steering subsequent generations toward more promising regions of the hypothesis space. We evaluate our approach on a real-world clinical dataset for modeling APOs and their risk factors, comparing our results against an expert-constructed causal graph. Our method recovers all expert-validated edges and identifies additional plausible causal relations not previously listed by experts, potentially providing new insights for targeted interventions.

## Metadata
- **Published**: 2026-08-21T13:24:20Z
- **Authors**: Kavimayil P. Komarasamy, Saurabh Mathur, Ameet Soni, David M. Haas, Kristian Kersting, Sriraam Natarajan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21079v1)