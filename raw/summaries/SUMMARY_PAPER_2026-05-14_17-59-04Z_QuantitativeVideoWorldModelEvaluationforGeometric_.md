---
title: Quantitative Video World Model Evaluation for Geometric-Consistency
url: http://arxiv.org/abs/2605.15185v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_17-59-04Z_QuantitativeVideoWorldModelEvaluationforGeometric_.md
generated_at: 2026-06-11 10:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PDI‑Bench, a quantitative framework that evaluates the geometric coherence of generated videos by measuring projective‑geometry residuals across scale‑depth alignment, 3D motion consistency, and structural rigidity. The study demonstrates that state‑of‑the‑art video generators consistently exhibit geometry‑specific failures that are invisible to conventional perceptual metrics.

## Key Takeaways
- PDI quantifies three failure dimensions—scale‑depth alignment, 3D motion consistency, and 3D structural rigidity—using object‑centric observations lifted to world space.  
- The framework uncovers consistent geometric flaws in current video generators that are not captured by human judgments or learned graders.  
- PDI provides a diagnostic signal for progress toward physically grounded video generation.

## Context
Generative video models are treated as implicit world models, yet their physical plausibility is rarely verified objectively. Existing evaluation methods depend on subjective human feedback or weak‑diagnostic learned graders, limiting the ability to detect subtle geometric errors that affect downstream applications.

## Implications
PDI‑Bench offers an objective benchmark for researchers and industry practitioners aiming at robust, physically consistent video generation. By exposing hidden failure modes, it guides model improvement and informs deployment decisions where visual fidelity is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.15185v1)
