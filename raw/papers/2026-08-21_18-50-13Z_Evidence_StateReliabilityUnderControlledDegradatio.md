---
title: Evidence-State Reliability Under Controlled Degradation: Parser-Validity Divergence in a Multi-Stage LLM Pipeline
published: 2026-08-21T18:50:13Z
authors: Naimur Rahman
url: http://arxiv.org/abs/2608.21559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-State Reliability Under Controlled Degradation: Parser-Validity Divergence in a Multi-Stage LLM Pipeline

## Abstract
Multi-stage LLM pipelines can remain structurally valid even when evidence available to downstream stages becomes incomplete, compressed, or conflicting. This paper introduces and operationalizes Evidence-State Reliability (ESR), an evaluation layer concerned with whether intermediate evidence remains sufficiently complete, grounded, internally consistent, and usable for a stage's assigned function. ESR is evaluated separately from parser validity, which measures structural conformance.   We evaluate the framework using GLM-5.2 on 60 sanitized base cases under four evidence conditions: clean, compressed-lossy, partial-dropout, and noisy-conflicting. Each condition was processed through decision, audit, and escalation stages. The design comprised 720 planned and ledgered calls, with 713 retained, sanitized execution rows.   Across nine matched degraded-minus-clean condition-stage comparisons, all operational stage-success estimates were negative, and all 95% bootstrap intervals remained below zero. All nine parser-validity point estimates were positive, although the three partial-dropout intervals included zero. Among parser-valid degraded audit outputs, degradation detection was 1.0 in each degraded condition, while false-assurance rates remained non-zero; among parser-valid degraded escalation outputs, recovery was 0.0 in every degraded condition.   The results show a bounded reliability-layer divergence in the evaluated pipeline: structural conformance can improve directionally while evidence-sensitive stage success deteriorates under the same controlled intervention. They also separate detection of degraded evidence from recovery. The conclusions are limited to the evaluated model configuration, pipeline design, selected sanitized cases, scoring procedure, and single scaled run.

## Metadata
- **Published**: 2026-08-21T18:50:13Z
- **Authors**: Naimur Rahman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21559v1)