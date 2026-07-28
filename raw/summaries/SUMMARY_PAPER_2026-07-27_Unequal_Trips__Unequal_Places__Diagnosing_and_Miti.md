---
title: Unequal Trips, Unequal Places: Diagnosing and Mitigating Delay Inequity in Autonomous Vehicle Fleet Coordination
url: http://arxiv.org/abs/2607.24336v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_12-12-51Z_UnequalTrips_UnequalPlaces_DiagnosingandMitigating.md
generated_at: 2026-07-27 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how delay is distributed across trips and regions in autonomous vehicle fleet coordination, showing that inequities vary by city and coordinator design. It introduces SPARE, a budgeted online framework that reallocates limited replanning capacity to improve both efficiency and fairness.

## Key Takeaways
- The audit reveals pervasive trip-length inequity whose direction depends on the city and coordinator.
- Spatial inequity becomes more pronounced as demand grows and is stronger when trips are grouped by origin rather than destination.
- SPARE provides a per-review decision guarantee, bounds online route updates, and delivers strongest joint efficiency-fairness performance among baselines while maintaining scalability.

## Context
This work addresses a critical gap in AI‑driven transportation systems where aggregate optimization ignores distributional impacts. By treating fairness as an explicit objective alongside efficiency, the study aligns with broader efforts to make autonomous mobility more inclusive and resilient.

## Implications
For industry practitioners, SPARE offers a practical method to balance performance gains with equitable outcomes without costly full‑fleet replanning. Practitioners can adopt similar budgeted, locally aware strategies to enhance both user experience and social responsibility in city‑scale AV deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24336v1)
