---
title: Revealing what benchmark scores hide: Jointly measuring the breadth and reliability of LLM capabilities using accessibility profiles
url: http://arxiv.org/abs/2610.24957v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-18_02-15-55Z_Revealingwhatbenchmarkscoreshide_Jointlymeasuringt.md
generated_at: 2026-10-20 00:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "accessibility profiles" as a framework for evaluating language model capabilities by measuring the probability that a model succeeds across multiple meaning-preserving reformulations of the same inquiry, rather than scoring a single fixed wording. The authors demonstrate that two models with identical average accuracy can differ fundamentally in whether their capabilities are broad but unreliable or narrow but consistent, and they propose two metrics—Access@5 and Reliable@5—to capture this distinction. Across six benchmarks and over twenty models, they show this tradeoff is common and that aggregate scores obscure meaningful differences in how capabilities are distributed across inquiry formulations.

## Key Takeaways
- The paper defines "accessibility" as the probability a model succeeds across meaning-preserving formulations of a query, arguing that single-wording benchmark scores collapse a richer structure: the breadth of inquiries a model can handle versus the reliability with which it handles them. Two models can share the same average performance while one succeeds across more inquiries unreliably and the other across fewer inquiries consistently, leading to opposite user preferences depending on whether a single success suffices or repeated consistent success is required.
- Across six benchmarks and more than twenty models, for approximately half of model pairs with nearly equal mean accessibility, the ranking flips depending on whether the evaluation uses Access@5 (at least one success across five formulations) or Reliable@5 (all five must succeed). For some pairs the two measures diverge by up to 10 points in opposite directions, showing that standard benchmark scores can mislead practitioners about which model is genuinely more capable for their use case.
- The authors show that scaling, reasoning techniques, and prompt optimization can redistribute capability across inquiries in ways aggregate accuracy obscures—sometimes broadening the set of inquiries a model can succeed on while simultaneously making success on those inquiries less repeatable. This means improvements in headline scores may mask regressions in reliability, and accessibility profiles expose these hidden tradeoffs.

## Context
LLM evaluation has long relied on fixed benchmark questions with single-wording prompts, treating formulation sensitivity as noise to be averaged away. This paper reframes formulation sensitivity as a first-class measurable property of model capability, connecting to broader concerns in the field about benchmark saturation, prompt sensitivity, and the gap between reported scores and real-world deployment reliability. It builds on growing awareness that models behave inconsistently under paraphrase and that aggregate accuracy hides distributional structure in capability.

## Implications
For practitioners selecting models for production systems, this work warns that headline benchmark scores can be misleading: a model that looks better under one evaluation protocol may be worse under another, and the choice between Access@5 and Reliable@5 should match the operational requirement—whether retries are acceptable or consistent correctness is mandatory. For the research community, the findings suggest that benchmark design must account for formulation diversity and that future evaluation frameworks should report accessibility distributions rather than single-point scores, enabling more honest comparisons of what models can actually be depended upon versus what they can sometimes achieve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24957v1)
