---
title: AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents
url: http://arxiv.org/abs/2608.05891v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_11-15-41Z_AppDeltaWorld_Transition_GroundedDeltaCodeWorldMod.md
generated_at: 2026-08-06 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AppDeltaWorld, a transition‑grounded delta code world model that predicts the next GUI as a reachable code update rather than an unconstrained image or text description. The model retrieves app‑specific HTML references under action‑transition constraints and generates executable HTML conditioned on current screen, action, predicted next‑screen text, and retrieved structure. AppDeltaWorld achieves state‑of‑the‑art performance on CMGUIBench‑500 and enables strong results for mobile GUI agents.

## Key Takeaways
- The model predicts the next GUI by generating a code update that respects transition constraints rather than producing raw visual data.
- It combines Level‑1 HTML references with conditional executable HTML to insert visual assets before browser rendering, improving fidelity.
- AppDeltaWorld’s world‑model training supports filtered closed‑loop SFT and yields state‑of‑the‑art results on AndroidLens and MobileGym.

## Context
Mobile GUI agents face challenges in obtaining real trajectories due to privacy concerns and the high cost of simulation. Existing simulators lack stable generation, limited modality coverage, and inconsistent action‑transition logic. This work addresses these gaps by providing a scalable, constraint‑aware world model for mobile interaction research.

## Implications
AppDeltaWorld demonstrates that transition‑grounded code updates can significantly boost performance in real‑world mobile GUI tasks. Practitioners can leverage this framework to build more reliable simulation environments and improve privacy‑preserving training pipelines without extensive app access.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05891v1)
