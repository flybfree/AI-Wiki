---
title: A Compositional Theory of Curvature in Probabilistic Circuits
url: http://arxiv.org/abs/2608.12869v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_06-34-01Z_ACompositionalTheoryofCurvatureinProbabilisticCirc.md
generated_at: 2026-08-13 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a compositional theory of curvature for probabilistic circuits, showing that the trace of the Hessian can be decomposed node‑wise and that global sharpness regularization is misaligned with this structure. It proves that each sum node’s contribution to the loss surface factorizes into a flow term measuring usage and a local sharpness term from its output distribution. The authors then propose an adaptive regularizer that respects these factors, preserving closed‑form EM updates.

## Key Takeaways
- Each sum node’s Hessian trace splits exactly into a circuit‑flow component reflecting how heavily the node is used and a local curvature term derived from its output probability distribution.
- Global sharpness regularization biases learning toward flatter optima because it ignores this compositional structure, leading to depth bias and possible underfitting.
- The adaptive sharpness aware regularizer retains closed form EM updates while targeting nodes with high intrinsic curvature, recovering the generalization lost by global approaches.

## Context
Probabilistic circuits are a class of generative models that support exact inference and provide a well‑defined loss surface where curvature is computable. Unlike deep neural networks, their analysis relies on second‑order information that can be exploited for regularization strategies. This compositional view clarifies why standard global penalties may perform poorly in these settings.

## Implications
For practitioners working with probabilistic models, the paper offers a principled way to design regularizers that align with model structure rather than assuming uniform penalty across all components. It could improve training stability and generalization without sacrificing the benefits of sharpness awareness, making it valuable for both research and industry applications in AI inference systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12869v1)
