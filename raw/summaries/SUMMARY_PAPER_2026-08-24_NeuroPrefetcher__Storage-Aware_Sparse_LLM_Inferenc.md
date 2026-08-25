---
title: NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching
url: http://arxiv.org/abs/2608.22643v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_22-58-11Z_NeuroPrefetcher_Storage_AwareSparseLLMInferencevia.md
generated_at: 2026-08-24 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
NeuroPrefetcher addresses the challenge of running large language models on edge devices where model size exceeds resident memory. By exploiting temporal locality in MLP activity, it predicts which sparse weights will be needed for each token and prefetches only those delta rows from storage, achieving a 7.9‑12.0× speedup over existing approaches.

## Key Takeaways
- The system predicts active neurons across all downstream MLP layers using a single GPU‑resident predictor that occupies just 2.86% of the base model parameters.  
- Prefetching is triggered only for incoming delta rows, replacing reactive OS demand paging with explicit, model‑aware weight movement.  
- On unified‑memory edge hardware, NeuroPrefetcher delivers up to a twelvefold performance improvement under constrained memory budgets.

## Context
Large language models are increasingly deployed on resource‑limited devices, yet traditional techniques like quantization or offloading still require the model to be partitioned within a fixed memory budget. The gap between model size and available memory remains a bottleneck for real‑world edge inference.

## Implications
This work demonstrates that storage can be leveraged as an active component of inference rather than merely a fallback resource, offering a scalable path toward truly large models on edge hardware. Practitioners can adopt similar predictive prefetching strategies to reduce latency and power consumption in AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22643v1)
