---
title: ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI
published: 2026-07-10T17:47:38Z
authors: Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani, Bhupesh Kumar Mishra, Tejal Shah, Zhibao Mian
url: http://arxiv.org/abs/2607.09649v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI

## Abstract
Concept-based explainable artificial intelligence (AI) can make model reasoning more human-understandable, but concept-level outputs are not automatically trustworthy. We introduce ConceptSMILE, a model-agnostic perturbation-based auditing framework for evaluating the reliability of concept-based explanations. Rather than replacing SMILE, ConceptSMILE extends its perturbation-based logic from feature- or region-level attribution to the auditing of human-understandable concept explanations. The framework perturbs input regions, measures concept-response shifts, applies locality weighting, and fits an XGBoost surrogate to approximate local concept behaviour. Reliability is assessed through attribution accuracy, surrogate fidelity, faithfulness, stability, and consistency. We evaluate ConceptSMILE on retinal fundus images by comparing MedSAM-derived visual concepts with VLM-based semantic concepts. Results show that reliability varies across concepts and pathways: MedSAM achieves stronger spatial attribution and the highest surrogate fidelity ($R^2 = 0.8503$, $R_w^2 = 0.8465$), while the VLM pathway shows stronger vessel faithfulness and stronger stability under selected artefact conditions. ConceptSMILE provides an independent audit layer for evaluating the trustworthiness of concept-based XAI.

## Metadata
- **Published**: 2026-07-10T17:47:38Z
- **Authors**: Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani, Bhupesh Kumar Mishra, Tejal Shah, Zhibao Mian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.09649v1)