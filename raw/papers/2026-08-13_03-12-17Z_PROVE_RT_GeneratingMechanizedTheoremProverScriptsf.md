---
title: PROVE-RT: Generating Mechanized Theorem Prover Scripts for Real-Time Systems using LLMs
published: 2026-08-13T03:12:17Z
authors: Sadat Shahriyar, Shareef Ahmed, Abdullah Al Arafat
url: http://arxiv.org/abs/2608.12762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PROVE-RT: Generating Mechanized Theorem Prover Scripts for Real-Time Systems using LLMs

## Abstract
Schedulability analysis is essential for certifying real-time systems, but existing tests are often developed through pen-and-paper proofs that are difficult to scale, validate, and maintain. Mechanized verification in PROSA/ROCQ offers a rigorous alternative, yet manually constructing such proofs requires substantial domain expertise and proof-engineering effort. Recent successes of large language models (LLMs) across a wide range of tasks make them promising candidates for generating PROSA/ROCQ scripts for mechanized theorem provers. However, state-of-the-art LLMs often lack the PROSA-specific knowledge required to correctly use its modeling abstractions and proof patterns.   This paper introduces PROVE-RT, an LLM-assisted framework for generating PROSA/ROCQ scripts to mechanize schedulability analyses in real-time systems literature. PROVE-RT guides generation through dependency-aware informal sketches, retrieval from processed PROSA documentation, staged skeleton generation, and proof completion. We construct a mechanization-oriented corpus from 1, 191 real-time systems papers, containing 13, 134 informal sketches with dependency information. On a curated evaluation set, direct prompting of state-of-the-art LLMs fails to reliably generate valid PROSA mechanizations, whereas PROVE-RT achieves a success rate of 44.7%. These results show that retrieval-guided and staged LLM assistance can improve automated mechanization of schedulability analysis in PROSA/ROCQ.

## Metadata
- **Published**: 2026-08-13T03:12:17Z
- **Authors**: Sadat Shahriyar, Shareef Ahmed, Abdullah Al Arafat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12762v1)