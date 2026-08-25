---
title: Correcting a learned physical invariant improves world-model rollouts
published: 2026-08-24T17:29:40Z
authors: Richard Bao
url: http://arxiv.org/abs/2608.23526v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Correcting a learned physical invariant improves world-model rollouts

## Abstract
World models can predict video without learning dynamics that they reliably preserve. We test whether a frozen DreamerV3 trained only on pendulum video learns a scalar that its own latent transition treats as approximately conserved. A label-free search recovers the same energy-like invariant across independently trained conservative models, while the same procedure finds no comparable invariant in matched damped models. During autonomous rollouts, this quantity drifts. Projecting the latent state back toward its initial level set reduces rollout error in all three conservative models, whereas matched random constraints usually increase it. These results distinguish a dynamically meaningful invariant from a merely decodable correlate and reveal a concrete failure mode: a world model can learn a physical constraint from pixels yet violate that constraint when it imagines forward.

## Metadata
- **Published**: 2026-08-24T17:29:40Z
- **Authors**: Richard Bao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23526v1)