---
title: Measuring Stability and Failure Behavior in Language Models Under Structured Perturbations
published: 2026-08-22T23:46:11Z
authors: Samira Golsefid
url: http://arxiv.org/abs/2608.22138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Stability and Failure Behavior in Language Models Under Structured Perturbations

## Abstract
Language models are usually judged by a single accuracy score, which does not reveal how their performance degrades as inputs are perturbed. We present a graded, multi-family, failure-aware framework for stress-testing reasoning models. It perturbs each problem along a multi-level severity ladder across seven families: six that preserve the answer, paraphrase, input noise, formatting, irrelevant context, context load, and conflicting instructions, and a Knowledge Boundary family that removes answerability so that refusal becomes the correct response. Every test is validity-gated and labeled by its measured severity, and each model is summarized by per-level Accuracy, a magnitude-weighted Stability, and a per-family Collapse Point defined relative to the model's own baseline. Instantiated on the same 100 seed problems used by GSM-Symbolic, expanded into 4,473 gated tests and run on four models spanning capability tiers, the framework exposes structure that an aggregate score hides: the level at which a model fails is family-specific rather than global, and two stressors expose consistent weaknesses across all models: conflicting instructions and questions built on an impossible premise. Recognition of unanswerability is otherwise uneven, reliable on missing information and fabricated evidence but weak on impossible premises. These failure points are invisible to standard accuracy reporting.

## Metadata
- **Published**: 2026-08-22T23:46:11Z
- **Authors**: Samira Golsefid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22138v1)