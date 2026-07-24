---
title: Spatially Grounded Concept Bottleneck Models for Trustworthy Breast Ultrasound Diagnosis
url: http://arxiv.org/abs/2607.20691v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
generated_at: 2026-07-23 22:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a spatially grounded Concept Bottleneck Model (SG-CBM) that uses coarse lesion masks to improve trustworthy breast ultrasound diagnosis by producing concept explanations that align with anatomy. Experiments show higher AUROC and better spatial alignment compared to prior methods, demonstrating the value of data‑centric supervision.

## Key Takeaways
- The model leverages coarse lesion delineations as weak supervision to guide concept activations toward anatomically plausible regions such as in‑lesion morphology zones and posterior acoustic bands.  
- Grouped spatial grounding encourages the network to produce evidence that matches these clinical zones, preserving semantic faithfulness through a linear bottleneck classifier.  
- Validation across five‑fold stratified group cross‑validation reveals improved diagnostic AUROC and concept macro‑AUROC while markedly increasing spatial alignment of concept evidence.

## Context
Medical AI models often sacrifice interpretability for accuracy, creating explanations that are not grounded in the image’s physical structure. This work addresses that gap by integrating clinical zone definitions directly into the training objective, offering a pathway toward explainable diagnostics without sacrificing performance.

## Implications
Clinicians can rely on ultrasound reports that include spatially coherent concept maps, enhancing trust and facilitating regulatory approval. The approach also provides a template for future AI systems where weak supervision is combined with spatial grounding to ensure both accuracy and interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20691v1)
