---
title: Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis
url: http://arxiv.org/abs/2609.02473v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_11-44-21Z_LearningtoFuseLLMswithOntologyRankersforRare_Disea.md
generated_at: 2026-09-02 20:25
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes a behavior‑based fusion model that combines large language models with ontology rankers to diagnose rare diseases. Experiments on eight open LLMs show the fusion improves recall by up to 20 points compared with ranker alone, while preserving candidate‑level ontology evidence for most correct diagnoses.

## Key Takeaways  
- The fusion model learns case‑specific reliance on each system, avoiding a fixed weighting scheme that could discard evidence.  
- It achieves a 7.86 point gain in Phenomizer Recall@1 and a 20.18 point gain on RAMEDIS without retraining the ranker.  
- For 90.8% of fused diagnoses, the disease retains its original ontology support, allowing inspection of evidence.

## Context  
Ontology‑based rankers provide interpretable diagnostic pathways for rare diseases, but they often lack the nuanced reasoning that LLMs offer. Integrating these two approaches addresses a gap where human expertise and machine insight could complement each other in clinical decision support systems.

## Implications  
Practitioners can deploy LLMs as augmentations to existing ontology tools without sacrificing interpretability, enhancing diagnostic accuracy for underserved conditions. This approach may lower the barrier to evidence‑driven AI adoption across healthcare settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02473v1)
