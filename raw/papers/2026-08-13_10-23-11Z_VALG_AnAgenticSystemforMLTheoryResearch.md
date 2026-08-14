---
title: VALG: An Agentic System for ML Theory Research
published: 2026-08-13T10:23:11Z
authors: Dechen Zhang, Xuan Tang, Xinxiang Yin, Xingwu Chen, Jian Qian, Difan Zou
url: http://arxiv.org/abs/2608.13060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VALG: An Agentic System for ML Theory Research

## Abstract
Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We investigate whether this process can be organized as an autonomous agentic workflow for ML theory research.   We develop VALG, an agentic system that combines multi-level Verification, Adaptive formulation of Learning-theory problems, and Graph-structured proof development. Within each source-relative theorem branch, VALG maintains a fixed mathematical specification, checks the theorem-level composition of a typed proof-dependency graph, and constructs and reviews local proofs in dependency order. When a proof attempt fails, VALG identifies whether the obstruction lies in a derivation, the proof structure, or the theorem formulation and routes the next attempt accordingly. Formulation-level obstructions initiate an explicitly related variant or relaxation, preserving the mathematical relation between the resulting theorem and the source problem.   We evaluate VALG on nine subproblems from five COLT 2026 open problems. Two runs produce internally finalized theorem candidates that match the scope of their source briefs; the remaining seven yield restricted-method results, special cases, or conditional theorems. These case studies show how VALG keeps source-scope matches, relaxations, conditional results, and blocked attempts mathematically distinct. VALG is open source at https://github.com/DechenZhang/VALG-ML-Theory-Agent.

## Metadata
- **Published**: 2026-08-13T10:23:11Z
- **Authors**: Dechen Zhang, Xuan Tang, Xinxiang Yin, Xingwu Chen, Jian Qian, Difan Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13060v1)