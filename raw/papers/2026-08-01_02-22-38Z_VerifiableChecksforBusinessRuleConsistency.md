---
title: Verifiable Checks for Business Rule Consistency
published: 2026-08-01T02:22:38Z
authors: Joseph Tafese, Milad Hooshyar, Sam Bayless, Nick Feng, Arie Gurfinkel
url: http://arxiv.org/abs/2608.00396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verifiable Checks for Business Rule Consistency

## Abstract
Maintaining consistency between natural language documentation of business rules and their evolving internal implementations is a significant challenge in large-scale systems. We present SIRNA, a tool and framework for checking such consistency using SMT solvers. Using the case study of cost calculations in tax domains, we demonstrate a three-part system that combines large language models (LLMs) with formal verification methods. SIRNA translates natural language documentation into candidate SMT formulas using LLMs, followed by checks to validate the translations. Then, corresponding business rules are converted into equivalent SMT representations and validated against the natural language formalizations. Our method is generalizable to domains where business logic exists in both natural language documentation and programmatic implementation. Compared to baseline evaluations, SIRNA significantly reduces the number of false positives and false negatives while offering explainability for its findings.

## Metadata
- **Published**: 2026-08-01T02:22:38Z
- **Authors**: Joseph Tafese, Milad Hooshyar, Sam Bayless, Nick Feng, Arie Gurfinkel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00396v1)