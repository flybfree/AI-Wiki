---
title: ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation
published: 2026-08-23T19:11:59Z
authors: Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein
url: http://arxiv.org/abs/2608.22559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation

## Abstract
Rubrics aim to make language-model evaluation transparent by decomposing response quality into interpretable criteria. However, natural-language rubrics are often ambiguous, require black-box LLM judges, and typically assume criteria aggregate independently through linear weighted sums, limiting their ability to capture dependencies, alternatives, penalties, and override conditions. We propose ExecRubrics, a framework for representing rubrics as compact executable programs. ExecRubrics encodes evaluation logic as verifiable Python scoring functions, giving natural-language rubric intent an operational semantics: a fixed decision procedure that can be inspected, executed, and edited. On three long-form response benchmarks-HealthBench, HelpSteer, and ArgQuality-we show that ExecRubrics can substitute for expensive black-box judges in ranking preferred over dispreferred responses, matching or improving NL rubric baselines with best preference accuracies of 53%, 78%, and 92%, respectively, while reducing evaluation latency by up to 320 times. We show that incorporating external logic and resources from text processing libraries such as NLTK and spaCy further improves preference accuracy. Our results suggest a novel way of looking at evaluation, by offering a faster, more explainable, and less ambiguous alternative to black-box rubric evaluation, particularly in high-stakes domains such as healthcare and banking where precision and auditability are critical.

## Metadata
- **Published**: 2026-08-23T19:11:59Z
- **Authors**: Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22559v1)