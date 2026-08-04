---
title: Neuro-Evolved Heuristics for Variable Gapped Common Subsequence Identification
published: 2026-08-01T22:36:35Z
authors: Marko Djukanović, Christian Blum, Aleksandar Kartelj, Saso Dzeroski, Ziga Zebec
url: http://arxiv.org/abs/2608.00888v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neuro-Evolved Heuristics for Variable Gapped Common Subsequence Identification

## Abstract
This study addresses the Variable Gapped Longest Common Subsequence Problem (VGLCSP), a variant of the classical longest common subsequence problem with additional gap constraints and applications in sequence alignment and time-series analysis. While the two-sequence version has been widely studied using dynamic programming, the generalized multi-sequence form is usually solved with beam search-based heuristics, whose hand-crafted designs often lack robustness.   To overcome this limitation, we propose a learning-based approach for automatically designing more effective data-driven heuristics. The heuristics are represented by a neural network with predefined architecture, whose weights are optimized by a genetic algorithm within a neuro-evolutionary framework. The learning process alternates between weight optimization and evaluation within an iterative multi-source beam search procedure, a state-of-the-art method for the problem. Rather than constructing solutions directly, the neural network learns to guide the search process, producing a neuro-evolved heuristic. We further introduce an ensemble heuristic that combines the scores of learned and the best-performing hand-crafted heuristic. Integrated into the iterative multi-source beam search framework, the resulting hybrid approach outperforms existing methods on both synthetic benchmark instances and newly introduced real-world instances with data-driven gap constraints.

## Metadata
- **Published**: 2026-08-01T22:36:35Z
- **Authors**: Marko Djukanović, Christian Blum, Aleksandar Kartelj, Saso Dzeroski, Ziga Zebec
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00888v1)