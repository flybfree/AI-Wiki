---
title: Biological Amnesia in ICU Time-Series Prediction: A Drift-Adaptive Two-Stream Architecture with Temporal Retrieval
published: 2026-07-21T12:07:36Z
authors: Fatema Ferdous Tamanna, K. M. Merajul Arefin, Md. Abdul Masud
url: http://arxiv.org/abs/2607.19020v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Biological Amnesia in ICU Time-Series Prediction: A Drift-Adaptive Two-Stream Architecture with Temporal Retrieval

## Abstract
Background: Clinical decision support systems degrade silently as treatment protocols evolve, yet standard adaptation methods treat models as monolithic blocks, unable to distinguish stable patient physiology from shifting institutional practice. Methods: We propose an adaptive clinical intelligence architecture for ICU intervention prediction that structurally decouples physiological from treatment representations, confining parameter updates to the treatment stream upon a dual distributional and accuracy trigger. Automated audit logs record which treatment features drove each adaptation event and how their importance shifted. At inference, an attribution-driven Temporal RAG module grounds each prediction in patient-specific, era-matched PubMed evidence anchored to the patient's dominant physiological features. Experiments used 84,792 MIMIC-IV stays (2008-2022) under strict chronological split. Results: Drift localised entirely to the treatment stream, validating the structural prior. Selective adaptation improved vasopressor and septic shock discrimination and calibration over the static source model. A fully retrained baseline yielded marginally higher aggregate discrimination but missed 26 septic shock cases the framework correctly identified, with none in the reverse direction; retrieval consistency with the pre-adaptation source model was preserved by the framework but degraded substantially in the retrained baseline. Conclusions: Structurally constraining adaptation to drifting components while preserving stable physiological representations enables clinical AI to evolve with practice without distorting learned patient biology. This architecture offers a template for governable, interpretable deployment of adaptive models in high-stakes clinical environments.

## Metadata
- **Published**: 2026-07-21T12:07:36Z
- **Authors**: Fatema Ferdous Tamanna, K. M. Merajul Arefin, Md. Abdul Masud
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19020v1)