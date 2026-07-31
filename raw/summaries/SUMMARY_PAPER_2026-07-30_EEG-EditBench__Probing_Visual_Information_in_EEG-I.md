---
title: EEG-EditBench: Probing Visual Information in EEG-Image Retrieval Models with Controlled Image Edits
url: http://arxiv.org/abs/2607.27857v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-34-40Z_EEG_EditBench_ProbingVisualInformationinEEG_ImageR.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EEG-EditBench, a benchmark that tests how well visual decoding models retain information when images are edited. Using controlled edits of object identity, attributes, background, and presence, the authors evaluate eight state‑of‑the‑art EEG‑to‑image retrieval models on 2,137 quality‑controlled edits derived from the THINGS-EEG2 dataset.

## Key Takeaways
- Strong standard retrieval accuracy does not guarantee performance under edit conditions; models often fail to distinguish edited images that change only fine‑grained attributes.  
- The benchmark reveals that attribute modifications are the most challenging, indicating a reliance on coarse visual cues rather than detailed object properties.  
- By isolating specific edits, EEG-EditBench uncovers hidden model behavior that aggregate scores mask.

## Context
Visual decoding models aim to map EEG patterns to images without explicit labels, but their robustness is rarely tested under realistic perturbations. This work fills that gap by providing a systematic way to assess whether these models preserve visual information when the underlying image changes.

## Implications
For researchers, EEG-EditBench offers a reproducible tool to probe model reliability beyond simple accuracy metrics. Practitioners can use it to guide feature selection and improve robustness in applications where visual integrity must be maintained under edits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27857v1)
