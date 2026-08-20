---
title: Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth
published: 2026-08-18T18:05:53Z
authors: Ivan Viakhirev, Kirill Borodin, Amirah Almutairi, Serguei Barannikov, Maxim Abramov, Grach Mkrtchian
url: http://arxiv.org/abs/2608.18222v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth

## Abstract
Recurrent-depth reasoners aim to solve harder problems by iterating their update longer at test time, but additional iterations can improve, preserve, or degrade an answer. We show that a measurable property of the trained operator, its finite-time dynamical regime (estimated as settling, marginal, or drifting), indicates which of these occurs. We give a sufficient condition for depth-safety: once an operator's per-step displacement is small relative to the decoder margin, the decoded answer cannot change under further iterations. Empirically, on algorithmic tasks trained from $800$ unaugmented examples per difficulty tier, settling operators do not degrade with added depth, and on some tasks convert it into higher accuracy on harder unseen instances (Sudoku, $0.19$ to $0.34$ past the training horizon). A single terminal fixed-point objective moves the regime and the depth behavior together: removing it induces drift and removes the gains, and adding it to a generic recurrence yields depth-safe extrapolation on carry propagation. We give four operational criteria for useful test-time depth, use them to catalogue failure modes, and, as a consistency check, apply the same measurements to Huginn-3.5B, which falls in the non-settling family.

## Metadata
- **Published**: 2026-08-18T18:05:53Z
- **Authors**: Ivan Viakhirev, Kirill Borodin, Amirah Almutairi, Serguei Barannikov, Maxim Abramov, Grach Mkrtchian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18222v1)