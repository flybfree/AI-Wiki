---
title: High-Order Markov Blanket Discovery via a k-Order Relaxation of the Faithfulness Assumption
published: 2026-07-29T00:12:43Z
authors: Loong Kuan Lee, Ragavi Krishnamoorthy, Nico Piatkowski
url: http://arxiv.org/abs/2607.26357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# High-Order Markov Blanket Discovery via a k-Order Relaxation of the Faithfulness Assumption

## Abstract
The problem of learning the graphical Markov blanket (MB) of a variable from data has applications in many areas such as structure learning for Bayesian networks and Markov random fields, causal discovery, and feature selection. However, a common assumption most methods make is that the conditional independencies in the distribution imply the same separation in the graphical structure -- also known as the faithfulness assumption. Unfortunately, this assumption can be violated by higher-order dependencies such as XOR and parity-type relations, and -- on finite samples -- by empirical violations that, in extreme cases, even induce spurious dependencies absent from the true distribution. Therefore, in this paper we propose a "k-order" relaxation of the faithfulness assumption that captures parity type relationships between k+2 variables. We then propose a proof of concept algorithm called k-order Markov blanket (kOMB) that uses this relaxation for MB discovery. Finally, we empirically show how kOMB can recover the MB of a variable under both true and empirical violations of faithfulness. Code available at: https://github.com/lklee9/k-order-Markov-blanket

## Metadata
- **Published**: 2026-07-29T00:12:43Z
- **Authors**: Loong Kuan Lee, Ragavi Krishnamoorthy, Nico Piatkowski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26357v1)