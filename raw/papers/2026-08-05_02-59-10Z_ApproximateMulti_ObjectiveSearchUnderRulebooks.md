---
title: Approximate Multi-Objective Search Under Rulebooks
published: 2026-08-05T02:59:10Z
authors: Omar Muhammetkulyyev, Oren Salzman, Tichakorn Wongpiromsarn
url: http://arxiv.org/abs/2608.04398v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Approximate Multi-Objective Search Under Rulebooks

## Abstract
Robotic planning often involves multiple objectives with complex priority relationships, such as safety, efficiency, and regulatory compliance. Rulebooks formalize these relationships, allowing partial ordering of objectives that generalizes both Pareto and lexicographic dominance. Computing the full set of rulebook-optimal solutions, however, is computationally expensive. To address this challenge, we introduce the concept of epsilon-rule-dominance, a principled notion of approximate dominance under rulebooks, and propose RA*pex, a best-first search algorithm that efficiently computes a compact set of epsilon-approximate rulebook-optimal solutions. RA*pex leverages dimensionality reduction, a technique used to speed up existing multi-objective search algorithms, while respecting rule hierarchies by maintaining separate closed sets and performing dominance checks over truncated and residual rule sets. We provide a formal analysis of RA*pex, proving that every rulebook-optimal solution is epsilon-rule-dominated (a generalization of approximate dominance we introduce) by at least one solution in the returned set. Empirical results demonstrate that our approach achieves computation times over two orders of magnitude faster than existing methods.

## Metadata
- **Published**: 2026-08-05T02:59:10Z
- **Authors**: Omar Muhammetkulyyev, Oren Salzman, Tichakorn Wongpiromsarn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04398v1)