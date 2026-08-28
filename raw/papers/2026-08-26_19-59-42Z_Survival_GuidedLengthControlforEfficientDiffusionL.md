---
title: Survival-Guided Length Control for Efficient Diffusion Language Models
published: 2026-08-26T19:59:42Z
authors: Ivan Kobyzev, Abbas Ghaddar, Yufei Cui
url: http://arxiv.org/abs/2608.26374v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Survival-Guided Length Control for Efficient Diffusion Language Models

## Abstract
Diffusion language models (DLMs) generate text by iteratively denoising masked sequences, but standard decoding either fixes the sequence length or relies on ad hoc stopping rules, often leading to unnecessary denoising steps. We recast length selection as a discrete-time survival problem over the end-of-sequence token and propose a plug-in, training-free length predictor that can be added to any existing DLM. Across reasoning and code-generation benchmarks, survival-guided length decoding speeds up inference by up to 7 times while preserving task accuracy. We further find that predicted lengths vary widely even within the same dataset, making model performance sensitive to the chosen length.

## Metadata
- **Published**: 2026-08-26T19:59:42Z
- **Authors**: Ivan Kobyzev, Abbas Ghaddar, Yufei Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26374v1)