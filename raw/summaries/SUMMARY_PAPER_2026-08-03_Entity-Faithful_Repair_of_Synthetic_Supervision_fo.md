---
title: Entity-Faithful Repair of Synthetic Supervision for Zero-Shot Image Captioning
url: http://arxiv.org/abs/2608.00994v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_04-43-04Z_Entity_FaithfulRepairofSyntheticSupervisionforZero.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReCap, a plug‑and‑play framework that corrects misalignment between synthetic images and captions by aligning entities explicitly rather than relying on global similarity. Experiments demonstrate that ReCap improves image‑text consistency and reaches state‑of‑the‑art results on both in‑domain and cross‑domain zero‑shot captioning benchmarks.

## Key Takeaways
- Synthetic supervision often suffers from entity‑level misalignment where captions omit or misplace entities, degrading training quality.
- ReCap uses detected image‑supported entities to rewrite captions, enforcing explicit correspondence between image features and textual descriptions.
- The adaptive dynamic weighted learning strategy downweights unreliable synthetic pairs, preventing the model from overfitting to flawed supervision.

## Context
Zero‑shot image captioning requires generating natural language without paired data, so reliance on synthetic data is common. However, most synthetic pipelines prioritize overall plausibility over fine‑grained entity fidelity, limiting training effectiveness.

## Implications
For researchers and practitioners, ReCap offers a practical upgrade to existing synthetic‑data workflows, enabling higher quality zero‑shot captioning models. This advancement can be adopted across vision‑language systems where reliable supervision is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00994v1)
