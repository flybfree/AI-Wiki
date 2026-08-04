---
title: It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling
url: http://arxiv.org/abs/2608.01207v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_12-47-39Z_It_stheDecodingFormat_NotthePerturbation_AuditingC.md
generated_at: 2026-08-03 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why test‑time scaling works for language models but not for vision‑language models, and proposes Perturbation Grounded Selection (Pgs) to select answers that depend on the image. Experiments show Pgs can beat majority voting by up to 31.8 points on TextVQA with Qwen, yet a matched‑budget control often matches or exceeds it. The authors conclude that gains are real but not always significant.

## Key Takeaways
- Simple majority voting and self‑verification methods perform similarly because both rely on the same language prior when an image‑grounded answer looks like a confident guess.
- Pgs scores candidates by checking if they survive label‑preserving perturbations, which recovers majority voting only with no perturbation.
- When decoding format and budget are matched, Pgs does not consistently outperform plain majority voting; the control often tracks or exceeds it.

## Context
Vision‑language models face a similar scaling problem as language models, but their reliance on visual cues makes selection more fragile. This study highlights that label‑free, training‑free rules can be useful yet must be evaluated under realistic constraints.

## Implications
This work suggests that future research should focus on image‑grounded consistency rather than self‑verification alone to improve test‑time performance. Practitioners should also control for decoding format and budget when interpreting gains, avoiding overstated improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01207v1)
