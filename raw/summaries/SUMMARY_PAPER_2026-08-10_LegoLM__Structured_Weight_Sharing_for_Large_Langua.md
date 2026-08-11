---
title: LegoLM: Structured Weight Sharing for Large Language Models
url: http://arxiv.org/abs/2608.08652v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_11-51-14Z_LegoLM_StructuredWeightSharingforLargeLanguageMode.md
generated_at: 2026-08-10 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LegoLM, a structured weight‑sharing compression method that addresses two failure modes in global weight sharing for large language models. The authors show that the framework reduces model size by up to 4.4× on Mistral‑7B while keeping perplexity loss minimal and outperforms standard post‑training quantization.

## Key Takeaways
- Distributional mismatch causes a linear increase in perplexity for low‑dimensional vector blocks, which can be eliminated with a scalar‑block encoding that removes the d‑linear penalty.  
- Outlier dominance leads to catastrophic quality loss because about 1/K of scalar weights fall beyond the Lloyd‑Max threshold and cannot be represented by centroids; selective replacement preserves these outlier values verbatim.  
- Adding selective replacement to per‑layer K‑means yields near‑lossless quality, confirming that this mechanism is dominant in compression performance.

## Context
Global weight sharing has been a focus of model compression research because it can dramatically reduce storage without retraining. However, existing methods often ignore the nuanced distribution of weights across layers and dimensions, leading to hidden degradation. LegoLM’s systematic analysis provides a data‑free solution that works for both small and large transformer models.

## Implications
For practitioners seeking efficient deployment of LLMs on constrained hardware, LegoLM offers a balance between compression ratio and quality preservation. The method can be applied across the model lifecycle, enabling higher compression without sacrificing downstream performance, which is crucial for real‑world applications where bandwidth and storage are limited.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08652v1)
