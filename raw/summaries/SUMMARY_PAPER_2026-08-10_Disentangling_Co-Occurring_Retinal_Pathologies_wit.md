---
title: Disentangling Co-Occurring Retinal Pathologies with Saliency-Guided Sparse Expert Routing
url: http://arxiv.org/abs/2608.09752v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_15-43-43Z_DisentanglingCo_OccurringRetinalPathologieswithSal.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a sparse expert routing approach that uses guided context gating to allocate computation to specialized experts, achieving high performance on multi-disease retinal images. The model reaches macro AUC 0.912 and F1 0.653 across five disease classes in patient-disjoint cross-validation. Expert allocation is data-driven and interpretable.

## Key Takeaways
- Guided Context Gating creates spatial attention that directs feature tokens to experts based on disease-specific patterns, enabling sparse conditional computation.
- The MoE block routes expert selection dynamically, with healthy normal state and distinct pathologies like ERM and AMD isolating to dedicated experts (p < 0.001).
- Validation shows high macro AUC 0.912 ± 0.008 and F1 0.653 ± 0.014 on a five-class, patient-disjoint benchmark.

## Context
Current deep learning models treat retinal images as single inputs, ignoring the heterogeneous distribution of co-occurring diseases. This limits diagnostic accuracy and interpretability. The proposed sparse routing addresses these limitations by providing disease-specific computation pathways.

## Implications
Interpretable routing can guide clinicians to specific lesions, improving trust in AI systems. Industry adoption may accelerate multi-disease screening pipelines where transparency is required for regulatory compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09752v1)
