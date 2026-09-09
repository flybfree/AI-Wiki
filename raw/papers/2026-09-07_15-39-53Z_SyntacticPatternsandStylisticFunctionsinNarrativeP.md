---
title: Syntactic Patterns and Stylistic Functions in Narrative Prose: A Rule-Based and Machine-Learning Approach
published: 2026-09-07T15:39:53Z
authors: Stefana Janicijevic
url: http://arxiv.org/abs/2609.07651v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Syntactic Patterns and Stylistic Functions in Narrative Prose: A Rule-Based and Machine-Learning Approach

## Abstract
This paper presents a small-scale quantitative experiment that links syntactic structure to stylistic functions in narrative prose. Starting from a dependency-parsed corpus of 3,300 sentences, we derive sentence-level stylistic labels across five categories --- descriptive, introspective, causal, ideological, and neutral --- using a transparent rule-based procedure that inspects lemmas, universal part-of-speech tags, and syntactic relations. For each sentence we construct a compact representation of its syntactic profile as a sequence of linearised triples combining lemma, POS tag, and dependency relation. These patterns serve as input to standard machine-learning classifiers trained to predict sentence-level style. The best-performing model achieves a macro-F1 of 0.948 under 10-fold cross-validation. The experiment is implemented entirely in Python using open-source tools. Our goal is not to propose a fully fledged stylistic theory, but to offer a reproducible and extensible workflow for exploring how grammatical structure contributes to narrative interpretation.

## Metadata
- **Published**: 2026-09-07T15:39:53Z
- **Authors**: Stefana Janicijevic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07651v1)