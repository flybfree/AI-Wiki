---
title: DynaContext: Self-Improving Dynamic Contextualization of Optimized Prompts for Heterogeneous Parameter Extraction
published: 2026-08-22T15:36:12Z
authors: Joe Yu, Shibin Thomas Stanley Paul, Sven Mayer
url: http://arxiv.org/abs/2608.22014v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynaContext: Self-Improving Dynamic Contextualization of Optimized Prompts for Heterogeneous Parameter Extraction

## Abstract
Automated prompt and skill optimization typically produces a single static instruction that is reused across inference instances until the next optimization cycle. However, this approach cannot adapt when the required context, constraints, and evidence vary from one instance to another. For instance, parameter extraction from electronic component descriptions breaks this assumption: resistors, capacitors, transistors, and connectors require different fields, unit constraints, and demonstrations, and each input provides a different evidence state. We introduce DynaContext, a framework that combines an offline-optimized extraction core, learned with GEPA or SkillOpt, with inference-time contextual adaptation and validation-gated self-improvement. DynaContext routes each item through internal, external, or fallback evidence paths and composes an item-specific prompt from the core, schema, evidence, unresolved fields, and validated demonstrations. Deterministic validation and an LLM judge gate every output, uncertain cases go to human review, and only human-verified corrections enter the demonstration memory. On a single-category benchmark, average accuracy increases from 86.6% for the base prompt to 96.9% for standalone SkillOpt and 98.6% for the best DynaContext configuration. Across 850 heterogeneous gold parameter facts, average field-level F1 increases from 51.8% for an unoptimized, demonstration-free control to 59.2% with dynamic demonstrations alone, 66.9% with the optimized core alone, and 71.0% with both. Holding the model fixed, the full configuration outperforms the deployed static-prompting pipeline by 17.3 F1 points on average.

## Metadata
- **Published**: 2026-08-22T15:36:12Z
- **Authors**: Joe Yu, Shibin Thomas Stanley Paul, Sven Mayer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22014v1)