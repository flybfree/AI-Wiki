---

title: Transformer as an Euler Discretization of Score-based Variational Flow
published: "2026-04-26T14:36:31Z"
authors: Huadong Liao
url: http://arxiv.org/abs/2604.23740v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Transformer as an Euler Discretization of Score-based Variational Flow



**Source**: [Original Paper](http://arxiv.org/abs/2604.23740v1)
## Abstract
Despite the Transformer's dominance across machine learning, its architecture remains largely heuristic and lacks a unified theoretical foundation. We introduce Score-based Variational Flow (SVFlow), a continuous-time dynamical system for representation learning in which the state evolves according to a variational posterior-weighted average of conditional log-likelihood scores, and provide a principled basis for regularization through variational consistency. We show that forward Euler discretization of spherical SVFlow exactly recovers the Transformer architecture. Multi-head attention approximates SVFlow vector field via a vMF kernel-smoothed posterior, while MoE/FFN approximates it in a relaxed network-based way, and the residual-normalization block implements a relaxed retraction that maintains spherical geometry. This unification explains why attention trains stably without explicit regularization while MoE requires auxiliary balancing losses. Experiments on pre-trained language models with prefix shuffling show that SVFlow-induced metrics correlate with task performance, reveal depth-dependent sensitivity, and reflect the intrinsic dynamics of attention.

## Metadata
- **Published**: 2026-04-26T14:36:31Z
- **Authors**: Huadong Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2604.23740v1)