---
title: Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation
url: http://arxiv.org/abs/2607.22766v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_03-31-44Z_BeyondShapley_AnInfluence_BasedDataAuditingPipelin.md
generated_at: 2026-07-27 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a scalable data auditing pipeline that estimates the predictive influence of individual records in LLM alignment datasets using an approximation of Shapley values without retraining models. By converting semantic k-NN neighborhoods into a directed graph and measuring shifts in probability distributions, the framework identifies problematic records across both training and evaluation splits. Experiments on HelpSteer2 and Anthropic’s HH-RLHF show dramatic reductions in manual audit effort while uncovering hidden label errors.

## Key Takeaways
- The pipeline maps semantic k-NN neighborhoods into a directed graph to compute predictive influence scores via zero‑shot conditional log‑likelihood shifts, providing an inference‑only valuation of each record.  
- Applying the method to HelpSteer2 cut manual audit search space by 99.1% and revealed falsely‑labeled entries across multiple failure modes.  
- Extending the audit to Anthropic’s evaluation split exposed systematic preference inversions that undermine benchmark integrity.

## Context
Current alignment pipelines rely on large, manually curated datasets whose quality is often obscured by subtle contradictions and annotation mistakes. Existing auditing tools either focus on surface similarity or require costly model retraining, limiting scalability. This work introduces a mathematically grounded, zero‑shot approach that can be deployed directly on existing models.

## Implications
Practitioners can now audit large alignment corpora efficiently, ensuring that training data truly reflects intended behavior and that evaluation benchmarks are trustworthy. This reduces the risk of deploying models with hidden safety flaws or misleading performance metrics, fostering more reliable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22766v1)
