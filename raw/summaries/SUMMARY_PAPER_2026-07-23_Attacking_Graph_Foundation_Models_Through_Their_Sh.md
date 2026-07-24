---
title: Attacking Graph Foundation Models Through Their Shared Representation
url: http://arxiv.org/abs/2607.18567v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_23-03-26Z_AttackingGraphFoundationModelsThroughTheirSharedRe.md
generated_at: 2026-07-23 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new attack surface for graph foundation models that exploits the shared representation learned by an alignment layer. By perturbing this representation at inference time, the authors show that all six tested models are vulnerable to a directed perturbation that collapses predictions. The vulnerability is linked to how directly the decoder reads the representation and not to clean accuracy.

## Key Takeaways
- A directed representation-space perturbation can collapse every model with a budget comparable to the norm needed for a plain graph network, except OpenGraph which collapses at one‑fifth of that cost.
- The attack works on six public models covering different tokenizers and embedding spaces, demonstrating a consistent failure across diverse architectures.
- Realizable input attacks such as edge edits or text modifications can remove at least half the correct predictions on three of the models, showing fragility beyond clean accuracy.

## Context
Graph foundation models aim to generalize across domains by using a shared representation layer that separates tokenization from task decoding. Prior research has focused on training robustness but rarely examined attackability of this alignment component, leaving a gap in understanding model security.

## Implications
If the alignment layer is an unprotected weak point, attackers could degrade performance with minimal resources, undermining trust in these models. Practitioners must treat representation learning as a security target and design defenses that preserve task accuracy while protecting against such attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18567v1)
