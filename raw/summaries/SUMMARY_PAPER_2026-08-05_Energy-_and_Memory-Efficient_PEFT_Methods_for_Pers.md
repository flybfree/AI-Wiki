---
title: Energy- and Memory-Efficient PEFT Methods for Personalized On-Device SLMs on Consumer GPUs
url: http://arxiv.org/abs/2608.04488v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-20-57Z_Energy_andMemory_EfficientPEFTMethodsforPersonaliz.md
generated_at: 2026-08-05 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates five parameter‑efficient fine‑tuning methods for small language models on consumer GPUs and evaluates them across multiple architectures, tasks and personalization benchmarks while measuring both energy consumption (NetScore‑E) and memory usage (NetScore‑M). It finds that LoRA+ dominates in energy‑focused comparisons and QLoRA excels when VRAM is the limiting factor. The study also demonstrates that compact SLMs combined with PEFT provide a practical path to personalized on‑device deployment.

## Key Takeaways
- LoRA+ achieves the highest NetScore-E in 19 of 24 configurations, indicating it is the most energy‑efficient PEFT approach across all models and tasks.  
- QLoRA reduces peak finetuning VRAM by up to 3.9× for Transformer models, giving it the best NetScore-M in five Transformer configurations despite higher de‑quantization overhead.  
- Full fine‑tuning and BitFit are rarely competitive on either energy or memory metrics, while TinyLlama‑1.1B leads the NetScore‑E on five benchmarks and the NetScore‑M on four.

## Context
These findings highlight a growing need for lightweight, personalized AI that can run locally without draining battery life or requiring high‑end hardware. In the era of mobile AI, such benchmarks help guide hardware optimization decisions.

## Implications
For developers, the paper suggests prioritizing LoRA+ when energy is the primary constraint and QLoRA when memory is tight. Practitioners should benchmark both NetScore‑E and NetScore‑M to align method selection with real deployment priorities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04488v1)
