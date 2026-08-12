---
title: Hypothesis Frontier: Verifier Guided LLM and Symbolic Search for First-Order Induction
published: 2026-08-11T12:13:35Z
authors: Serafim Batzoglou
url: http://arxiv.org/abs/2608.10843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hypothesis Frontier: Verifier Guided LLM and Symbolic Search for First-Order Induction

## Abstract
First-order concept synthesis asks a system to infer one formula that classifies labeled objects consistently across several finite relational structures. Every candidate can be evaluated exactly, but quantified first-order formulas form a vast search space, and LLM outputs are often semantically promising without being fully correct. We introduce Hypothesis Frontier, a verifier-guided neurosymbolic framework that evaluates each LLM formula on every training object, retains the strongest verified hypothesis across rounds, and uses its remaining errors to guide subsequent generation. Symbolic processing repairs invalid formulas while remaining anchored to the LLM-generated hypothesis, and simplifies train-valid formulas without changing any training prediction. Under matched models, problem sets, and LLM-round budgets, Hypothesis Frontier solves substantially more problems than repeated original-prompt generation. After the final formulas are selected, exact simplification shortens many train-valid formulas while preserving every training prediction. Exact symbolic reasoning therefore helps both to solve more induction problems and to compress many of the resulting formulas.

## Metadata
- **Published**: 2026-08-11T12:13:35Z
- **Authors**: Serafim Batzoglou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10843v1)