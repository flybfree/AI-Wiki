---
title: Generating Workflow DAGs from Natural Language with Non-Reasoning LLMs
published: 2026-08-31T05:01:29Z
authors: Anand Iyer, Bhanu Khetharpal, Srinivas Upadhya, Ramkumar Rajagopal
url: http://arxiv.org/abs/2608.30250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generating Workflow DAGs from Natural Language with Non-Reasoning LLMs

## Abstract
This paper addresses the problem of translating natural-language routing rules written by business administrators into executable workflow graphs for enterprise contact centers. Each target is a directed acyclic graph (DAG) of conditional actions with parallel branches, hit-first fallback chains, and per-branch Boolean predicates, encoded in the JSON dialect of a commercial routing platform. We show that neuro-symbolic decomposition enables lower-cost, non-reasoning large language models to generate complex workflow DAGs at production-relevant quality without expensive extended-reasoning models. Our central diagnostic is an emission-density bottleneck: on a 635-rule benchmark of manufactured synthetic data, models select the correct graph nodes with high accuracy but increasingly misconfigure attributes and Boolean grouping as the number of interdependent nodes emitted in one pass grows. We therefore move combinatorial graph construction from the model into a deterministic compiler driven by a compact intermediate representation, with a learned registry-selection front end that focuses generation on relevant vocabulary. Across four models, the full system reaches approximately 89% LLM-judge validity, approximately 90% exact-match condition accuracy, and 99-100% valid JSON while using roughly half the per-rule prompt tokens of a monolithic prompt. On GPT-5.3-chat, the method improves judge validity by 24 percentage points and achieves statistical equivalence to a reasoning model's out-of-the-box quality, although an approximately 8-point frontier gap remains. We also present a deployment path and transferable lessons for structured-generation applications.

## Metadata
- **Published**: 2026-08-31T05:01:29Z
- **Authors**: Anand Iyer, Bhanu Khetharpal, Srinivas Upadhya, Ramkumar Rajagopal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30250v1)