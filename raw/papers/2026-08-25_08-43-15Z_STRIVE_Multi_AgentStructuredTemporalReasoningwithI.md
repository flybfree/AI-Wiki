---
title: STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation
published: 2026-08-25T08:43:15Z
authors: Junyeong Maeng, Eunsong Kang, Heung-Il Suk
url: http://arxiv.org/abs/2608.24237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation

## Abstract
Longitudinal radiology report generation (LRRG) requires identifying both current findings and their changes relative to a prior study. Existing methods jointly model diagnosis, attribute estimation, temporal comparison, and language generation within implicit representations, which can cause task interference, obscure the evidence underlying each decision, and limit error traceability. They also model progression states as independent labels, ignoring their ordered structure and thus treating missed changes and direction reversals equally. We present STRIVE, Multi-Agent Structured Temporal Reasoning with Integrated Verification for LRRG, which decomposes clinical reasoning into specialized Diagnosis, Attribute, and Temporal Change Agents that produce explicit intermediate evidence. In particular, the Temporal Change Agent is further post-trained using Progression-Aware GRPO, a verifiable, shaped reward that assigns partial credit to direction-preserving errors while scoring direction reversals lowest. STRIVE performs verification at two stages: a deterministic Consistency Gate reconciles the agent outputs before report generation, and a Validation Agent checks whether the generated report is supported by the aggregated clinical evidence. On Longitudinal-MIMIC, STRIVE attains the best clinical efficacy among recent methods and more than doubles Longitudinal Change Concordance (LCC), a measure of temporal agreement with the reference report, over the strongest baseline.

## Metadata
- **Published**: 2026-08-25T08:43:15Z
- **Authors**: Junyeong Maeng, Eunsong Kang, Heung-Il Suk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24237v1)