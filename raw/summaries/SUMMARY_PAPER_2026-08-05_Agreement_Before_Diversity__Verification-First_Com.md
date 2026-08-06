---
title: Agreement Before Diversity: Verification-First Complementarity for Heterogeneous Language-Model Coordination
url: http://arxiv.org/abs/2608.04618v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_09-24-39Z_AgreementBeforeDiversity_Verification_FirstComplem.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Agreement‑Before‑Diversity (ABD), a rule that decides whether an existing model answer should be kept or replaced by a new heterogeneous synthesis. It proves two exact identities linking accuracy gaps to coverage and authority, and shows ABD outperforms single‑model baselines on LiveCodeBench‑v6 and GPQA‑Diamond.

## Key Takeaways
- The method treats replacement authority as an auditable object that is granted only when two trusted samples agree under a fixed equivalence relation.  
- Accuracy improvement depends jointly on how much the anchor answer is agreed upon and its advantage on the protected subset, as shown by the first exact identity.  
- The second identity links gaps to authorized recovery versus authorized destruction, revealing that diversity alone does not guarantee better performance.

## Context
Heterogeneous language‑model ensembles are common in AI but lack systematic criteria for answer replacement, leading to suboptimal or inconsistent outputs. This work addresses the need for a principled gating mechanism that balances candidate diversity with verification reliability.

## Implications
ABD provides a clear, label‑free decision process that can be integrated into existing ensemble pipelines without retraining models. Practitioners can use it to improve factual consistency in large language systems while preserving response variety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04618v1)
