---
title: A Tight Theory of Error Feedback Algorithms in Distributed Optimization
published: 2026-05-29T17:57:03Z
authors: Daniel Berg Thomsen, Adrien Taylor, Aymeric Dieuleveut
url: http://arxiv.org/abs/2605.31594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Tight Theory of Error Feedback Algorithms in Distributed Optimization

## Abstract
Communication costs are a major bottleneck in distributed learning and first-order optimization. A common approach to alleviate this issue is to compress the gradient information exchanged between agents. However, such compression typically degrades the convergence guarantees of gradient-based methods. Error feedback mechanisms provide a simple and computationally cheap remedy for this issue, but numerous variants have been proposed, and their relative performance remains poorly understood. This paper provides tight convergence analyses for two of the main error-feedback algorithms from the literature, the classic Error Feedback method (EF) and Error Feedback 21 (EF21), by identifying optimal step-size choices and constructing optimal Lyapunov functions tailored to each method. The results hold independently of the number of agents and recover the known best guarantees possible in the single-agent regime.

## Metadata
- **Published**: 2026-05-29T17:57:03Z
- **Authors**: Daniel Berg Thomsen, Adrien Taylor, Aymeric Dieuleveut
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.31594v1)