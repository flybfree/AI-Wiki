---
title: Stemma: Induced Decision Regions Reveal LLM Provenance
url: http://arxiv.org/abs/2607.25880v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_15-42-53Z_Stemma_InducedDecisionRegionsRevealLLMProvenance.md
generated_at: 2026-07-28 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Stemma, a method for testing LLM provenance by measuring induced decision regions, and reports that it outperforms baselines with high AUC and TPR at low FPR across many model variants. The approach abstracts surface variation into stable decision regions, allowing reliable lineage inference.

## Key Takeaways
- Induced decision regions map open-ended outputs to a finite space, preserving provenance signals despite surface-form changes.
- Stemma’s probe-selection principles combine stability, robustness, and specificity to improve detection accuracy across diverse checkpoints.
- The method achieves AUC 0.967 with 87.8% TPR at 1% FPR on 770 pairs and reaches 0.995 AUC with 93.5% TPR at 1% FPR on 1,260 deployment instances.

## Context
LLM provenance testing is critical for ensuring model integrity in commercial and research settings where models may be fine‑tuned or deployed under different conditions. Existing methods rely on response characteristics that can drift, limiting their trustworthiness. Stemma’s focus on decision regions addresses this gap by emphasizing invariance to adaptation.

## Implications
For industry practitioners, Stemma offers a practical fingerprinting tool that can be integrated into model governance pipelines without requiring access to model internals. Its robustness across deployment settings supports trustworthy AI workflows and regulatory compliance, fostering confidence in LLM lineage tracking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25880v1)
