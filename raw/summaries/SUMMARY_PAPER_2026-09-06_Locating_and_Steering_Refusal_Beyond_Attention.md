---
title: Locating and Steering Refusal Beyond Attention
url: http://arxiv.org/abs/2609.04721v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_04-45-53Z_LocatingandSteeringRefusalBeyondAttention.md
generated_at: 2026-09-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates where refusal mechanisms reside within different neural architectures and shows that a single geometric direction in the residual stream persists across architectures. It demonstrates that aligning this direction between transformer and state‑space model models enables safety probes to detect harmful inputs consistently. The key insight is that the location of reading, not writing, determines how refusals are interpreted.

## Key Takeaways
- Refusal resides at a fixed output point in each layer’s residual stream where the direction is estimated rather than applied.
- A rigid rotation aligns representation spaces so safety tools calibrated on one architecture work on another without rebuilding defenses.
- The intervention strength is irrelevant; only the direction matters, and it transfers across transformer, SSM, recurrent, and hybrid models.

## Context
Current AI safety research focuses on detecting harmful outputs but often assumes architecture‑specific representations. This work reveals a universal geometric structure that can be read at any write site, simplifying cross‑model tooling. The findings address the challenge of maintaining consistent refusal behavior as model families evolve.

## Implications
Practitioners can port existing refusal detectors to new architectures by re‑estimating the direction locally rather than redesigning defenses, reducing development time and cost. This uniform approach strengthens overall safety ecosystems across diverse model families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04721v1)
