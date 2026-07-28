---
title: Maximum Satisfiability of Simple Temporal Problems
published: 2026-07-26T18:00:56Z
authors: Johannes K. Fichte, Johanna Groven, Peter Jonsson, Victor Lagerkvist, Jorke M. de Vlas
url: http://arxiv.org/abs/2607.23785v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Maximum Satisfiability of Simple Temporal Problems

## Abstract
The Simple Temporal Problem (STP) is a core framework for quantitative temporal constraints. As STP data can be inconsistent, we study MAXSTP: compute a maximum-cardinality consistent subset of constraints. This extension is NP-hard, and we analyze its parameterized complexity under measures that capture practically relevant instance features: the number of variables $n$ (instance scale), the maximum coefficient magnitude $k$ (numeric range), and structural parameters of the constraint graph such as treewidth $tw$ (decomposability) and vertex cover size $vc$ (density). We show that MAXSTP is W[1]-hard parameterized by $n$, implying that $n$ and parameters that depend on $n$ (including $tw$ and $vc$) are insufficient for fixed-parameter tractability. For combined parameters, we give an $O^*(k^n)$-time algorithm, yielding single-exponential solvability for fixed $k$. While $k+tw$ remains W[1]-hard, MAXSTP is in XP via an $O^*((n\cdot k)^{tw})$ algorithm. Our results suggest that MAXSTP is often computationally harder than optimizing qualitative CSPs. We verify that many such problems (including RCC-8 and Allen's algebra) are FPT when parameterized by $n$ or $tw$. However, we also demonstrate that FPT algorithms for MAXSTP are indeed possible but with other parameters such as $k + vc$.

## Metadata
- **Published**: 2026-07-26T18:00:56Z
- **Authors**: Johannes K. Fichte, Johanna Groven, Peter Jonsson, Victor Lagerkvist, Jorke M. de Vlas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23785v1)