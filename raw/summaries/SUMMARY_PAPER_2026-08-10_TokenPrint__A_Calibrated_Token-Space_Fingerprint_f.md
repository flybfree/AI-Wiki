---
title: TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance
url: http://arxiv.org/abs/2608.08139v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_13-56-39Z_TokenPrint_ACalibratedToken_SpaceFingerprintforLan.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TokenPrint, a training-free fingerprint that uses top‑k vocabulary projections of late hidden states to compare token strings via Jaccard overlap across 250 probes. It demonstrates high similarity between models sharing identical data and accurately retrieves documented lineage among open‑weight models. The fingerprint remains stable under quantization with minimal loss in similarity.

## Key Takeaways
- Similarity ladder indicates independent identical‑data training yields high raw scores but lower vocabulary‑corrected values, revealing a shared base even before measurable task competence.
- Nearest‑neighbor retrieval ranks the documented base as top candidate for all five R1 distillations with mean rank 1.8 and MRR 0.60, detecting a math‑specialized base not visible in coarse metadata.
- Depth ablation shows lineage discrimination strengthens toward output distribution, AUC rising to 0.90 at full depth while using only the top 5 output tokens retains AUC 0.87.

## Context
This work tackles provenance attribution for language models where metadata alone is insufficient and training data overlaps obscure true origins. By providing a calibration‑based fingerprint, it offers a transparent measure of model lineage independent of fine‑tuning.

## Implications
Practitioners can verify model authenticity without access to training logs, supporting responsible AI deployment. The method’s stability across quantization suggests practical use in resource‑constrained settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08139v1)
