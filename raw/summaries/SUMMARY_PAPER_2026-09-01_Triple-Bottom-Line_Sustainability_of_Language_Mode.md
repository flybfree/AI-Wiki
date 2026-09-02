---
title: Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs
url: http://arxiv.org/abs/2609.00665v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_03-44-18Z_Triple_Bottom_LineSustainabilityofLanguageModelsfo.md
generated_at: 2026-09-01 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates the sustainability of deploying language models at the edge by comparing native small language models (SLMs) with quantized large language models (LLMs). It finds that optimized quantized LLMs often achieve higher holistic scores than SLMs, challenging the assumption that smaller models are universally more sustainable. The study also demonstrates that quantization choices such as BF16, INT8, NF4 4‑bit, GPTQ 4‑bit, and GGUF Q4 create distinct efficiency profiles.

## Key Takeaways
- The Holistic Sustainability Score (HSS) integrates economic capability, environmental energy use, and social safety across 30 model configurations, providing a single metric for trade‑off analysis.  
- Quantized LLMs such as Qwen3-30B-A3B/GGUF Q4 rank highest at 93.38, surpassing most SLMs and demonstrating that higher capability can outweigh resource costs in sustainability calculations.  
- Phi‑4‑mini/BF16, a native SLM, ranks third overall at 89.49, showing that low‑resource models remain competitive when efficiency is prioritized.

## Context
Edge AI deployment faces the challenge of balancing performance with limited hardware and energy budgets, making holistic evaluation essential for real‑world adoption. The results highlight that sustainability is not monotonic with precision reduction and depends heavily on the proxy definitions used for each pillar.

## Implications
This research shifts model selection from single‑metric optimization to comprehensive sustainability frameworks, guiding developers toward quantized LLMs when resource constraints are moderate but capability is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00665v1)
