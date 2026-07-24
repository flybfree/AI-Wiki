---
title: Gate-Zero Growth: A Geometric Framework for Function-Preserving Continual Learning
published: 2026-07-16T05:00:49Z
authors: Dante Lok
url: http://arxiv.org/abs/2607.14571v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gate-Zero Growth: A Geometric Framework for Function-Preserving Continual Learning

## Abstract
We introduce \emph{gate-zero growth}, a function-preserving (FP) operator for continual learning that adds new residual blocks through a zero-initialised gate. Under a transversality condition, gate-zero growth induces \emph{rank separation} in the functional Jacobian: old directions are unchanged, new-weight directions are exactly flat at the growth point, and new gate directions are the only first-order source of new functional variation. As gates open during continual learning, function drift is $O(\|\boldsymbolα\|^2)$ and Jacobian leakage $O(\|\boldsymbolα\|_\infty)$, giving a controlled departure from the FP locus. On a $300\mathrm{M}\to857\mathrm{M}$ Transformer adapted from WikiText-103 to BookCorpus, gate-zero growth reaches near-zero old-domain forgetting ($Δ_A < 0.1$) under both exact-preservation (Isolation) and joint-frontier (Freeze-Nothing) operating points, while a non-FP control ($G_{\text{stack}}$) suffers an order-of-magnitude larger forgetting under the same recipe. The same geometric analysis covers LoRA, ReZero, and zero-init adapter constructions, establishing gate-zero growth as the canonical instance of a shared local geometry that governs safe capacity activation in CL.

## Metadata
- **Published**: 2026-07-16T05:00:49Z
- **Authors**: Dante Lok
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14571v1)