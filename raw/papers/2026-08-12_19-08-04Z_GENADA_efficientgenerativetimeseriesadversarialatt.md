---
title: GENADA: efficient generative time series adversarial attack framework
published: 2026-08-12T19:08:04Z
authors: Michael Baronov, Denis Vorobev, Margarita Rusanova, Petr Sokerin, Alexey Zaytsev
url: http://arxiv.org/abs/2608.12535v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GENADA: efficient generative time series adversarial attack framework

## Abstract
Deep learning models are widely used for time series analysis in domains such as healthcare, finance, energy systems, and environmental monitoring. However, these models remain vulnerable to adversarial attacks, where small input perturbations cause severe degradation in predictive performance. Commonly used gradient-based attacks, iterative first-order methods, are computationally burdensome, as they repeatedly backpropagate through the victim model to compute input gradients during a number of iterative refinement steps. We propose a GENerative ADversarial Attack (GENADA) that learns a generative model to produce deceptive perturbations directly in a single forward pass and a procedure to train it. Variants include single-step and iterative generative attack schemes. The validation considers attacks on several neural models and datasets in the time-series domain, a controlled, low-dimensional setting. Empirically, GENADA achieves comparable attack quality to strong baselines while requiring less time to generate perturbations during inference.

## Metadata
- **Published**: 2026-08-12T19:08:04Z
- **Authors**: Michael Baronov, Denis Vorobev, Margarita Rusanova, Petr Sokerin, Alexey Zaytsev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12535v1)