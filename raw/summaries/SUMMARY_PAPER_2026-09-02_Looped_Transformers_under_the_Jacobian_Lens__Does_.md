---
title: Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?
url: http://arxiv.org/abs/2609.01924v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_22-47-16Z_LoopedTransformersundertheJacobianLens_DoestheGlob.md
generated_at: 2026-09-02 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the global workspace that appears in deep feedforward transformers persists when depth is implemented via recurrence rather than stacked layers. By applying a suite of experimental tests to two looped architectures, the authors show that a functional analogue of the workspace emerges but its accessibility is altered by the looping mechanism.

## Key Takeaways
- The iterated part of both Ouro‑2.6B and Huginn‑0125 contains a workspace that can be reconstructed in every loop, yet linear transport cannot carry content across loop boundaries, requiring writes and ablations to span all loops.
- In Huginn‑0125 the workspace content is carried forward across all sixteen recurrences, whereas reads, writes, and ablations operate only within a sliding window of about two recurrences.
- Whether newly injected content can be verbalised depends on explicit per‑iteration supervision, while steering existing content does not.

## Context
Understanding how representational dynamics behave under different depth implementations is crucial for designing scalable models that maintain functional capabilities. This work bridges theoretical insights from the Jacobian lens with practical recurrent architectures, offering a clearer picture of workspace behavior in non‑stacked transformers.

## Implications
For practitioners, the findings suggest that recurrence can preserve workspace functionality but at the cost of limited cross‑loop communication, guiding model architecture choices for tasks requiring long‑range reasoning. Industries may adapt these insights to improve efficiency while maintaining performance in iterative neural models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01924v1)
