---
title: A Russian, a Brazilian, and a German Walk into a Bar, Ask the Same Question-- And Get Three Different Answers: Profiling LLM Perspective Diversity on Contested Topics
url: http://arxiv.org/abs/2610.34278v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-25_13-14-41Z_ARussian_aBrazilian_andaGermanWalkintoaBar_AsktheS.md
generated_at: 2026-10-27 00:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PerspectivesQA, a manually verified multilingual dataset spanning 18 languages that captures globally contested topics, alongside the ROOTS framework for profiling linguistic, perspective, and framing diversity in large language model outputs. The authors evaluate eight models across open-source and proprietary families at varying scales, finding that LLMs tend to hedge their answers in English while committing to definitive positions in lower-resource languages, and that model size significantly influences cross-lingual consistency.

## Key Takeaways
- LLMs exhibit a striking asymmetry in response behavior across languages: they hedge and qualify their answers in English but commit to firm positions in lower-resource languages, suggesting that training data distribution and language-specific fine-tuning create uneven epistemic confidence across linguistic contexts.
- Model scale plays a critical role in cross-lingual perspective consistency. Larger models maintain a more stable and coherent worldview across languages, while smaller models are more easily swayed by language-specific framing, indicating that capacity and training breadth help stabilize perspective alignment but do not eliminate it.
- All evaluated models, regardless of size, demonstrate high sensitivity to minor surface-level input variations, producing notable stance shifts even in larger models. This fragility highlights that small perturbations in phrasing can meaningfully alter the perspective an LLM adopts on contested topics.

## Context
Most existing benchmarks for subjective or contested questions in NLP are English-centric, which limits understanding of how LLMs represent diverse global viewpoints. As LLMs are deployed worldwide across many languages and cultural contexts, understanding whether they faithfully represent the plurality of human perspectives—or default to Anglophone framings—becomes a critical open question. This paper addresses that gap by building a multilingual evaluation infrastructure and a profiling framework that goes beyond accuracy to assess perspective diversity, linguistic framing, and stance consistency across 18 languages.

## Implications
For practitioners deploying LLMs in multilingual or cross-cultural settings, these findings underscore that model outputs on contested topics are not language-neutral and that lower-resource language users may receive more assertive, less hedged answers that could misrepresent the genuine diversity of opinion. For the broader AI research community, the work signals a need to move beyond English-dominated evaluation and to incorporate perspective-diversity metrics into model development pipelines, ensuring that scaling alone does not inadvertently homogenize worldviews under the guise of consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34278v1)
