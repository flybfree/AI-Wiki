---
title: SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling
published: 2026-08-02T04:41:20Z
authors: Shrenil Shaun Sharma, Avi Sharma
url: http://arxiv.org/abs/2608.00991v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling

## Abstract
This paper introduces SCHEDBench, a natural-language benchmark for evaluating combinatorial scheduling constraint faithfulness under surface-form variation. Grounded in canonical scheduling instances and solver-derived feasibility and optimality, SCHEDBench assesses whether large language models (LLMs) generate schedules with the same constraint-feasible behavior across varied natural-language (NL) surface forms. SCHEDBench spans 1,132 instances across job-shop scheduling problems (JSP), single and multi-mode resource-constrained project scheduling problems (RCPSP), nurse rostering/scheduling, and curriculum timetabling problems of varying difficulty. Instances are templated into natural language problems using domain-specific templates, themed entities, lexical-syntactic template rephrasing, and constraint-level surface-form variation, with reference solutions verified for feasibility and objective optimality. Across thirteen frontier and open-weight LLMs, we find that models are not reliably invariant to semantically equivalent renderings of the same scheduling problem. Surface-form variation reduces feasibility and induces above-noise shifts in per-instance hard-constraint violations on matched instances. Among the tested isolated axes, constraint reordering yields the clearest above-noise sensitivity.

## Metadata
- **Published**: 2026-08-02T04:41:20Z
- **Authors**: Shrenil Shaun Sharma, Avi Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00991v1)