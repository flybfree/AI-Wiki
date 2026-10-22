---
title: Where Do Legal Factors Live in LLMs?
url: http://arxiv.org/abs/2610.28799v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_18-24-37Z_WhereDoLegalFactorsLiveinLLMs.md
generated_at: 2026-10-21 21:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models internally encode the 26 CATO legal factors used in case-based legal reasoning systems like HYPO and CATO. Using linear decodability analysis and sparse autoencoders across three open models (Qwen3-1.7B, Qwen3-8B, and Gemma-2 2B), the authors demonstrate that all 26 expert-defined legal factors are linearly decodable from LLM internal activations, with test AUCs ranging from 0.86 to 1.00. The study identifies 78 specific layer-feature coordinates mapping each factor to a precise location within each model's architecture.

## Key Takeaways
- All 26 CATO factors are linearly decodable across all three tested models, meaning that information corresponding to expert-defined legal concepts such as legally significant fact patterns can be extracted from internal activations when LLMs process legal narratives. Single-feature sparse readouts cover the complete factor catalog, with best-layer test AUCs ranging from 0.86 to 1.00, indicating near-perfect or perfect linear separability of these legal concepts within model representations.
- The authors report 78 model-specific layer-feature coordinates, one for each factor in each model, enabling sparse localization of legal knowledge. Five selected features approach full-vector readout performance, suggesting that a small number of interpretable features can capture the majority of legal factor information, which has implications for model interpretability and auditing.
- The study bridges symbolic AI & Law frameworks (HYPO dimensions and CATO factors) with the learned internal representations of LLMs, connecting legal language processing to structured, auditable legal concepts. Cross-model comparison and human audit of controlled natural-language passages provide validation that these decodable representations correspond to genuine legal reasoning patterns rather than superficial statistical correlations.

## Context
This work sits at the intersection of AI & Law, interpretability research, and legal informatics. The CATO factor framework, developed by Kevin Ashley and colleagues, has long served as a symbolic representation of legally significant fact patterns for case-based reasoning. As LLMs increasingly handle legal tasks, understanding whether their internal organization aligns with or diverges from established legal knowledge structures becomes critical for trust, accountability, and regulatory compliance in legal AI applications.

## Implications
For legal AI practitioners and researchers, this study provides a concrete methodology for auditing whether LLMs encode legally meaningful concepts, enabling verification that model outputs are grounded in recognized legal reasoning patterns rather than mere pattern matching. For the broader AI safety and interpretability community, the sparse localization results demonstrate that domain-specific expert knowledge can be traced to specific model components, offering a template for auditing other specialized knowledge domains. For legal professionals and regulators, the findings suggest that LLM-based legal tools could potentially be made more transparent and auditable by mapping their internal representations back to established legal frameworks like CATO and HYPO.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28799v1)
