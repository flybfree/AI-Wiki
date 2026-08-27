---
title: SkyDrive: Learning to Drive in a New City from Aerial Traffic Monitoring
url: http://arxiv.org/abs/2608.25142v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_20-47-09Z_SkyDrive_LearningtoDriveinaNewCityfromAerialTraffi.md
generated_at: 2026-08-26 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SkyDrive, a framework that uses drone‑based traffic monitoring to generate supervised driving data for autonomous planners in unfamiliar cities. Experiments show that limited aerial supervision can dramatically reduce performance gaps compared with zero‑shot training from scratch. The authors report 650 K trajectory samples derived from 137 hours of aerial footage.

## Key Takeaways
- Aerial traffic monitoring provides a scalable source of supervised driving data, yielding 650 K samples from 137 hours of drone footage.
- Zero‑shot performance on new cities is poor, but adding just 30 minutes of sky supervision can alleviate many domain gaps.
- The framework demonstrates that existing trajectory planners and motion predictors benefit significantly from limited aerial supervision.

## Context
Autonomous driving systems rely heavily on large datasets collected by vehicles, which are costly to gather in new environments. This paper offers an alternative that leverages inexpensive, high‑resolution aerial observations to fill the data gap without requiring a vehicle sensor suite. The approach aligns with broader trends toward multimodal and unsupervised learning for domain adaptation.

## Implications
For city planners and autonomous vehicle developers, SkyDrive reduces the need for expensive on‑road data collection while improving safety through richer supervision. Practitioners can adapt models to new urban layouts quickly, accelerating deployment of self‑driving services in diverse locations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25142v1)
