---
title: Tetra: Serving Leech-Lattice Quantized LLMs at 2.7 Bits per Parameter
published: 2026-09-28T15:51:56Z
authors: Pier-Jean Malandrino
url: http://arxiv.org/abs/2609.35465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tetra: Serving Leech-Lattice Quantized LLMs at 2.7 Bits per Parameter

## Abstract
Leech-lattice quantization gives good quality at two bits per weight, but its codebooks hold more than 10^14 points, too many for a lookup table. Our earlier kernel expanded the codes at load time and read 4.804 bits per weight from GPU memory for 2 bits of code. We present Tetra, a new codebook on the same lattice. A 24-weight block still takes 48 bits, most of which index a 64-state trellis of the Golay code and one shared 16 KiB table. The kernel decodes a block with six table loads and two small lookups inside the matrix-vector product, and reads 2.148 bits per weight. For full models, we retrain one scale per matrix row, store the matrices that lose the most as 4-bit integers, and pay for them with 4-bit embedding tables. Our Qwen3-4B, 8B and 14B files hold 2.73, 2.70 and 2.73 bits per parameter over the whole model. They score 63.37, 69.58 and 75.66 on the full MMLU test set, 4.76, 4.21 and 2.46 points below 4-bit AWQ at 5.3 to 6.0 bits per parameter. They generate 113.8, 95.0 and 57.2 tokens per second in our engine. On GSM8K, through the served kernel, they lose 9.63, 4.62 and 3.26 points to FP16. At 4B our file scores 23.6 points above llama.cpp's IQ2_XXS (2.48 bits per parameter). Every number we measured for a table or figure comes from one NVIDIA L40S GPU. We preregistered the main experiments.

## Metadata
- **Published**: 2026-09-28T15:51:56Z
- **Authors**: Pier-Jean Malandrino
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35465v1)