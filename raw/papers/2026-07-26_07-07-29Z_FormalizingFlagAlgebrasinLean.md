---
title: Formalizing Flag Algebras in Lean
published: 2026-07-26T07:07:29Z
authors: Gyeongwon Jeong, Seonghun Park, Jihoon Hyun, Sang-il Oum, Hongseok Yang
url: http://arxiv.org/abs/2607.23500v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Formalizing Flag Algebras in Lean

## Abstract
Razborov's flag algebra method is a powerful tool for proving asymptotic inequalities in extremal graph theory, often reducing the task to finding a finite certificate by semidefinite programming. We present a machine-checked formalization of the method for finite simple graphs, together with a certificate-to-proof compiler that turns externally generated certificate data into algebraic proofs checked by Lean. The formalization covers the foundations of the method: partially labeled graphs, their densities in large graphs, the quotient algebra of density expressions, graph-limit semantics through positive homomorphisms, and the downward operators used to average out labels. The compiler treats the external semidefinite programming output as candidate data rather than trusted input: Lean independently computes the required density and multiplication facts, verifies positive semidefiniteness exactly over $\mathbb{Q}$, and carries out the algebraic normalization steps of flag-algebra proofs. Our case studies yield formal proofs of seven Turán-type upper bounds, including Mantel's theorem and the Erdős pentagon theorem, a $C_4$-density bound for triangle-free graphs, and edge-density bounds for $K_4$-free, $K_5$-free, and $C_5$-free graphs. Independently of the compiler, we formalize the matching constructions that complete the exact Turán densities of Mantel's theorem and the Erdős pentagon theorem, and prove two inequalities of Goodman. Our constrained semantics also prompted a meta-theoretic comparison of two ways of imposing graph constraints: building a hereditary constraint into the flag algebra from the start, or testing inequalities afterward on constrained graph limits with labels chosen at random. We state the resulting root-plantability criterion characterizing when the two approaches agree; a forthcoming paper will present the complete account.

## Metadata
- **Published**: 2026-07-26T07:07:29Z
- **Authors**: Gyeongwon Jeong, Seonghun Park, Jihoon Hyun, Sang-il Oum, Hongseok Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23500v1)