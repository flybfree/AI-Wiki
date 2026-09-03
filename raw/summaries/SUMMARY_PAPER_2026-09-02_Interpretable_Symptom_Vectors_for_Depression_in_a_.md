---
title: Interpretable Symptom Vectors for Depression in a Large Language Model
url: http://arxiv.org/abs/2609.01832v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_20-07-03Z_InterpretableSymptomVectorsforDepressioninaLargeLa.md
generated_at: 2026-09-02 20:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how depressive symptoms are encoded within the Gemma‑3‑27B-PT language model by examining its residual activations during symptom descriptions from validated clinical instruments. The authors show that symptom groups are geometrically distinct at layer 21 and that projecting naturalistic text onto these layers yields per‑symptom coefficients that preserve clinician‑rated ordering across mood, somatic, and suicidality dimensions. A single depression vector in this layer separates depressive from non‑depressive speech with AUC 0.789.

## Key Takeaways
- The residual activation at layer 21 creates geometrically separated symptom groups, indicating a clear internal representation of different symptom categories.
- Projecting held‑out naturalistic text onto these layers produces per‑symptom coefficients that align exactly with the rank ordering established by clinicians on mood, somatic, and suicidality axes.
- A single depression vector in layer 21 discriminates depressive from non‑depressive speech with an AUC of 0.789, serving as a reliable emotional valence gate.

## Context
Current AI models treat mental health symptoms as a monolithic severity score, obscuring the nuanced symptom profiles that clinicians rely on for diagnosis and treatment planning. This study demonstrates that deep neural networks can encode these nuanced dimensions in their internal representations, offering a pathway to more interpretable diagnostic tools.

## Implications
For mental‑health practitioners, this mechanism provides a concrete way to extract clinically meaningful symptom signals directly from model activations, potentially enabling automated risk stratification without sacrificing interpretability. In industry, the approach could be integrated into AI‑assisted care platforms to improve patient communication and reduce bias in symptom assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01832v1)
