---
title: Anatomy Contextualized Adaption of CT Foundation Models
url: http://arxiv.org/abs/2607.27154v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_17-32-57Z_AnatomyContextualizedAdaptionofCTFoundationModels.md
generated_at: 2026-07-29 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Anatomy Contextualized Adaptation (ACA) to adapt frozen CT foundation model representations for anatomy-level vision-language alignment while preserving global contextual information. ACA leverages TotalSegmentator decompositions and a transformer that refines these embeddings, aligning them with both per-anatomy and scan-level text from radiology reports. The approach consistently outperforms baseline frozen models and existing fine-grained methods on Merlin and CT-RATE zero-shot classification tasks.

## Key Takeaways
- ACA adapts frozen CT foundation model representations for anatomy-level alignment using TotalSegmentator decompositions, refining embeddings via an inter-anatomy transformer that captures cross‑anatomy relationships.  
- The framework aligns per‑anatomy and scan‑level text from radiology reports to both anatomy embeddings and global context, improving zero‑shot classification performance.  
- Training requires less than one hour once embeddings are cached, making it computationally efficient compared to fine‑grained methods that train from scratch.

## Context
This work addresses the persistent trade‑off between fine‑grained anatomical detail and whole‑volume contextual information in CT vision‑language models, a challenge central to medical AI. By integrating anatomy‑specific alignment with global context, ACA shows that lightweight adaptation can rival full re‑training performance without sacrificing accuracy.

## Implications
For radiology practitioners, ACA provides a practical tool to enhance model interpretability through visualizable cross‑anatomy attention routes, fostering trust in clinical decision support. Industry adoption could accelerate the integration of CT foundation models into healthcare systems while keeping compute costs manageable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27154v1)
