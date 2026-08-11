---
title: PolicyKG: An Agentic LLM Pipeline for Translating Institutional Policies into SHACL Knowledge Graphs
url: http://arxiv.org/abs/2608.09028v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_02-28-57Z_PolicyKG_AnAgenticLLMPipelineforTranslatingInstitu.md
generated_at: 2026-08-11 12:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PolicyKG, an LLM pipeline that converts natural‑language institutional policies into SHACL knowledge‑graph constraints. It achieves high classification accuracy on the Asian Institute of Technology corpus and demonstrates reliable retargeting between vocabularies. The results show strong performance in both automated and human evaluation.

## Key Takeaways
- PolicyKG classifies each sentence as an obligation, permission or prohibition with 86.9% deontic classification accuracy (Cohen's kappa = .709) on a corpus of 1,663 sentences.
- The system uses a YAML‑based Corpus Adapter that allows domain retargeting without model retraining, and the SHACL shape correctness reaches F1 = .866 on a subset of rules.
- Human re‑annotation of a 50‑item sample yields Fleiss' kappa = .844 agreement, confirming reliability across annotators.

## Context
Institutional policies are typically written in natural language but required by compliance systems as machine‑readable SHACL constraints. Current solutions rely on manual conversion, which is error‑prone and slow. This work demonstrates that an LLM can automate the translation while preserving logical structure through first‑order deontic logic.

## Implications
Automating policy translation reduces human workload and minimizes misinterpretation of legal language. The registry‑swap mechanism enables rapid adaptation to new regulations, supporting scalable compliance tooling across industries such as finance, healthcare, and contract law.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09028v1)
