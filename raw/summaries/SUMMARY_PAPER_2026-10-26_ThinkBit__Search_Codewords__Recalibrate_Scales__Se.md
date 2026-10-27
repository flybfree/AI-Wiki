---
title: ThinkBit: Search Codewords, Recalibrate Scales, Select by Reasoning
url: http://arxiv.org/abs/2610.34886v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_05-56-35Z_ThinkBit_SearchCodewords_RecalibrateScales_Selectb.md
generated_at: 2026-10-26 23:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ThinkBit introduces a strictly scalar two-bit quantization framework designed specifically to preserve reasoning capabilities in large language models, addressing the gap between traditional quantization metrics like perplexity and actual reasoning performance. The framework employs a multi-stage pipeline including sensitivity-based bit allocation, Gumbel-softmax codeword search, knowledge-distillation-based scale recalibration, and quantization-aware training, ultimately achieving 46.7 on MATH-500 with Qwen3-1.7B at 0.52 GB and 94.8 on MATH-500 at 14B scale, approaching the bfloat16 baseline of 97.5.

## Key Takeaways
- ThinkBit uses a sensitivity metric to assign each layer a ternary, 2-bit, or 3-bit tier, enabling optimal bitwidth allocation across layers rather than uniform quantization, which is critical because reasoning tasks stress different layers differently and a one-size-fits-all approach degrades performance disproportionately on harder problems.
- The framework combines a Gumbel-softmax-based scalar quantization algorithm that searches for optimal codewords block by block with a knowledge-distillation-based recalibration stage that freezes codewords but adjusts shared bfloat16 scales, capturing inter-layer interactions that purely layerwise quantization misses, followed by a short QAT stage that reassigns codewords to mimic the base model's distribution.
- A paired reasoning test on training problems is used as a checkpoint selection mechanism between the recalibration and QAT stages, and the resulting model at 0.52 GB outperforms every published 2-bit GGUF of Qwen3-1.7B on MATH-500, while scaling to 14B yields a 3.74 GB model scoring 94.8 versus 97.5 for the 29.5 GB bfloat16 original, demonstrating near-lossless reasoning preservation at extreme compression.

## Context
This work sits at the intersection of model compression and reasoning capability preservation, a critical frontier as reasoning language models generate thousands of tokens per answer and inference speed is bottlenecked by memory bandwidth. Traditional quantization evaluation relies on perplexity and multiple-choice accuracy, which fail to capture whether a compressed model can still perform multi-step reasoning on complex problems like competition mathematics. ThinkBit directly challenges the assumption that aggressive quantization inherently destroys reasoning ability by demonstrating that careful codeword search, scale recalibration, and reasoning-aware checkpoint selection can maintain near-baseline performance at 8× memory savings.

## Implications
For practitioners deploying reasoning models on edge devices or in cost-constrained environments, ThinkBit demonstrates that two-bit quantization no longer requires accepting a severe reasoning penalty, potentially enabling on-device deployment of capable reasoning models at a fraction of the memory footprint. For the broader field, the paper signals that evaluation protocols must evolve beyond perplexity and multiple-choice benchmarks toward reasoning-specific tests, and that quantization pipelines need reasoning-aware stages like knowledge distillation and paired reasoning selection to remain viable for chain-of-thought workloads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34886v1)
