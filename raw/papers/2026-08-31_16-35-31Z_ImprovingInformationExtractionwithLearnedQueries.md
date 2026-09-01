---
title: Improving Information Extraction with Learned Queries
published: 2026-08-31T16:35:31Z
authors: Omar Sharif, Soroush Vosoughi, Nikhil Singh
url: http://arxiv.org/abs/2608.31058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Information Extraction with Learned Queries

## Abstract
When information extraction fails, a natural instinct is to improve the model doing it: for example, by scaling it up or refining its reasoning. In this paper, we show that another part of the pipeline matters at least as much: the queries used to elicit this information. Across four clinical benchmarks and five LLMs, improving the question design alone raises performance by 18.6 F1-score points, i.e. more than using larger extraction models. To make such question design learnable, we introduce List of Questions (LoQ), which generates document-specific question sets, and FeedQ, a feedback-driven optimization method that iteratively refines questions against extraction outcomes. The resulting optimized questions can be used to train lightweight generators: with fine-tuning, 4B-parameter models match or outperform expert-derived baselines and substantially exceed the performance of much larger untuned models. We release a dataset of 12,820 optimized questions to support a broader shift in information extraction research toward treating question design as a first-class problem.

## Metadata
- **Published**: 2026-08-31T16:35:31Z
- **Authors**: Omar Sharif, Soroush Vosoughi, Nikhil Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31058v1)