---
title: TEAMMix: Taxonomy Enrichment Augmentation and Minority-augmented Mixing Strategy for LLM-enhanced Weak-Supervised Hierarchical Text Classification
url: http://arxiv.org/abs/2608.11044v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-16-59Z_TEAMMix_TaxonomyEnrichmentAugmentationandMinority_.md
generated_at: 2026-08-11 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TEAMMix, a weakly supervised hierarchical text classification framework that augments data using LLMs and improves label hierarchy understanding. It enriches labels via keyword generation and corpus mining, then uses LLM-generated pseudo-samples combined with Gaussian mixture resampling to boost performance on imbalanced datasets.

## Key Takeaways
- The semantic enrichment of label hierarchies through keyword generation and corpus mining enhances the model’s ability to interpret fine-grained categories.
- LLM-based pseudo-sample generation mitigates long-tail class imbalance, while Gaussian mixture resampling adds confidence‑based quality control to the augmented data.
- Experimental results show that TEAMMix significantly improves classification accuracy on both fine‑grained and heavily imbalanced datasets compared with baseline methods.

## Context
Hierarchical text classification is essential for many downstream applications such as document summarization and sentiment analysis, yet it suffers from label sparsity and structural complexity. Large language models are powerful but often require long prompts that obscure hierarchical relationships, limiting their practical use in HTC tasks.

## Implications
This work demonstrates a reliable way to leverage LLMs without sacrificing label structure, offering practitioners a scalable solution for real‑world imbalanced classification problems. The approach can be adopted by companies needing precise multi‑level text analysis with limited labeled data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11044v1)
