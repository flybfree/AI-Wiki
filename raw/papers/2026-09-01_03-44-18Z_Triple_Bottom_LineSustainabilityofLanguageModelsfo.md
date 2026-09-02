---
title: Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs
published: 2026-09-01T03:44:18Z
authors: Jainil Dharmil Shah
url: http://arxiv.org/abs/2609.00665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs

## Abstract
Edge-AI model selection is commonly driven by one isolated metric - accuracy, latency, memory, energy, or safety, even though a deployable language model must balance all five. Our work focuses on answering the question whether na- tively trained small language models (SLMs) or large language models (LLMs) compressed through post-training quantization offer the more sustainable edge- deployment trade-off. We introduce a reproducible Holistic Sustainability Score (HSS) organized around the triple bottom line: an economic pillar for capability and systems efficiency, an environmental pillar for operational GPU energy and a social pillar for harmful-prompt robustness. Five BF16 SLMs and five LLMs under different quantization approaches - BF16, INT8, NF4 4-bit, GPTQ 4-bit, and GGUF Q4 produce 30 measured configurations. Capability is assessed on five zero-shot benchmarks; efficiency uses latency, throughput, peak VRAM and energy; and safety is approximated by attack success rate on five harmful prompts. Qwen3-30B-A3B/GGUF Q4 ranks first in the combined pool (93.38), followed by Mistral-Small-24B/GGUF Q4 (92.40), while Phi-4-mini/BF16 is the highest- ranked SLM in that pool (89.49). Thus, the hypothesis that native SLMs must be the most sustainable edge choice is not supported universally; optimized quantized LLMs can win overall, while SLMs remain competitive through lower resource demand. Quantization is a systems-level choice rather than a monotonic precision- efficiency trade-off and HSS remains relative to its comparison pool and proxy definitions.

## Metadata
- **Published**: 2026-09-01T03:44:18Z
- **Authors**: Jainil Dharmil Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00665v1)