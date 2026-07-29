---
title: dtControl2+$\varepsilon$: Trading Optimality for Explainability in MDPs via Decision Trees
published: 2026-07-28T16:15:11Z
authors: Tereza Kinská, Jan Křetínský, Tobias Meggendorfer, Sabine Rieder, Maximilian Weininger
url: http://arxiv.org/abs/2607.25925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# dtControl2+$\varepsilon$: Trading Optimality for Explainability in MDPs via Decision Trees

## Abstract
Over the past decade, decision trees have been used to represent controllers (a.k.a. policies) in an explainable way, with dtControl2 as a current state-of-the-art tool. However, for systems that are large or have many corner cases, even such representations tend to be too complex and not human-comprehensible. Unfortunately, reducing the size of the decision tree is not straightforward, as missing just a single crucial case might result in an incorrect controller. We tackle this issue in the setting of Markov decision processes, extending dtControl2 by "$\varepsilon$" functionality: Given an allowed imprecision $\varepsilon \geq 0$, we construct a smaller decision tree, distilling the essence of the controller, while still guaranteeing its $\varepsilon$-optimality. This enables us to provide tunably simpler explanations, omitting a controllable amount of detail. Our tool constructs decision trees that are orders of magnitude smaller than the state of the art.

## Metadata
- **Published**: 2026-07-28T16:15:11Z
- **Authors**: Tereza Kinská, Jan Křetínský, Tobias Meggendorfer, Sabine Rieder, Maximilian Weininger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25925v1)