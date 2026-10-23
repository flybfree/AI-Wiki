---
title: Where Do Legal Factors Live in LLMs?
url: http://arxiv.org/abs/2610.28799v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-20_18-24-37Z_WhereDoLegalFactorsLiveinLLMs.md
generated_at: 2026-10-22 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models form internal representations that correspond to the 26 CATO factors, which are symbolic legal concepts used in case-based legal reasoning systems like HYPO and CATO. Using linear decodability probes and sparse autoencoders across three open models (Qwen3-1.7B, Qwen3-8B, and Gemma-2 2B), the authors demonstrate that all 26 expert-defined legal factors are linearly decodable from LLM internal activations, with single-feature sparse readouts achieving test AUCs between 0.86 and 1.00. The study produces 78 model-specific layer-feature coordinates, effectively mapping where legal knowledge resides within each model's architecture.

## Key Takeaways
- All 26 CATO factors are linearly decodable in every tested model, meaning that information corresponding to expert-defined legal concepts such as legally significant fact patterns can be extracted from LLM internal activations when processing legal narratives. This confirms that LLMs do encode structured legal knowledge, not merely surface-level text patterns.
- Single-feature sparse readouts from sparse autoencoders can cover the complete factor catalog, with best-layer test AUCs ranging from 0.86 to 1.00, and five selected features approach full-vector readout performance. This suggests that legal factor representations are not diffusely spread but can be localized to specific, sparse features within particular layers.
- The authors report 78 model-specific layer-feature coordinates (one per factor per model), providing a concrete map of where each legal factor's representation lives in each architecture. Cross-model comparison and human audit of controlled natural-language passages validate these findings, connecting symbolic legal abstractions from HYPO and CATO to learned internal representations.

## Context
This work sits at the intersection of AI & Law interpretability research and mechanistic interpretability of neural networks. Prior AI & Law systems like HYPO and CATO encode legal reasoning through explicit, auditable symbolic structures, but the rise of LLMs for legal tasks has created a gap: practitioners cannot trace how these models internally organize legal knowledge. By applying sparse autoencoders and linear probing techniques typically used in mechanistic interpretability to legal-specific factor taxonomies, this paper bridges symbolic legal AI and modern LLM interpretability, offering a method to audit whether LLMs genuinely encode structured legal reasoning or merely approximate it statistically.

## Implications
For legal AI practitioners and developers, these findings suggest that LLMs can be audited for specific legal reasoning capabilities by probing known layer-feature coordinates, enabling more transparent and accountable deployment of AI in case-based legal reasoning workflows. For the broader AI field, the demonstration that expert-defined symbolic concepts map to sparse, localizable internal features validates mechanistic interpretability tools as applicable to domain-specific knowledge structures, potentially guiding the design of more interpretable and legally grounded language models. For legal professionals, this research offers a pathway toward verifying whether AI-assisted legal tools truly perform precedent-based reasoning aligned with established legal factor frameworks rather than producing superficially plausible outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28799v1)
