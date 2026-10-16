---
title: Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models
published: 2026-10-14T18:12:58Z
authors: Yuxuan Chen, Yang Xiao, Jack Sun, Chak Sun, Brick Li,  Sam
url: http://arxiv.org/abs/2610.20763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models

## Abstract
Full-duplex spoken language models decide at every frame whether to take the floor, defining a conversational personality -- yet each set of weights encodes exactly one, which human speakers bracket rather than share. Existing controls mostly act from outside; none identifies the quantity that sets how much the model speaks. We identify it: a single late-layer residual-stream direction, the initiative vector, extracted from the model's own conversations without training or annotation. The same direction reads the decision, anticipating onsets up to 800 ms ahead, and shifts it: scaled during generation, it moves speech ratio from 6-12% to 42-61% (no steering: 21-30%), consistently across conversations, weights, and corpora. A short reference recording suffices to transfer a speaker's turn-taking style to the model, and the transfer is reference-specific: swapping in another speaker's reference worsens the match in 93-98% of cases, whereas the best uniform dose is indistinguishable from no steering. Turn-taking style is not frozen into the weights but a direction that can be read, shifted, and calibrated per person. Audio examples are available at https://elpsykongloo.github.io/initiative-vector/.

## Metadata
- **Published**: 2026-10-14T18:12:58Z
- **Authors**: Yuxuan Chen, Yang Xiao, Jack Sun, Chak Sun, Brick Li,  Sam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20763v1)