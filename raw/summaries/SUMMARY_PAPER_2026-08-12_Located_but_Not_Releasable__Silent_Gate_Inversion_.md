---
title: Located but Not Releasable: Silent Gate Inversion and Bounded Linear Release
url: http://arxiv.org/abs/2608.11822v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_09-04-54Z_LocatedbutNotReleasable_SilentGateInversionandBoun.md
generated_at: 2026-08-12 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents a fully preregistered pipeline that detects, localizes, and releases latent causal structure in a 25.7M transformer trained on causal‑evidence discrimination. The study tests the complete process end‑to‑end and finds three distinct failures: successful localization, an out‑of‑distribution inversion of the gating mechanism, and a capped linear release that never reaches the intended threshold.

## Key Takeaways
- Localization succeeds: interventions at observation‑evidence channels restore target behavior with paired release advantages of 0.563 and 0.854 (97.5% CIs excluding zero), achieving an overall best‑site release rate of 0.889.
- Gating fails out of distribution: a detector calibrated to trigger on zero OOD calibration worlds triggers on 6.9–7.3% of held‑out in‑distribution generations and never triggers on the few that actually need it, causing a silent inversion that reduces the pipeline to its base model.
- Linear release is capped: removing the gate and injecting an unconditional linear direction yields a monotone dose‑response with intercepts 0.382 → 0.311 → 0.264 versus threshold ≤ 0.08; per‑instance adaptivity adds less than ±0.03, indicating bounded insufficiency.

## Context
The work addresses the gap between locating task‑relevant latent structure in language models and converting that structure into observable behavior. By rigorously preregistering a stress test, it provides empirical evidence of where current pipelines break down, which is crucial for advancing trustworthy AI systems.

## Implications
For practitioners, the findings warn against assuming that detection alone guarantees behavioral change; gating mechanisms must be validated across both OOD and in‑distribution scenarios. The bounded release limitation highlights the need for adaptive strategies beyond simple linear injection to achieve meaningful improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11822v1)
