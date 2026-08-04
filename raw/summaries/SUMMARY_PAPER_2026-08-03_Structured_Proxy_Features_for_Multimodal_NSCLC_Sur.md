---
title: Structured Proxy Features for Multimodal NSCLC Survival Prediction from Pretreatment CT
url: http://arxiv.org/abs/2608.00446v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_05-10-02Z_StructuredProxyFeaturesforMultimodalNSCLCSurvivalP.md
generated_at: 2026-08-03 23:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes structured proxy features derived from simulation to improve multimodal prediction of NSCLC survival using pretreatment CT, radiomics, and clinical data. It evaluates these features on the Lung1 dataset and achieves a C-index of 0.641 with iAUC 0.731, outperforming prior multimodal methods. The results suggest that simulation-derived interaction features complement conventional representations.

## Key Takeaways
- Structured proxy features are generated from entropy and sphericity to capture heterogeneity-morphology interactions, providing a novel way to augment imaging data.
- The Transformer-based Masked Autoencoder (TMAE) backbone with attention visualizations improves multimodal fusion compared to other encoders evaluated in the same pipeline.
- On Lung1, the primary four-modality fusion reaches C-index 0.641 and iAUC 0.731, significantly higher than earlier results of C-index 0.631.

## Context
This work addresses a key limitation in survival prediction where imaging features are treated independently, ignoring complex interactions between tumor heterogeneity and morphology that affect prognosis. By introducing simulation-derived proxy variables, the study advances multimodal AI by integrating structured interaction signals into radiomics pipelines. The approach aligns with broader trends toward context-aware feature engineering in medical AI.

## Implications
For clinicians and researchers, these findings suggest that incorporating structured interaction features can enhance survival prediction models without requiring additional data collection. Practitioners may integrate such proxies into existing CT-based workflows to improve risk stratification for NSCLC patients. The methodology could be extended to other cancers where imaging heterogeneity plays a role in outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00446v1)
