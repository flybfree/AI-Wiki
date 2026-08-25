---
title: Where Cognition Lives: Dissecting Emergent from Computed Function in a Minimal Complete Cognitive Architecture
published: 2026-08-23T10:27:13Z
authors: Francisco M. Arrabal-Campos, Francisco G. Montoya, Alfredo Alcayde, Ignacio Fernández
url: http://arxiv.org/abs/2608.22347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Cognition Lives: Dissecting Emergent from Computed Function in a Minimal Complete Cognitive Architecture

## Abstract
A cognitive architecture is more than the module that reasons: it must also decide how long to think and what deserves the effort. We built a minimal but complete system - a recurrent reasoner with adaptive halting, a homeostatic control field, and a value module - and asked of each part: does this function emerge from gradient descent, or must it be computed? Competence emerges. Stopping appears to emerge too, and to be worth more than everything decidable in advance, but that appearance is instrumentation: payoff at matched mean compute climbs from 0.467 (uniform) through 0.546 (difficulty) to 0.698 (ex-ante value), and the further climb to 0.921 (posterior self-observation) does not survive audit. PonderNet-style halting returns a halting-weighted mixture of hidden states while forced-depth baselines return one, and the language head is trained on the mixture alone; equalizing the readout annihilates the apparent advantage of native execution (residual +0.000 [0.000, 0.000]). Value does not emerge: trained couplings capture zero of a payoff an explicit allocator captures completely (+0.151, routing correlation +0.79), so the second-order decisions that pay must be computed, at least where value is orthogonal to content, as here by construction. On a frozen LLM actuator the same instruments show self-consistency voting to be a measured bound (+0.0236 [+0.0150, +0.0326]) and inter-sample agreement nearly worthless as a stopping signal, its mass concentrating on wrong answers. Every null we assert carries a mechanism and a positive control, and the protocol is part of the contribution. Executing our own falsifiable prediction, value under commitment pays +0.1312 [+0.1124, +0.1502] in a cliff-cost family, some seven times the smooth-family estimate - not because the cliff shifts information ex ante, but because it multiplies the attainable range fivefold (5.1x [3.4, 8.2]).

## Metadata
- **Published**: 2026-08-23T10:27:13Z
- **Authors**: Francisco M. Arrabal-Campos, Francisco G. Montoya, Alfredo Alcayde, Ignacio Fernández
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22347v1)