---
title: Dissecting Neuro-Symbolic Quality Assurance for Synthetic Oncology Data Generation
published: 2026-08-22T19:34:21Z
authors: Laxmigayathri Challa, Yuhan Zhou, Ana Cleveland, Haihua Chen
url: http://arxiv.org/abs/2608.22085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dissecting Neuro-Symbolic Quality Assurance for Synthetic Oncology Data Generation

## Abstract
Synthetic clinical data generation with large language models addresses the scarcity that limits cancer staging research, but oncology hallucinations are categorically harmful: one clinically impossible staging assignment contaminates every downstream model trained on it. Neuro-symbolic pipelines validate during generation, yet the contribution of individual quality-assurance components remains unclear. We report three controlled studies isolating gate necessity, constraint attribution, and retrieval conditionality, holding generation protocol, diversity thresholds, and fine-tuning hyperparameters constant across adapter conditions. The symbolic gate enforces schema completeness, ontology coverage against the Systematized Nomenclature of Medicine, and staging-logic consistency under American Joint Committee on Cancer eighth-edition rules. Ungated, 29.9% of records contain schema failures and 20.1% contain clinically invalid staging. Schema validation is the load-bearing filter: within the fully gated corpus it rejects 148 of 512 records, ontology grounding a further 24, and staging-logic validation none---the only generator producing logic violations is already excluded on schema, making clinical-logic validation a generator-conditional safeguard rather than the dominant filter. Retrieval augmentation is strongly model-dependent: it improves gate compliance for one generator by 12.5 percentage points, has no measurable effect for a second, and collapses output in a third. Across gated configurations ontology density is largely unchanged, indicating that symbolic validation improves clinical validity rather than vocabulary richness. Symbolic gating therefore buys corpus validity but no commensurate gain on real lung-cancer notes in this study; retrieval should be evaluated per model, and ontology density should not be reported as a proxy for corpus quality.

## Metadata
- **Published**: 2026-08-22T19:34:21Z
- **Authors**: Laxmigayathri Challa, Yuhan Zhou, Ana Cleveland, Haihua Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22085v1)