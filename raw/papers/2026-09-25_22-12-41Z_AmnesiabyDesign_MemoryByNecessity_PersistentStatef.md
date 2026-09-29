---
title: Amnesia by Design, Memory By Necessity: Persistent State for Document Intelligence
published: 2026-09-25T22:12:41Z
authors: Souhail Bakkali, Ayoub Merimi
url: http://arxiv.org/abs/2609.32041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Amnesia by Design, Memory By Necessity: Persistent State for Document Intelligence

## Abstract
Modern Document AI reads contracts, extracts fields, reasons over tables, and grounds answers to page regions, then forgets everything. Processing an amendment the next day begins from scratch: no schema retained, no contradiction detected, no experience carried forward. This is a structural choice, not a scale failure: current systems are stateless functions. We call this the statelessness bottleneck. This bottleneck lies beyond parameter scaling, context extension, and retrieval augmentation: storage provides persistence and retrieval provides access, but neither consolidates observations into knowledge that improves future processing. This survey formalizes persistent evidence-grounded document state as a unifying framework, specifying the operations and invariants required to convert multimodal evidence into durable, provenance-linked state. We introduce a statefulness audit showing that ten representative benchmarks, coded against eight statefulness criteria, leave cross-session state evolution untested, and derive a longitudinal benchmark harness with five counterfactual metrics: Experience Gain, Cost Efficiency, Memory Harm, Forgetting Fidelity, Coverage Retention, to characterize the benefit, cost, risk, and governability of persistent document state. Document AI lacks mechanisms coupling persistent state to document-native structure, provenance, and temporal validity. The next era of Document AI will be defined by what systems retain across documents, sessions, and time.

## Metadata
- **Published**: 2026-09-25T22:12:41Z
- **Authors**: Souhail Bakkali, Ayoub Merimi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32041v1)