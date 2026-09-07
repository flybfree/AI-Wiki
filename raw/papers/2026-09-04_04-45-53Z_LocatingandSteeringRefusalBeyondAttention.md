---
title: Locating and Steering Refusal Beyond Attention
published: 2026-09-04T04:45:53Z
authors: Preethi Carmel Bosco, Gopalakrishnan Srinivasan
url: http://arxiv.org/abs/2609.04721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locating and Steering Refusal Beyond Attention

## Abstract
Where inside a language model does refusal live, and does that place change when the architecture does? In a transformer, refusal is governed by a single direction in the residual stream, a finding that safety and interpretability tooling now depend on. State-space models (SSMs) route information through a recurrent update instead of attention, sharing no token-mixing mechanism with a transformer. Does the same safety representation survive this shift, or must it be rediscovered per architecture? It survives. A single rigid rotation, which can only reorient a space and not reshape it, aligns one model's representation space with another's, so the two genuinely share the representation. A harm probe trained on a transformer then flags an SSM's harmful inputs, and removing the aligned direction makes a model answer attacks it would otherwise refuse, while a random direction of the same size does far less. What is architecture-specific is not where the direction is steered but where it must be read. Each layer computes a fresh output that is then added into the residual stream, and harm is cleanly readable at this output, the write site, before the addition. A control that holds the intervention's strength fixed shows that what matters is where the direction is estimated, not where it is applied. Applied through a detector-triggered gate, this direction lowers jailbreak success in all four architecture families we test (SSM, transformer, recurrent, hybrid), and on the SSM it holds against an attacker that tunes its prompt against the defense. The gate only matches a trivial rule that returns a fixed refusal whenever the same detector fires, so what transfers across architectures is the direction itself, not defense strength. Safety tooling built on refusal therefore ports to a new architecture by re-estimating the direction at that architecture's write site, not by rebuilding it.

## Metadata
- **Published**: 2026-09-04T04:45:53Z
- **Authors**: Preethi Carmel Bosco, Gopalakrishnan Srinivasan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04721v1)