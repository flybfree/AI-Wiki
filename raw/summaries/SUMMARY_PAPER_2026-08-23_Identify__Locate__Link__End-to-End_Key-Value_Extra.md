---
title: Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images
url: http://arxiv.org/abs/2608.20868v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_08-36-23Z_Identify_Locate_Link_End_to_EndKey_ValueExtraction.md
generated_at: 2026-08-23 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an end-to-end vision-language model that extracts key-value pairs directly from document images without OCR preprocessing. The model fine‑tunes SmolDocling, a compact 256M‑parameter VLM, to identify, locate, and link entities in a single pass. On benchmark datasets it achieves strong performance while being significantly smaller and faster than larger zero‑shot baselines.

## Key Takeaways
- The model integrates identification, localization, and association using specialized tags for key, value, region, and link, allowing many‑to‑many relationships to be captured in one output sequence.  
- A synthetic form‑filling augmentation pipeline combined with graph‑based crops preserves complete key‑value subgraphs, mitigating data scarcity.  
- Evaluation includes a layout‑aware framework that verifies spatial bounding boxes, ensuring extracted pairs are correctly positioned relative to each other.

## Context
Current document processing relies on multi‑stage pipelines where OCR errors propagate through downstream models, limiting efficiency and accuracy. Vision‑language models can bypass this bottleneck by understanding both visual layout and textual content simultaneously, offering a more robust alternative for structured information extraction.

## Implications
For industry practitioners, the lightweight architecture enables real‑time deployment in edge devices, reducing latency and computational cost. The approach also sets a new benchmark for zero‑shot VLM performance on document tasks, encouraging further research into compact yet effective multimodal models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20868v1)
