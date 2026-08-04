---
title: Symbolic Attack Chain Generation from Atomic Red Team Techniques: An Empirical Study of Predicate Representation Granularity
published: 2026-07-31T15:35:06Z
authors: Ramya Varunsegar
url: http://arxiv.org/abs/2608.00143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Symbolic Attack Chain Generation from Atomic Red Team Techniques: An Empirical Study of Predicate Representation Granularity

## Abstract
Automated attack chain generation is critical for modern cybersecurity, yet manual construction fails to scale as adversary behaviors expand. While classical AI planning using PDDL offers a formal method to automate this process, it relies on the accurate translation of techniques into symbolic predicates. Current state-of-the-art systems like AURORA employ a nine-category Attack Action Linking Model (AALM), but the necessity of this specific granularity remains unvalidated. This work investigates the impact of predicate representation granularity on plan validity, cost, and fidelity. Utilizing a pipeline where a Large Language Model (LLM) performs translation and the Fast Downward engine performs deterministic reasoning, the study compares the full nine-category AALM against a reduced five-category scheme derived empirically from Atomic Red Team (ART) execution evidence. Results from a sixteen-technique corpus demonstrate that plan validity and cost are largely insensitive to granularity, with 81.3% identical outcomes across both schemes. The findings suggest that higher granularity primarily enhances the internal structural resolution of a plan's justification rather than the viability of the generated attack chain itself.

## Metadata
- **Published**: 2026-07-31T15:35:06Z
- **Authors**: Ramya Varunsegar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00143v1)