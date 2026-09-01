---
title: Convergence rates for the RMSprop optimizer with full control of the hyperparameters
published: 2026-08-31T07:37:57Z
authors: Steffen Dereich, Arnulf Jentzen
url: http://arxiv.org/abs/2608.30382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Convergence rates for the RMSprop optimizer with full control of the hyperparameters

## Abstract
Popular adaptive stochastic gradient descent (SGD) methods to train artificial intelligence (AI) systems include the RMSprop, the Adam, and the AdamW optimizers, where the adaptivity parts in Adam and AdamW basically just coincide with RMSprop. Such adaptive methods involve several hyperparameters including the regularization parameter $ε$ (which ensures that one does not divide by 0 and is often chosen to be very close to zero such as $10^{-8}$ in PyTorch by default) and the second moment decay parameter $β$ (which is often chosen to be very close to $1$ such as 0.99 (RMSprop) and 0.999 (Adam and AdamW) in PyTorch by default). Despite the high relevance of such methods, it remains an open research problem to provide error estimates for such methods with the error constants being not exploding but uniformly bounded with the respect to the hyperparameters, even in the situation of convex stochastic optimization problems.   It is the key contribution of this work to essentially solve this problem for RMSprop. Specifically, we bound the expectation of the stopped evaluation of the objective function at the RMSprop process from above by the sum of an initialization term that decays exponentially in the training time, a stochastic approximation remainder of order $γ_n$, and a memory error of order $( 1 - β)^2$ with the error constants being uniformly controlled over all admissible choices of the step sizes, the second moment decay parameter $β$ and the regularization parameter $ε\in[0,1]$ (also covering $ε=0$). Our non-asymptotic error estimates hold not just for all sufficiently large n but hold for every gradient step $n=1,2,3,...$ with all error constants being explicitly specified. The key innovative new feature in the proof of our analysis are suitable inverse moment bounds for the second moment process in RMSprop.

## Metadata
- **Published**: 2026-08-31T07:37:57Z
- **Authors**: Steffen Dereich, Arnulf Jentzen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30382v1)