---
title: Using Fine-Tuned LLMs to Identify Indicators of Vulnerability in UK Police Incident Logs
published: 2026-07-20T18:58:33Z
authors: Sam Relins, Daniel Birks
url: http://arxiv.org/abs/2607.18446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Using Fine-Tuned LLMs to Identify Indicators of Vulnerability in UK Police Incident Logs

## Abstract
Purpose: Understanding how much of routine policing involves vulnerable people could inform resourcing, training, and multi-agency response, yet administrative data provide limited insight. We explore whether an LLM-based classification pipeline, developed on open-source US police data, can be adapted to estimate the prevalence of four vulnerability indicators - mental ill health, substance misuse, alcohol dependence, and homelessness - in UK police incident narratives, and when outputs can be treated as defensible measurements.   Methods: We analyse nearly 3,000 de-identified incident logs from a UK police force, using a multi-stage pipeline combining repeated model inference, label aggregation, structured human review, and statistical correction. The pipeline runs on a locally hosted open-weight LLM, reflecting the secure environments police must work in.   Results: LLMs can produce meaningful, if imperfect, prevalence estimates at scale. Mental ill health indicators are present in approximately one in five incidents, with lower prevalence for other indicators. However, naive LLM deployment is unreliable: single-pass classifications are unstable, and aggregated outputs systematically over-assign indicators relative to human judgement. Correcting these biases required substantial human input and statistical adjustment, leaving considerable uncertainty.   Conclusions: While LLMs can extract information from unstructured police data, their outputs cannot be treated as valid measurements without careful methodological support. At the population level, defensible estimates are achievable but resource-intensive; at the individual level, errors remain frequent and unpredictable, limiting suitability for operational decisions. This study highlights both the potential and the constraints of LLM-based measurement in applied settings.

## Metadata
- **Published**: 2026-07-20T18:58:33Z
- **Authors**: Sam Relins, Daniel Birks
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18446v1)