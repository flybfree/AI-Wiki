---
title: Rewrite Once, Validate Anywhere: Producing OWL-Aware SHACL Constraints (Extended Version)
published: 2026-08-14T09:06:10Z
authors: Anouk Oudshoorn, Piotr Gorczyca, Dörthe Arndt
url: http://arxiv.org/abs/2608.14104v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rewrite Once, Validate Anywhere: Producing OWL-Aware SHACL Constraints (Extended Version)

## Abstract
The Shapes Constraint Language (SHACL) is a W3C recommendation to express syntactic constraints, called shapes, on RDF graphs. SHACL validators are used to test whether a given graph adheres to such a shape. However, RDF graphs often come with OWL ontologies, whose implicit knowledge needs to be taken into account. This is classically handled by first applying reasoning and then performing the constraint checking on the results, often using different technologies which makes the process inefficient and vulnerable for mistakes.   To overcome this, we propose to internalise the OWL axioms in the SHACL constraints; we construct a rewriting which takes as input both shapes and an OWL EL$^-$ ontology -- a fragment of OWL EL restricting the usage of existential restrictions -- and produces SHACL constraints. This output can then be evaluated by any validator supporting SHACL core regardless of its reasoning support, while yielding the same results as the traditional approach. The implementation of our translation is evaluated both against applying state-of-the-art reasoners and validators consecutively, as against validators with built-in reasoning support. For our benchmark, we show that our approach is in general more efficient in finding violations compared to the sequential approach, thus providing a powerful tool which simplifies combining reasoning with validation.

## Metadata
- **Published**: 2026-08-14T09:06:10Z
- **Authors**: Anouk Oudshoorn, Piotr Gorczyca, Dörthe Arndt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14104v1)