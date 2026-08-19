---
title: FedPref: Federated Preference Learning for Structured Radiology Report Extraction
url: http://arxiv.org/abs/2608.16971v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_12-29-42Z_FedPref_FederatedPreferenceLearningforStructuredRa.md
generated_at: 2026-08-18 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FedPref, a federated preference learning framework that enables structured extraction from radiology reports without pooling data or sharing annotations. It uses frozen public language models to generate JSON extractions locally, ranks them with site-specific labels, and collaboratively trains compact adapters while sharing only model updates. On simulated hospitals with unequal data, FedPref improves client‑mean F1 by 2.49 points and worst‑site F1 by 9.10 points compared with isolated training.

## Key Takeaways
- The framework generates multiple JSON extractions per report using frozen language models, then selects the best one through local ranking based on few annotations.  
- It trains a tiny Qwen3‑8B adapter per site from these preferences while only exchanging model updates, preserving privacy and reducing communication.  
- Central training on the union of all preference pairs yields higher client‑mean F1 (2.66 points) than isolated training.

## Context
Federated learning has become a standard approach for collaborative AI across institutions with heterogeneous data. Radiology report extraction is a prime example where local annotations are scarce and sharing them is infeasible. This work demonstrates how preference modeling can improve extraction quality without centralizing raw reports.

## Implications
Clinics can now benefit from collective intelligence while keeping patient data on‑site, accelerating deployment of structured radiology outputs. The method also offers a template for other domains where fine‑grained labels are limited and privacy constraints exist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16971v1)
