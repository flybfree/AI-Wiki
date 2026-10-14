---
title: NepPlural: A Human-Anchored Benchmark for Persona Annotation in Nepali Migration Discourse
url: http://arxiv.org/abs/2610.15732v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_16-12-20Z_NepPlural_AHuman_AnchoredBenchmarkforPersonaAnnota.md
generated_at: 2026-10-13 21:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
NepPlural introduces a human-anchored benchmark designed to evaluate how well language models can represent competing socio-cultural personas in Nepali public discourse surrounding youth migration and brain drain, addressing the Western-centric bias in existing pluralistic-alignment datasets. The paper demonstrates that LLM annotation quality is critically dependent on the annotation protocol rather than model capability alone, and that allowing models to abstain from assigning personas dramatically improves alignment with human judgments.

## Key Takeaways
- The benchmark curates 2,148 code-mixed YouTube comments (Devanagari, Romanized Nepali, English) annotated along a four-axis persona taxonomy covering Intent, Primary Driver, Value Orientation, and Affect, plus an explicit No-Persona class, with a 300-comment gold set independently labelled by three native Nepali speakers achieving a mean Fleiss' kappa of approximately 0.55.
- Annotation protocol fundamentally determines LLM reliability: batched chat-interface annotation yields near-chance inter-model agreement (kappa around 0.17), while annotating one comment at a time raises agreement above the native-speaker level (kappa around 0.72). However, consistency does not equal validity—under a forced-choice schema, models confidently assign personas to 39% of comments that native speakers judge as expressing none, keeping macro-F1 near 0.50.
- Allowing abstention resolves the forced-choice problem: models recover No-Persona comments with F1 scores of 0.79 to 0.87 and match or exceed individual native speakers against leave-one-annotator-out references (macro-F1 0.75 to 0.86 versus 0.75). Encoders fine-tuned on batched labels perform poorly at 0.34, and a steerability probe reveals that frontier models adopt single persona axes with 59 to 77% fidelity but compose full coherent personas only 33% of the time.

## Context
Pluralistic alignment research has largely relied on datasets skewed toward Western respondents, leaving non-Western value systems underrepresented in model evaluation. NepPlural addresses this gap by grounding benchmark construction in authentic Nepali-language discourse and native-speaker annotation, providing a template for how multilingual and culturally specific persona modelling can be rigorously evaluated. The finding that annotation protocol design—batched versus single-item prompting—drastically alters measured agreement has broader implications for how benchmark datasets are constructed and audited across the field.

## Implications
For practitioners building multilingual or culturally grounded AI systems, this work shows that evaluation infrastructure and annotation protocols are as consequential as model architecture, and that forced-choice labelling schemas can silently inflate apparent model performance by masking abstention behavior. Industry teams deploying LLMs for content moderation, policy analysis, or social discourse understanding in non-Western contexts should adopt abstention-capable annotation pipelines and single-item prompting protocols to avoid systematic overconfidence in persona assignment. The steerability findings further suggest that current frontier models struggle to compose coherent multi-axis personas, a limitation that must be addressed before pluralistic alignment claims can be extended beyond single-dimension value representation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15732v1)
