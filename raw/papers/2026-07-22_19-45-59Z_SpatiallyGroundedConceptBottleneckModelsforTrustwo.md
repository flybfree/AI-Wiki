---
title: Spatially Grounded Concept Bottleneck Models for Trustworthy Breast Ultrasound Diagnosis
published: 2026-07-22T19:45:59Z
authors: Moshiur Rahman Tonmoy, Dunren Che, Haitham Y. Adarbah, Afzel Noore
url: http://arxiv.org/abs/2607.20691v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spatially Grounded Concept Bottleneck Models for Trustworthy Breast Ultrasound Diagnosis

## Abstract
Concept Bottleneck Models provide interpretable-by-design predictions by mediating diagnosis through human-understandable concepts, but in medical imaging, their trustworthiness is often limited by the quality and granularity of available supervision. In particular, predicted concept activations can be driven by irrelevant regions, leading to spatially unfaithful explanations. We study a data-centric spatially grounded Concept Bottleneck Model (SG-CBM) that leverages coarse lesion delineations as weak supervision to encourage anatomically plausible concept evidence. For breast ultrasound, we derive two clinically motivated zones from each lesion mask: (i) an in-lesion region of interest for morphology-related concepts and (ii) a posterior acoustic band for posterior phenomena. We train concept maps using a grouped spatial grounding objective and preserve semantic faithfulness with a linear bottleneck classifier. Across five-fold stratified group cross-validation, the proposed SG-CBM improves diagnostic AUROC and concept macro-AUROC while markedly increasing spatial alignment of concept evidence. We also perform a Train-corrupt/Test-clean annotation-quality stress test to quantify the impact of supervision quality on diagnosis and spatial faithfulness. Overall, the results underscore the need for data-quality-aware supervision design and systematic trustworthiness validation for deployable healthcare AI systems.

## Metadata
- **Published**: 2026-07-22T19:45:59Z
- **Authors**: Moshiur Rahman Tonmoy, Dunren Che, Haitham Y. Adarbah, Afzel Noore
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20691v1)