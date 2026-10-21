---
title: Same Judgment, Different Yes: Measuring Multilingual Judgment Profiles in Language Models
url: http://arxiv.org/abs/2610.28066v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_11-50-08Z_SameJudgment_DifferentYes_MeasuringMultilingualJud.md
generated_at: 2026-10-21 00:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether multilingual evaluations that score a language model's opening "yes" or "no" token are measuring genuine moral judgment or merely a language-specific answering habit. By collecting 1.1 million model replies across eight models, six languages, and up to 105 moral vignettes under varying question forms and reading constraints (the FAR-6 battery), the authors demonstrate that story-level judgment profiles largely converge across different elicitation methods, but the initial yes/no token under specific negative-interrogative framings diverges significantly from sentence-level profiles. The core finding is that a model can preserve its underlying judgment while altering the surface token it produces, meaning that scoring that token without establishing which proposition it affirms conflates judgment with convention.

## Key Takeaways
- Story-level judgment profiles converge across tested readouts and question forms, with sentence profiles agreeing with free-sentence profiles at a correlation of 0.94, indicating that the underlying moral reasoning is robust to phrasing changes. However, the yes/no token read under a negative interrogative with a preset mapping breaks this convergence, showing a median correlation of only 0.67 between token and sentence profiles across experimental cells.
- After removing each language's story consensus, a model's judgment profile in one language is nearest to its own profile in another language for 39 out of 48 model-language cells under proposition labels and 15 under free sentences, far exceeding the 5 expected by chance. This suggests genuine cross-lingual judgment consistency exists but is obscured by surface-level token conventions.
- Particle preferences, positional biases, and named-term preferences follow their own distinct patterns independent of the moral judgment itself, confirming that the initial token encodes answering conventions (such as negation handling in different languages) rather than purely the model's evaluative stance.

## Context
Multilingual benchmarking of large language models increasingly relies on simple binary scoring of opening tokens to assess alignment, safety, and moral reasoning across languages. This paper addresses a foundational methodological vulnerability: when evaluation pipelines treat a first-token "yes" or "no" as a direct proxy for judgment, they risk measuring language-specific answering conventions—such as how negation is handled in interrogative prompts—rather than the model's actual reasoning. The FAR-6 battery provides a systematic framework for disentangling these confounds, contributing to the broader effort in NLP evaluation science to separate model capability from measurement artifact.

## Implications
For practitioners building multilingual safety evaluations, alignment audits, or cross-lingual benchmark suites, this work signals that scoring a model's first token without controlling for question polarity, answer constraints, and language-specific negation conventions can produce misleading or incomparable results across languages. Industry teams deploying multilingual content moderation or moral-reasoning benchmarks should adopt proposition-level or sentence-level readouts rather than token-level scoring, and should explicitly define which proposition a "yes" affirms before treating it as evidence of judgment. The findings also caution benchmark developers that cross-lingual consistency metrics can be inflated or deflated depending on whether the evaluation pipeline inadvertently captures answering habits instead of reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28066v1)
