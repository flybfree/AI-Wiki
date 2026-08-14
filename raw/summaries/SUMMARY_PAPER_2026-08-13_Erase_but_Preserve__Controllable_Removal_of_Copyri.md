---
title: Erase but Preserve: Controllable Removal of Copyrighted Animation Characters via Optimized Semantic Anchors
url: http://arxiv.org/abs/2608.12806v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_04-26-47Z_ErasebutPreserve_ControllableRemovalofCopyrightedA.md
generated_at: 2026-08-13 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a controllable erasure technique that removes copyrighted animation characters from generated images by optimizing semantic anchors within the model’s textual representation. The method replaces character‑specific embeddings with an optimized anchor, achieving high erasure effectiveness and preserving image fidelity while enabling fine‑grained control over removal intensity.

## Key Takeaways
- The proposed approach optimizes an anchor embedding using structural and detailed constraints to serve as a reliable surrogate for diverse characters, allowing precise replacement of target‑related embeddings.  
- Experiments demonstrate state‑of‑the‑art erasure effectiveness and minimal degradation in generated image quality, supporting both single‑target and multi‑target removal with adjustable degrees of control.  
- The optimized anchors are designed to be plug‑and‑play with existing model modification baselines, enhancing their erasure performance without requiring extensive retraining.

## Context
Current text‑to‑image diffusion models excel at generating realistic images but pose copyright challenges when reproducing distinctive animation characters. Existing erasure methods either rely on manual prompt adjustments or involve costly model modifications that cannot guarantee consistent results across varied characters.

## Implications
This work provides a scalable solution for creators and platforms to protect intellectual property while still utilizing generative AI, reducing legal risk and improving user trust in automated content creation. Practitioners can integrate the optimized anchors into their pipelines with minimal effort, fostering responsible innovation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12806v1)
