---
title: A General Sufficient Condition for Rewriting Horn-ALCHI Atomic Queries into GQL
url: http://arxiv.org/abs/2608.04945v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_15-12-01Z_AGeneralSufficientConditionforRewritingHorn_ALCHIA.md
generated_at: 2026-08-05 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a method for converting atomic queries expressed in Horn‑ALCHI ontologies into the GQL query language, which is built on controlled recursion. By modeling these queries as runs over fact sets using a new formalism called DL automata, the authors show that a large class of such automata can be rewritten as unions of conjunctive two‑way regular path queries (UC2RPQs), a core fragment of GQL.

## Key Takeaways
- The introduction of DL automata provides a precise representation of Horn‑ALCHI atomic queries, capturing their semantics through deterministic runs over fact sets.
- A key result is that these automata belong to a class that can be expressed as unions of conjunctive two‑way regular path queries, enabling direct translation into GQL.
- The authors rely on a state stratification technique to eliminate cyclic dependencies that would otherwise increase complexity and prevent rewriting.

## Context
GQL extends first‑order logic with controlled recursion, allowing it to handle queries that FO cannot express. Horn‑ALCHI is widely used for representing ontological constraints but lacks FO rewriteability, creating a gap between expressive power and query language support. This work bridges that gap by providing a systematic pathway from ALCHI‑based atomic queries to GQL.

## Implications
Practitioners can now apply GQL to evaluate complex ontology‑driven questions without resorting to costly intermediate representations. The rewriteable class reduces computational overhead, making large‑scale ontological reasoning more feasible and accessible across AI systems that rely on GQL for structured data access.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04945v1)
