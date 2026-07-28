---
title: MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift Spectrum
published: 2026-07-27T04:27:58Z
authors: Younggue Bae
url: http://arxiv.org/abs/2607.23986v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift Spectrum

## Abstract
We propose MEMOIR, a framework that segments user interaction histories into temporal windows, generates semantic behavioral memory for each period using an LLM, and aggregates current state, evolution direction, and predicted future into a single user representation. On the Electronics and Clothing_Shoes_and_Jewelry categories of Amazon Reviews 2023, MEMOIR is statistically tied with UniSRec, the strongest baseline, on aggregate NDCG@10 (0.0643 vs. 0.0641), splitting the four reported metrics 2-2: MEMOIR leads NDCG@10 and MRR, UniSRec leads HR@10 and HR@20. An ablation study finds that no single architectural component - the evolution-preserving contrastive loss, its directional-consistency term, or temporal window segmentation itself - individually explains much of MEMOIR's approximately 18% relative gain over ID-based SASRec; all four ablations land within 2% of the full model on aggregate NDCG@10. Stratifying test performance by a composite preference-drift score instead reveals where the gain concentrates: MEMOIR leads on ranking-quality metrics (NDCG@10, MRR) specifically among users at the high- and low-drift extremes of the distribution, while UniSRec leads the volume-oriented HR@10/HR@20 metrics across all drift strata and edges out MEMOIR on ranking quality in the middle band. We report this drift-stratified pattern, rather than the near-tied aggregate numbers or any single ablated component, as MEMOIR's most substantive and reproducible finding, and surface why it holds as an open question for future work.

## Metadata
- **Published**: 2026-07-27T04:27:58Z
- **Authors**: Younggue Bae
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23986v1)