---
title: When More References Hurt: Contamination-Aware DINOv2 Memory Banks for Few-Shot Steel Defect Detection
url: http://arxiv.org/abs/2608.22082v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_19-02-40Z_WhenMoreReferencesHurt_Contamination_AwareDINOv2Me.md
generated_at: 2026-08-24 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses contamination in reference banks for patch-memory anomaly detectors and introduces a contamination-aware approach that filters out anomalous patches from unverified images. It demonstrates that trimming suspicious patches reduces residual contamination significantly compared to naive methods. The proposed method yields higher AUPRC on the Severstal dataset.

## Key Takeaways
- The study shows that additional industrial images often contain a non‑negligible proportion of anomalous patches, with 9.46% in this case, and that explicitly trimming these suspicious patches can reduce contamination to just 2.59%.  
- Using the proposed greedy coreset selection on a fixed patch budget improves AUPRC from 0.0950 (naive) to 0.1084, outperforming random removal (0.0952) and eight clean images (0.1030).  
- Injecting only 0.5% anomalous patches into a clean bank drops AUPRC from 0.1030 to 0.0759, highlighting sensitivity to reference purity.

## Context
Patch‑memory anomaly detectors rely on a set of normal images as a reference bank to score candidate defects. When the reference bank is contaminated with anomalous patches, the detector’s performance degrades because it may treat some defect candidates as normal. This paper contributes a principled way to assess and clean such contamination before training.

## Implications
For industry, this approach allows practitioners to safely incorporate unverified images into their anomaly detection pipelines without sacrificing accuracy. Practitioners can focus on filtering rather than discarding data, improving resource efficiency while maintaining high detection rates. The methodology sets a new standard for reference bank design in few‑shot visual learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22082v1)
