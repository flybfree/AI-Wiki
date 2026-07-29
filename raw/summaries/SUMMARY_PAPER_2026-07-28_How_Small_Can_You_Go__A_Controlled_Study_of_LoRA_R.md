---
title: How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model
url: http://arxiv.org/abs/2607.25583v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-12-03Z_HowSmallCanYouGo_AControlledStudyofLoRARank_Target.md
generated_at: 2026-07-28 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper conducts a controlled study of LoRA rank, target modules, and quantization on the 60M‑parameter T5‑small model for text‑to‑SQL tasks. It finds that LoRA with rank 16 recovers within 12 points of full fine‑tuning accuracy while using minimal extra parameters and memory. The study systematically varies LoRA rank from 2 to 32, evaluates each setting on the WikiSQL benchmark, and measures both task accuracy and system‑level overhead.

## Key Takeaways  
- LoRA rank 16 recovers 71.2% exact‑match to 59.6%, showing high efficiency.  
- QLoRA with INT8 or NF4 quantization reaches 52.8–53.2% accuracy using only 0.60 GB memory, highlighting low‑bit gains.  
- Training fewer than 1% of parameters yields comparable performance to full fine‑tuning.

## Context  
In AI research, parameter‑efficient fine‑tuning and model compression are pursued to fit large models into limited hardware, yet their combined impact is rarely examined on modestly sized encoders. This study bridges that gap by providing a reproducible benchmark for small models.

## Implications  
Practitioners can deploy text‑to‑SQL systems with high accuracy under strict memory constraints without sacrificing compute resources. The findings guide future work on efficient model adaptation and deployment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25583v1)
