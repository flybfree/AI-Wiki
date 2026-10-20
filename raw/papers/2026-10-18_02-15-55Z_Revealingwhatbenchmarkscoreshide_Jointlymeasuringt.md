---
title: Revealing what benchmark scores hide: Jointly measuring the breadth and reliability of LLM capabilities using accessibility profiles
published: 2026-10-18T02:15:55Z
authors: Kazem Faghih, Yize Cheng, Shoumik Saha, Mobina Pournemat, Armin Gerami, Soheil Feizi
url: http://arxiv.org/abs/2610.24957v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Revealing what benchmark scores hide: Jointly measuring the breadth and reliability of LLM capabilities using accessibility profiles

## Abstract
Language model benchmarks assign each question a single outcome from one fixed wording, even though the same underlying request can be expressed in many equivalent ways. We argue that the quantity of interest should therefore not be correctness on one wording, but the accessibility of an inquiry, which we define as the probability that a model succeeds across meaning-preserving formulations. The distribution of accessibility across inquiries reveals a structure that accuracy and existing best-, worst-, or average-case prompt scores collapse: how broadly a model's capabilities extend across inquiries and how dependably those capabilities can be elicited. Two models can have the same average performance while one succeeds across more inquiries unreliably and the other succeeds across fewer inquiries but more consistently, leading to opposite preferences depending on whether the task allows multiple retries until one success or when repeated consistent success is required. Across six benchmarks and more than twenty models, this tradeoff is common: for about half of the model pairs with nearly equal mean accessibility, which model looks better depends on whether one success across five formulations is enough or all five must succeed, quantities we call Access@5 and Reliable@5, respectively. For some pairs the two measures diverge significantly, by up to 10 points in opposite directions. Accessibility also reveals that scaling, reasoning, and prompt optimization can redistribute capability across inquiries in ways aggregate accuracy obscures, sometimes broadening the set of inquiries a model can succeed on while making success on them less repeatable. Accessibility turns formulation sensitivity from a nuisance into a measurable property of capability, distinguishing what a model can sometimes succeed on from what users can actually depend on.

## Metadata
- **Published**: 2026-10-18T02:15:55Z
- **Authors**: Kazem Faghih, Yize Cheng, Shoumik Saha, Mobina Pournemat, Armin Gerami, Soheil Feizi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24957v1)