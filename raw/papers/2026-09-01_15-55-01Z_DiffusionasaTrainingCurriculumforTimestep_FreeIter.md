---
title: Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning
published: 2026-09-01T15:55:01Z
authors: Mariia Drozdova, Aidan Sirbu, Pietro Miotti, Robert Obryk, Mayalen Etcheverry, Eyvind Niklasson, Blake Richards
url: http://arxiv.org/abs/2609.01449v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning

## Abstract
Diffusion models and recursive reasoners are both iterative, but they carry information across iterations differently. We add a persistent hidden state to a diffusion denoiser and remove its timestep conditioning, leaving a single shared update that can be run to arbitrary depth. The result is an anytime solver: accuracy keeps improving with inference depth far beyond the rollout lengths and backpropagation window used in training, reaching 99.90% exact solve on Sudoku-Extreme. We also obtain 98.93% solve rate on Maze-Unique. Surprisingly, progressive denoising is unnecessary at inference: holding corruption at its maximum by replacing every non-clue variable with fresh Gaussian noise at each step retains near-perfect solving and converges to stable solutions. This simple noise-injection mechanism enables a single trajectory to efficiently explore the solution space and settle on the correct answer without parallel rollouts, candidate selection, or external verifiers required by prior reasoning models. Nonetheless, ordered annealed corruption remains critical during training, which suggests that diffusion's primary contribution to our anytime solver is not a sampling procedure at inference, but a denoising training curriculum.

## Metadata
- **Published**: 2026-09-01T15:55:01Z
- **Authors**: Mariia Drozdova, Aidan Sirbu, Pietro Miotti, Robert Obryk, Mayalen Etcheverry, Eyvind Niklasson, Blake Richards
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01449v1)