---
title: Guide, Not Bind: Why Defeasible Priors Fail in Augmented Lagrangian Causal Discovery
published: 2026-09-03T06:53:34Z
authors: Sairam Sundararaman, Sara Girdhar, Manit Narasimha Murthy, Samrudh N, Bhaskarjyoti Das
url: http://arxiv.org/abs/2609.03442v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Guide, Not Bind: Why Defeasible Priors Fail in Augmented Lagrangian Causal Discovery

## Abstract
Differentiable causal discovery methods increasingly encode expert priors as forbidden-edge constraints enforced by an Augmented Lagrangian (ALM) penalty, on the assumption that a data-adaptive relaxation mechanism will discount and eventually override a rule the data consistently contradicts. We show this design, which we call \emph{guide, not bind}, fails for two independent, precisely characterized reasons, and that directly repairing both restores it only partially. First, sequential penalty-ramping ALM suppresses a wrongly-forbidden true edge before any counterfactual check can detect it: we give three necessary conditions any adaptive relaxation must satisfy to avoid this (Proposition~\ref{prop:conditions}), prove that DADU---the natural relaxation rule this paper introduces as the object of study---violates all three (Corollary~\ref{cor:dadu_failure}), and confirm the failure across 3{,}072 training runs spanning graphs from 4 to 32 nodes, where a single wrong prior suppresses a true edge in 87--97\% of trials under DADU. Second, and independent of any fix to the mechanism, we prove in closed form that the standard correlation-matching objective ties a true edge and its reverse to an identical cost of exactly $2r^2$ (Lemma~\ref{lem:tie}), not because the underlying equal-variance model is unidentifiable, but because normalizing to correlation discards exactly the variance information that would make it identifiable; covariance matching instead separates the two directions by a provable margin of at least $w_0^4$ (Lemma~\ref{lem:separation}).

## Metadata
- **Published**: 2026-09-03T06:53:34Z
- **Authors**: Sairam Sundararaman, Sara Girdhar, Manit Narasimha Murthy, Samrudh N, Bhaskarjyoti Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03442v1)