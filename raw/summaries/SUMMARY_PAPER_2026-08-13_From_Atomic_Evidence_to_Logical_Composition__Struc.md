---
title: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning over Compound Answer Options
url: http://arxiv.org/abs/2608.12836v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_05-18-55Z_FromAtomicEvidencetoLogicalComposition_StructuredC.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the difficulty of large language models when answer options involve logical operators such as AND, OR, and NEITHER/NOR, even though individual atomic judgments are correct. It proposes a framework that separates compound options into atomic answers, scores contrastive hypotheses for each atom, and then combines these calibrated scores using an operator‑constrained integer linear program to produce a final prediction. On the LOGICAL-COMMONSENSEQA benchmark the model raises Macro‑F1 from 48.3 to 77.0 and on LOGICAL‑SATA it improves from 47.0 to 75.6, with the biggest gains for NEITHER/NOR.

## Key Takeaways
- The model never sees a compound option; it decomposes each into atomic answers and scores contrastive hypotheses about each one.
- An operator‑constrained integer linear program composes calibrated scores into a single prediction.
- Improvements are most pronounced on the NEITHER/NOR operator, showing larger gains than on AND or OR.

## Context
Large language models often struggle with tasks that require logical composition of atomic judgments because they treat options as independent strings. This limitation hampers applications in reading comprehension and knowledge verification where precise logical reasoning is needed. The paper contributes a method that respects logical structure while leveraging existing model outputs.

## Implications
For industry practitioners, this approach can be integrated into automated question‑answering pipelines to produce more reliable answers on complex multiple‑choice questions. Practitioners may adopt the decomposition‑and‑compose pipeline to improve performance without retraining large models, offering a practical upgrade for low‑resource settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12836v1)
