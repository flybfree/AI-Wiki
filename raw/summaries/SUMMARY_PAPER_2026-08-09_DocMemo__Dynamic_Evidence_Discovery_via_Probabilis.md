---
title: DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding
url: http://arxiv.org/abs/2608.07067v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-16-56Z_DocMemo_DynamicEvidenceDiscoveryviaProbabilisticMe.md
generated_at: 2026-08-09 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
DocMemo introduces a memory‑guided framework for long‑document understanding that enables dynamic evidence discovery across hundreds of pages. It overcomes limitations of static retrieval by maintaining three memory components and using Bayesian updating to refine page selection iteratively. The framework demonstrates state‑of‑the‑art performance on three benchmarks.

## Key Takeaways
- DocMemo maintains a tri‑level retrieval state consisting of Document Schema Memory, Page Belief Memory, and Question Episodic Memory, which respectively capture structural priors, dynamic relevance estimation, and query‑specific reasoning trajectories.  
- It uses Thompson sampling for Bayesian page belief updating to continuously refine cross‑round page selection.  
- Spatial proximity propagation and structure‑aware adaptive‑granularity evidence access improve the acquisition of fine‑grained visual regions.

## Context
Long‑document understanding remains a challenge because systems must locate sparse, heterogeneous evidence across many pages while tracking relevance changes between retrieval rounds. Existing methods either fix a top‑k page set or lack mechanisms to propagate dynamic relevance updates, limiting their effectiveness.

## Implications
This work advances AI research by providing a structured memory framework applicable beyond document understanding, such as in knowledge tracing and multi‑modal reasoning. Practitioners can leverage Thompson sampling for adaptive information retrieval in large‑scale data pipelines, improving both efficiency and accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07067v1)
