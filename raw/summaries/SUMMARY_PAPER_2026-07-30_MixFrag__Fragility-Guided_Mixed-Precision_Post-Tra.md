---
title: MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers
url: http://arxiv.org/abs/2607.28589v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-43-36Z_MixFrag_Fragility_GuidedMixed_PrecisionPost_Traini.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MixFrag, a fragility‑guided mixed‑precision post‑training quantization framework for Vision Transformers that allocates bits adaptively to each component based on its sensitivity to quantization error. By estimating component‑level fragility through KL divergence and solving the allocation as a multiple‑choice knapsack problem, MixFrag achieves competitive classification performance under realistic bit budgets while improving detection metrics compared with prior methods.

## Key Takeaways
- The fragility metric is computed as the Kullback–Leibler divergence between full‑precision and isolated quantized output distributions using a small calibration set.  
- Bit allocation follows a multiple‑choice knapsack formulation, allowing each transformer layer to choose among available precision levels within a fixed bit budget.  
- Experiments on ImageNet‑1K show MixFrag reaches state‑of‑the‑art classification results and lifts COCO object detection AP by up to 9.6 points in the MP3/MP3 setting.

## Context
Vision Transformers are increasingly deployed on edge devices where memory and compute are limited, making mixed‑precision quantization essential. Existing approaches often apply uniform bit widths, which can waste precision on robust layers while under‑utilizing it on fragile ones, limiting overall model quality.

## Implications
MixFrag demonstrates that component‑aware quantization can significantly boost performance without sacrificing accuracy, offering a practical path for deploying high‑quality Vision Transformers on resource‑constrained hardware. Practitioners can leverage fragility analysis to design efficient inference pipelines that balance speed and fidelity across diverse models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28589v1)
