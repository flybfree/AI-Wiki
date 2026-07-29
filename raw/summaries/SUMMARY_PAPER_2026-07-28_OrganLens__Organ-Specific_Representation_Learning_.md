---
title: OrganLens: Organ-Specific Representation Learning for CT Foundation Models
url: http://arxiv.org/abs/2607.25164v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_00-25-05Z_OrganLens_Organ_SpecificRepresentationLearningforC.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OrganLens, a method for generating organ‑specific representations from raw CT scans using self‑supervision without external segmentation masks. It conditions a shared encoder on organ identity and uses anatomy‑mask supervision to create 11 organ‑specific features at inference. Results show improved performance on heart AUROC and lung C‑index compared to baseline.

## Key Takeaways
- OrganLens provides organ‑specific representations from raw CT using self‑supervision, eliminating need for segmentation masks.
- The shared encoder is conditioned by organ identity while anatomy‑mask supervision shapes features for accurate pooling.
- Downstream tasks such as cardiomegaly detection and lung cancer mortality prediction benefit significantly with anatomically matched representations.

## Context
Organ‑level representation learning in medical imaging remains limited because most foundation models output a single volume‑level embedding. Existing approaches either separate organs or lack organ‑specific conditioning, hindering clinical utility. OrganLens addresses this gap by integrating self‑supervised signals across modalities.

## Implications
Clinicians and researchers can leverage these organ‑specific embeddings for personalized risk assessment and longitudinal monitoring without costly segmentation pipelines. The framework’s scalability encourages broader adoption of modular CT foundation models in diagnostic workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25164v1)
