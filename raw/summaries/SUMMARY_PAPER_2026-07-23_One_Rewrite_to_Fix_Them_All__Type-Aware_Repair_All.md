---
title: One Rewrite to Fix Them All? Type-Aware Repair Allocation for Text-to-Image Prompt Optimization
url: http://arxiv.org/abs/2607.18724v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_05-31-43Z_OneRewritetoFixThemAll_Type_AwareRepairAllocationf.md
generated_at: 2026-07-23 23:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Type-Aware Repair Allocation (TARA), a framework that treats prompt optimization as atomic repair allocation by routing each failed proposition to a type‑conditioned repair operator before compiling local constraints into a single executable prompt. Experiments on DSG and TIFA across four frozen generators show TARA achieves the highest semantic accuracy, improving VisualPrompter by 5.6 points on DSG and 2.6 points on TIFA while running faster at 16 seconds per prompt versus 20 seconds.

## Key Takeaways
- Each failed proposition is routed to a type‑conditioned repair operator before the resulting local constraints are compiled into one executable prompt, allowing heterogeneous failures to be handled with appropriate language.
- TARA separates diagnosis, allocation, compilation, and a semantic repair gate that uses an accept‑or‑revert controller over exactly one prescribed repair to prevent semantic regressions.
- The framework is evaluated on DSG and TIFA across four frozen generators, demonstrating the best semantic accuracy in all eight benchmark‑generator cells.

## Context
Prompt optimization remains crucial for text‑to‑image models because they often generate images that deviate from user intent. Existing optimizers treat various failure modes uniformly, leading to suboptimal repairs or unnecessary prompt expansions. This work advances the field by formalizing repair allocation as a type‑aware process, enabling more precise and efficient prompt correction.

## Implications
For practitioners, TARA offers a way to produce higher‑quality images with minimal latency, integrating seamlessly into existing generation pipelines without retraining models. The approach can be adopted across diverse image generators to improve user satisfaction and reduce the need for manual prompt tweaking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18724v1)
