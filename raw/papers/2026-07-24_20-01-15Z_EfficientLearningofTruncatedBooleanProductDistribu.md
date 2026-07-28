---
title: Efficient Learning of Truncated Boolean Product Distributions: Influence to the Rescue
published: 2026-07-24T20:01:15Z
authors: Rohan Chauhan, Ioannis Panageas
url: http://arxiv.org/abs/2607.22889v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Learning of Truncated Boolean Product Distributions: Influence to the Rescue

## Abstract
Learning the natural parameters $z \in \mathbb{R}^n$ of discrete distributions $μ_z$ from independent samples constrained to a subset $S \subseteq \{0,1\}^n$ is a foundational challenge in high-dimensional statistics. Existing methods for efficiently estimating truncated Boolean product distributions, notably the work of [Fotakis et al' COLT'20, Algorithmica '22], require either strong local connectivity assumptions on $S$ -- a property denoted fatness -- or stringent anti-concentration assumptions and necessitate the total mass of the truncation set to be a constant with respect to $n$. Moreover, the results in [Fotakis et al' COLT'20, Algorithmica '22] suffer from sample complexities that scale as $Ω(2^n)$ if the mass of $S$ is exponentially small in $n$.   In this work, we circumvent these limitations by analyzing the geometry of $S$ under the measure $μ_z$. We refine the existing parameter estimation guarantees under the fatness assumption, improving the prior sample complexity to $O( \log n / ε^2)$ for $\ell_\infty$-recovery, matching the untruncated minimax rate. We further generalize fatness using the notion of influence utilized in the analysis of Boolean functions and provide sufficient conditions for efficient inference. Notably, unlike previous work, our method does not require sampling at arbitrary parameterizations of the model. Lastly, we establish a theoretical lower bound demonstrating the sample complexity exhibits an intrinsic exponential dependence on the width of the model and the minimum distance between elements in the set.

## Metadata
- **Published**: 2026-07-24T20:01:15Z
- **Authors**: Rohan Chauhan, Ioannis Panageas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22889v1)