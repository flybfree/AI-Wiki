---
title: Constructing Executable Analytical Knowledge Representations for Meta-Analysis Synthesis Using an Agentic Harness
published: 2026-08-03T05:19:05Z
authors: Lingbo Li, Anuradha Mathrani, Teo Susnjak
url: http://arxiv.org/abs/2608.01711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constructing Executable Analytical Knowledge Representations for Meta-Analysis Synthesis Using an Agentic Harness

## Abstract
Meta-analysis synthesis highlights a fundamental challenge in knowledge-based scientific analysis: structured evidence does not by itself represent the analytical knowledge required for executable computation. Decisions about evidence assignment, analytical contrasts, outcome and time-point alignment, effect-size formulation, and methodological admissibility must be explicit before statistical execution. Existing automated approaches often embed these decisions in model outputs, generated code, or workflow traces rather than representing them as independently verifiable knowledge. We introduce the Executable Analytical Knowledge Representation (EAKR), a machine-actionable representation of the knowledge required to transform structured evidence into executable meta-analysis. An EAKR represents evidence, relations, numerical inputs, constraints, provenance, and unresolved issues. We operationalise EAKR in MetaSynDec, an agentic harness in which large language models propose structured updates and deterministic services govern schema- and contract-based validation and execution. Across 58 synthesis units, MetaSynDec constructed all EAKRs, with 57 proceeding to statistical execution. Of 56 units with sufficient information to define a reference analysis object, 38 (67.9%) achieved complete object fidelity and 42 (75.0%) exact evidence-set agreement, with a mean Jaccard similarity of 0.909. Generated and published confidence intervals overlapped in 54 of 55 units (98.2%). MetaSynDec outperformed direct LLM generation in reference synthesis-structure agreement (57/58 versus 23/58; p<0.001) and among 23 jointly completed units, exact reference-formulation agreement (23/23 versus 1/23; p<0.001). These findings provide feasibility evidence that EAKR supports formal validation, traceability, statistical execution, and improved methodological agreement relative to direct LLM generation.

## Metadata
- **Published**: 2026-08-03T05:19:05Z
- **Authors**: Lingbo Li, Anuradha Mathrani, Teo Susnjak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01711v1)