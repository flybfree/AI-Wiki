---
title: Padārtha: Ontology-Grounded Fine-Grained NER Benchmark for Classical Sanskrit
url: http://arxiv.org/abs/2608.29324v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_15-09-31Z_Padārtha_Ontology_GroundedFine_GrainedNERBenchmark.md
generated_at: 2026-08-31 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Padārtha, an ontology‑grounded fine‑grained Named Entity Recognition benchmark for classical Sanskrit based on the Mahābhārata. The study demonstrates that generative models can achieve performance comparable to task‑specific systems but suffer from a sharp drop in granularity and poor recall of unseen entities.

## Key Takeaways
- The benchmark uses Nyāya‑Vaiśesika ontology to create 18 fine‑grained tags under ten ontological nodes, mapping onto five coarse labels for interoperability.  
- Expert annotation yields fine‑grained data for 108,335 mentions across 73,632 verses with a 5,000‑verse test set stressing rare entities.  
- Fine‑tuned generative models match task‑specific systems on coarse tasks but decline sharply in fine granularity and recall unseen mentions.

## Context
The paper addresses the mismatch between modern NER benchmarks designed for contemporary texts and classical literature, highlighting the need for culturally appropriate annotation schemas. It also contributes to AI research by showing that generative architectures can be viable alternatives while exposing their limitations on rare or unseen entities.

## Implications
For Sanskrit scholars, Padārtha provides a rigorous framework to evaluate fine‑grained NER models with cultural relevance. Practitioners should recognize that fine granularity is fragile and that out‑of‑entity mentions remain challenging for generative systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29324v1)
