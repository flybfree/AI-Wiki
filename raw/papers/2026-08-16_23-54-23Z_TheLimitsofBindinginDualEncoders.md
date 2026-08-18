---
title: The Limits of Binding in Dual Encoders
published: 2026-08-16T23:54:23Z
authors: Kin Ian Lo
url: http://arxiv.org/abs/2608.15971v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Limits of Binding in Dual Encoders

## Abstract
Dual-encoder models such as CLIP score an image-caption pair by a single inner product of two independently computed unit vectors, and fail at binding, often scoring near chance when asked to distinguish "a red car and a blue dog" from "a blue car and a red dog". We give a mathematical account of when this failure is necessary and when it is contingent. Working within the ideal-encoder framework proposed by Kang et al., we first show the relevant axioms are satisfiable, so every impossibility must enter through an added, checkable hypothesis. We then prove three such obstructions. Depth: for recursive role-binding codes the swap margin obeys an exact law $m(D) = 2b^{-D}$ in the nesting depth D, with a finite-dimension version holding up to one explicitly flagged concentration estimate; the resolvable depth grows only logarithmically in the dimension and is single-digit at CLIP scale, the nesting depth of ordinary language. Objective: architecture-free throttle theorems showing that the contrastive objective's entire reward for binding is bounded by the rate at which training contrasts a caption against its own swap, a rate that vanishes at web scale, and that exactly reversed binding costs only that rate times the mean binding margin; both are verified in simulation. Geometry: a tight smoothness-binding frontier: the closer the two swap-related captions must embed to a shared paraphrase anchor, the smaller the binding margin can be, with an exact constant. Measuring its text-only diagnostic across 18 deployed text encoders, every model sits at roughly 25-35% of its ceiling, and the induced per-item ceiling tracks SugarCrepe's subset difficulty at r = 0.99. Binding failure in deployed dual encoders is thus not a dimension or smoothness limit today, but an incentive and code-structure limit, with a proved depth ceiling that remains once those are fixed.

## Metadata
- **Published**: 2026-08-16T23:54:23Z
- **Authors**: Kin Ian Lo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15971v1)