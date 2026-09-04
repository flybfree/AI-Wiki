---
title: Instruction Duplication as an Inference-Time Control Primitive
url: http://arxiv.org/abs/2609.04024v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_16-05-21Z_InstructionDuplicationasanInference_TimeControlPri.md
generated_at: 2026-09-03 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces instruction duplication as a simple inference-time control that repeats only the procedural part of a generated instruction without changing model parameters or decoding. Experiments on medical multiple-choice questions show that adding one duplicate copy improves deterministic All-8 diagnostic responses from 90.22% to 93.17%, reducing failures and increasing TF-IDF recall, while final answer accuracy stays constant.

## Key Takeaways
- Adding a single instruction duplication raises the deterministic All-8 diagnostic response rate by two percentage points, eliminating a significant portion of remaining errors.
- The method improves pre-provisional TF-IDF recall without affecting final‑answer accuracy, indicating that the duplication helps model confidence but not correctness.
- A blinded audit shows directional confirmations and perceptual ties are preserved, though the confirmation criterion is not met, suggesting operational relevance despite statistical limits.

## Context
Instruction duplication operates within a minimal black‑box framework where only the procedural instruction is repeated during generation. This approach aligns with efforts to keep large language models static while enabling downstream systems to shape outputs through simple post‑processing tricks.

## Implications
For industry practitioners, this low‑complexity control can be integrated into answer engineering pipelines to boost diagnostic branch preservation and repair success rates without retraining models. It highlights the importance of considering how generated trajectories are consumed by real‑world applications when selecting inference‑time interventions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04024v1)
