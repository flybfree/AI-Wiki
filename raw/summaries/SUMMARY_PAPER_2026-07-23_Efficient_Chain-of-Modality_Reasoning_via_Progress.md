---
title: Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models
url: http://arxiv.org/abs/2607.19932v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_09-04-55Z_EfficientChain_of_ModalityReasoningviaProgressiveC.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Efficient Chain-of-Modality Reasoning (ECoM Reasoning), a framework that compresses the textual component of spoken language models to serve both speech guidance and reasoning representation, thereby improving accuracy while using fewer tokens. Experiments on spoken mathematical question answering show that ECoM Reasoning boosts performance by 21 % compared with standard Chain-of-Modality without explicit traces and by 3 % over CoM with full traces, all within a 40 % token budget.

## Key Takeaways
- The model compresses textual reasoning into the speech guidance stream, reducing token usage to about half of the original chain.  
- Progressive Compression trains the model from full‑form reasoning to compressed reasoning through a curriculum that gradually removes text tokens.  
- Despite the compression, ECoM Reasoning achieves higher accuracy than both standard CoM and CoM with explicit traces.

## Context
Spoken language models face a gap in reasoning compared to their textual counterparts because they must interpret verbalized expressions without symbolic representation. This work addresses that gap by integrating reasoning directly into the speech pipeline, showing that efficiency and performance can coexist in multimodal AI systems.

## Implications
For developers building voice‑enabled assistants, ECoM Reasoning offers a practical way to enhance question answering accuracy while keeping latency low. The approach signals that compressed reasoning is viable for real‑world deployment, encouraging further research into lightweight, multimodal models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19932v1)
