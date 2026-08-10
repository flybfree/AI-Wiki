---
title: From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs
published: 2026-08-07T14:56:11Z
authors: Neal Batra
url: http://arxiv.org/abs/2608.07301v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs

## Abstract
We study what can be recovered about the transition probabilities of a Markov decision process from optimal actions alone. This is closely related to the inverse problem considered by Letcher et al., who ask when the dynamics can be recovered from numerical \(Q\)-values. Here the numerical values themselves are not observed; only the optimal actions are known, for every reward in a given class.   For state-action rewards \(r(s,a)\), knowing the optimal actions for every reward also tells us how much better one action is than another when each is followed by the same fixed policy. This is still not enough to determine the transition probabilities uniquely. We prove that two kernels give the same optimal actions for every reward exactly when \[ Q_{s,a} = \Bigl(P_{s,a}+\tfrac1γe_s^{\mathsf T}(L-I)\Bigr)L^{-1} \] for one invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). Near a kernel with strictly positive entries, there is an \(n(n-1)\)-dimensional family of different kernels with this property. The result is unchanged if we consider only rewards having a unique optimal action at every state.   We then compare this with rewards of the forms \(r(s)\) and \(r(s,a,s')\). Rewards that depend on the next state can usually recover the transition kernel itself: every row at a state with at least two actions is determined, and we describe exactly when a row at a state with one action can remain hidden. State rewards reveal less: two kernels give the same optimal actions exactly when every deterministic policy is optimal for the same set of rewards. The results show how the form of the reward affects what can be learned about the dynamics from optimal actions alone.

## Metadata
- **Published**: 2026-08-07T14:56:11Z
- **Authors**: Neal Batra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07301v1)