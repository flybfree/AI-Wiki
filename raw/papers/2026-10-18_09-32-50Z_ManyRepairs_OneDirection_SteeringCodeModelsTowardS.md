---
title: Many Repairs, One Direction: Steering Code Models Toward Safer Cryptographic API Use
published: 2026-10-18T09:32:50Z
authors: Tianhe Lu, Sakuna Harinda Jayasundara, Eric Spero, Ewan Tempero, Robert Biddle, Giovanni Russello
url: http://arxiv.org/abs/2610.25133v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Many Repairs, One Direction: Steering Code Models Toward Safer Cryptographic API Use

## Abstract
Cryptographic API misuse in large language model-generated code can compromise software security. While many existing approaches improve code security by modifying model parameters or inputs, how representation changes associated with different cryptographic API repairs can support a shared intervention for safer code generation remains underexplored. To investigate this, we construct 48,000 matched program pairs across four programming languages and ten cryptographic API misuse categories. Each pair changes a specified API decision while preserving the programming task. Subtracting the misuse program's internal representation from its secure counterpart's gives a repair vector. Across five models, comparisons of mean repair vectors reveal stronger organization by misuse category than by language. These category-specific patterns also support a shared intervention. We introduce CrypSteer, which extracts a shared direction by normalizing repair differences and selecting a principal component aligned with repairs across misuse categories. With model weights fixed, adding one shared direction per model to its internal activations during generation improves aggregate target security rates by 5.28--15.00 percentage points over unsteered generation across languages and misuse categories. These findings connect the shared structure of cryptographic repair representations to a reusable intervention for safer code generation.

## Metadata
- **Published**: 2026-10-18T09:32:50Z
- **Authors**: Tianhe Lu, Sakuna Harinda Jayasundara, Eric Spero, Ewan Tempero, Robert Biddle, Giovanni Russello
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25133v1)