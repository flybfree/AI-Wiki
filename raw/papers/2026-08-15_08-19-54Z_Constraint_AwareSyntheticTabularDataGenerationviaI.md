---
title: Constraint-Aware Synthetic Tabular Data Generation via Inter-Column Constraint Discovery with LLM Agents
published: 2026-08-15T08:19:54Z
authors: Jianxing Zhao, Mao Guan, Dongyu Liu
url: http://arxiv.org/abs/2608.15109v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constraint-Aware Synthetic Tabular Data Generation via Inter-Column Constraint Discovery with LLM Agents

## Abstract
Generating structurally valid synthetic tabular data remains difficult: outputs with high statistical fidelity and downstream utility can still violate semantically meaningful domain constraints. We study the discovery and enforcement of three complementary inter-column constraint families---equations, linear inequalities, and logical dependencies. Our unified tool-grounded workflow represents all three as machine-executable hypotheses and applies a common interface for full-table validation, deterministic diagnosis, and counterexample-guided revision. A generator-agnostic postprocessor coordinates family-specific repairs on outputs from unchanged tabular generators. Across curated behavioral audits and end-to-end evaluations, the complete workflow improves held-out violation detection over one-shot direct prompting, while postprocessing yields zero measured violations for every retained, applicable constraint, improves downstream utility on most datasets, and largely preserves univariate marginals.

## Metadata
- **Published**: 2026-08-15T08:19:54Z
- **Authors**: Jianxing Zhao, Mao Guan, Dongyu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15109v1)