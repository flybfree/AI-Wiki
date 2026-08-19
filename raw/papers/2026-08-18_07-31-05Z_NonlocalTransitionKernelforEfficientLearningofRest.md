---
title: Nonlocal Transition Kernel for Efficient Learning of Restricted Boltzmann Machines
published: 2026-08-18T07:31:05Z
authors: Kaiji Sekimoto, Muneki Yasuda
url: http://arxiv.org/abs/2608.17450v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nonlocal Transition Kernel for Efficient Learning of Restricted Boltzmann Machines

## Abstract
Learning restricted Boltzmann machines (RBMs) is computationally challenging because it requires expectations whose exact evaluation is generally intractable. The expectations are typically evaluated using a sampling approximation based on blocked Gibbs sampling (BGS), which is a local Markov chain Monte Carlo transition kernel. However, the locality of BGS can lead to poor sampling quality when the RBM has high energy barriers, thereby degrading learning performance. Deep tempering (DT), which performs parallel tempering over a sequence of learnable RBMs including the training RBM, alleviates this locality issue. However, DT algorithmically requires multiple steps to move through the RBM sequence to achieve a nonlocal transition. In this paper, we propose a transition kernel defined over the RBM sequence used in DT. The proposed kernel has a round-trip structure over the sequence, enabling nonlocal moves within a single transition while leaving the RBM sequence invariant. Numerical experiments show that the proposed kernel performs nonlocal transitions more frequently and achieves higher sampling quality with fewer transitions than BGS and DT. We further verify that learning based on the proposed kernel is more stable and mitigates the training failures observed with BGS- and DT-based learning.

## Metadata
- **Published**: 2026-08-18T07:31:05Z
- **Authors**: Kaiji Sekimoto, Muneki Yasuda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17450v1)