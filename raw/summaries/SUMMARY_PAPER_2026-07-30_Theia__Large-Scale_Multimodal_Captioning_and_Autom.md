---
title: Theia: Large-Scale Multimodal Captioning and Automated Validation of the Incidents1M Dataset for Data-Free Distillation
url: http://arxiv.org/abs/2607.28269v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-23-01Z_Theia_Large_ScaleMultimodalCaptioningandAutomatedV.md
generated_at: 2026-07-30 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new method to create high-quality multimodal captions from the vision-only Incidents1M dataset using two Qwen3.5 models and validates them with an image-blind LLM-as-a-Judge pipeline. It achieves 78.65 semantic agreement across 173,179 pairs and demonstrates conservative captioning with high precision (77.6%) and low recall (46.0%). The framework enables data-free distillation of disaster response knowledge.

## Key Takeaways
- The authors recover 100,000 images from Incidents1M and generate captions using a 4B dense Qwen3.5 model and a 35B MoE model.
- An image-blind LLM-as-a-Judge pipeline validates caption quality by simulating the student modality gap during data-free distillation.
- The evaluation shows high semantic agreement (78.65/100) between architectures while revealing annotation inconsistencies in ground truth.

## Context
Vision-language models face challenges when applied to disaster management due to limited or misaligned multimodal datasets. Data-free knowledge distillation offers a promising way to transfer knowledge without labeled captions, but requires reliable caption generation and validation. This work addresses both by producing a large-scale, LLM-validated dataset that can serve as a benchmark for DFKD.

## Implications
The generated dataset provides practitioners with a scalable resource for training robust disaster response AI systems. By exposing annotation flaws, it encourages more accurate human labeling processes. The approach also sets a template for automated validation pipelines in multimodal learning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28269v1)
