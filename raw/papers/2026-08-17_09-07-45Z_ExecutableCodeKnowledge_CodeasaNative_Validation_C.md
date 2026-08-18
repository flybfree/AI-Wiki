---
title: Executable Code Knowledge: Code as a Native, Validation-Carrying Knowledge Representation for AI Coding Agents
published: 2026-08-17T09:07:45Z
authors: Xueping Gao
url: http://arxiv.org/abs/2608.16295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Executable Code Knowledge: Code as a Native, Validation-Carrying Knowledge Representation for AI Coding Agents

## Abstract
AI coding agents need more than relevant snippets: they need business semantics, validation evidence, relations, and assurance that their context is current. Existing systems usually infer or externalize this knowledge through retrieval, summaries, graphs, rules, or reverse specifications. We investigate a complementary representation in which selected code units directly carry agent-usable knowledge. We introduce Executable Code Knowledge (ECK) and define an Executable Code Knowledge Unit (ECKU) as a source-bound object combining stable identity, semantics, executable behavior, contracts, evidence, relations, provenance, validation state, and a query interface. Our Python prototype supports code-local authoring, manifest export, evidence execution, exact changed-line impact, freshness checking, and agent-facing projections. Across three real Python repositories and 26 controlled patch tasks, direct ECK provides executable test coverage for 11/11 evidence-bearing tasks and exact selectors for 9/11; hiding declared evidence reduces exact recovery to 1/11 (paired exact McNemar p=0.0078). ECK-derived rules recover 11/11 exact selectors, showing that rules are effective delivery artifacts while ECK supplies source binding, validation state, impact, and freshness. Exact changed-line impact matches independently authored labels on all 26 patches (12 unit links; precision, recall, and F1 all 1.000). AST-bounded fingerprints classify 50 positive changes and 17 unrelated same-file controls correctly, whereas static rules snapshots detect none of the 50 stale cases. Model-backed patch-review and cross-layer studies measure projection fidelity rather than independent impact discovery. These results support a hybrid architecture: retrieval for coverage, ECK for source and evidence governance, and projections for delivery.

## Metadata
- **Published**: 2026-08-17T09:07:45Z
- **Authors**: Xueping Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16295v1)