---
title: Noise Your Prompt: Noising Conditioning Tokens in Continuous Diffusion Language Models
published: 2026-10-06T21:38:52Z
authors: Justin Jung
url: http://arxiv.org/abs/2610.09145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Noise Your Prompt: Noising Conditioning Tokens in Continuous Diffusion Language Models

## Abstract
We revisit a standard accepted practice in the continuous diffusion language model   literature of fixing conditioning prompt tokens clean during training.   We make a very simple modification: also noise the conditioning prompt tokens during training.   We demonstrate that under this modified training objective, we achieve better generalization   in combinatorial reasoning tasks such as Sudoku and N-Queens, with the largest gains on harder variants   ($3.73\% \to 24.65\%$ solve rate on Sudoku Hard), and increased diversity of generated solutions ($50.60\% \to 73.79\%$ coverage on   10x10 N-Queens). We also show measurable improvements to natural language generation quality   in modest dataset regimes with Gigaword summarization, but notably demonstrate that gains do not   transfer to all natural language tasks (e.g open ended dialogue generation).   Our method is a single line change to the training objective, requires no additional inference costs by default,   and provides the flexibility of classifier-free guidance inspired guided sampling. Our   \href{https://github.com/LateralIntelligence/noise-your-prompt} {code} is publicly available.

## Metadata
- **Published**: 2026-10-06T21:38:52Z
- **Authors**: Justin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09145v1)