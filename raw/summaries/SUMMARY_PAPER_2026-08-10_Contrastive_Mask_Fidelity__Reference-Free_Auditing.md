---
title: Contrastive Mask Fidelity: Reference-Free Auditing of Ground-Truth Masks in Remote Sensing Semantic Segmentation
url: http://arxiv.org/abs/2608.09101v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_04-02-32Z_ContrastiveMaskFidelity_Reference_FreeAuditingofGr.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Contrastive Mask Fidelity (CMF), a reference‑free metric that evaluates class masks against image evidence without relying on human ground truth. It demonstrates that CMF outperforms existing methods in auditing remote‑sensing annotations across ten benchmarks, revealing systematic annotation bias.

## Key Takeaways
- CMF scores competing masks by asking a frozen vision‑language judge whether class evidence is concentrated inside the mask and absent outside, providing an objective fidelity measure.
- The audit shows man‑made classes such as buildings, roads, and cars are favored by candidate masks in 62–85 % of pairs, indicating annotation distortion for these categories.
- On a blinded three‑annotator consensus, CMF matches expert judgment on 81 % of pairs, surpassing keep‑only scoring, model confidence, and a trained label‑quality baseline.

## Context
Remote sensing segmentation often depends on coarse or misaligned masks that are assumed reliable. Existing evaluation methods assume ground truth is perfect, which can mask systematic annotation errors. This work shifts focus to auditing the quality of those masks without human labels, aligning with broader AI goals of self‑supervised and blind verification.

## Implications
Practitioners can use CMF to generate more reliable supervision for transfer learning, reducing reliance on imperfect annotations. The method enables scalable audit pipelines that improve cross‑domain performance, offering a practical tool for remote sensing analysts seeking trustworthy segmentation outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09101v1)
