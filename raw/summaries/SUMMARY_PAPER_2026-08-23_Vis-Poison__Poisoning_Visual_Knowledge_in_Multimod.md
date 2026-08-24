---
title: Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation
url: http://arxiv.org/abs/2608.20756v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_05-34-48Z_Vis_Poison_PoisoningVisualKnowledgeinMultimodalRet.md
generated_at: 2026-08-23 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
Vis-Poison is a new visual knowledge poisoning attack that targets multimodal retrieval-augmented generation systems by injecting poisoned images directly into the knowledge base without altering any associated text. The authors report an end‑to‑end success rate ranging from 40.16 % to 65.40 % across multiple RAG pipelines, demonstrating that visual evidence can be weaponized even when parametric knowledge remains intact.

## Key Takeaways
- Vis-Poison constructs visually plausible poisoned images using an automated multi‑agent method, making the attack independent of captions or metadata.  
- The attack achieves a success rate above 60 % against models that rely solely on parametric knowledge, showing its potency in black‑box settings.  
- Experiments across six generation models and four embedding models confirm consistent high performance, highlighting robustness to diverse model architectures.

## Context
Multimodal retrieval-augmented generation (RAG) systems increasingly depend on images as external knowledge sources, yet prior defenses have focused on textual metadata or captions. This paper shifts the attack surface to the visual payload itself, revealing a vulnerability that could undermine system reliability without changing any textual components.

## Implications
For practitioners, Vis-Poison underscores the need for robust image validation and provenance checks in multimodal pipelines. Industry stakeholders must consider adversarial image injection as a threat vector when deploying RAG solutions that integrate visual data to ensure trustworthy output generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20756v1)
