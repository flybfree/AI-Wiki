---
title: Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors
url: http://arxiv.org/abs/2608.22872v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_06-59-34Z_BetterRetrieval_WorseRobustness_HowMulti_hopRAGAmp.md
generated_at: 2026-08-24 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how two RAG extensions — entity‑graph linking and iterative reformulation — interact with upstream ASR errors in speech‑based QA systems. Experiments on four English accents show that while richer retrieval structures improve absolute F1, they simultaneously widen the gap between clean‑text performance and noisy WER results by 36–67% across three benchmarks.

## Key Takeaways
- The combination of entity‑graph linking and iterative reformulation amplifies ASR‑induced errors, increasing the F1 loss from clean text to high‑WER accents.  
- Corruption of query entities accounts for 87–96% of the degradation across all methods on 2WikiMultiHopQA.  
- Lightweight surface‑form mitigations cannot close most of this gap, indicating that downstream retrieval structure magnifies remaining entity errors.

## Context
Speech‑based AI pipelines rely heavily on ASR accuracy, yet few studies examine how retrieval augmentations propagate these upstream mistakes. This work highlights a hidden bottleneck where richer graph structures may seem beneficial but actually worsen performance under noisy inputs.

## Implications
For practitioners developing robust spoken QA systems, the findings suggest that downstream retrieval design must be carefully balanced against ASR reliability rather than assumed to compensate for it. Future research should explore error‑aware retrieval strategies that mitigate entity corruption before it propagates further.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22872v1)
