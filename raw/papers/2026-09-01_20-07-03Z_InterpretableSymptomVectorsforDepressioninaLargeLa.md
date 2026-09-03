---
title: Interpretable Symptom Vectors for Depression in a Large Language Model
published: 2026-09-01T20:07:03Z
authors: Fangyi Zhu, Ajay Subramanian, Allison Constant, Camille Wang, Ravish Gupta, Corey J. Keller
url: http://arxiv.org/abs/2609.01832v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretable Symptom Vectors for Depression in a Large Language Model

## Abstract
Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using mechanistic interpretability techniques. Recording activations across symptom descriptions drawn from validated clinical instruments, we found that symptom groups geometrically separated the most at layer 21 across multiple distance metrics. Using Semantic Projection, we then projected held-out naturalistic text onto Symptom Vectors constructed from these instruments. The resulting per-symptom coefficients preserved clinician-annotated rank ordering across mood, somatic, and suicidality axes. Furthermore, a single depression vector in Layer 21 separates held-out depressive from non-depressive text (AUC = 0.789), which can be used as an emotional valence gate that restricts symptom projection to depressive speech. These results reveal a decorrelated, clinician-aligned symptom signal readable directly from internal activations, offering a mechanistic foundation for interpretable depression-assessment tools.

## Metadata
- **Published**: 2026-09-01T20:07:03Z
- **Authors**: Fangyi Zhu, Ajay Subramanian, Allison Constant, Camille Wang, Ravish Gupta, Corey J. Keller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01832v1)