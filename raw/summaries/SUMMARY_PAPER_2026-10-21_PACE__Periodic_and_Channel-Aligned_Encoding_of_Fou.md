---
title: PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States
url: http://arxiv.org/abs/2610.29545v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_10-31-52Z_PACE_PeriodicandChannel_AlignedEncodingofFour_BitR.md
generated_at: 2026-10-21 20:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PACE introduces a post-hoc four-bit quantization method for the recurrent states used in linear-attention language models, addressing the memory bottleneck that limits concurrent sequence decoding on accelerators. By rounding the state only periodically rather than after every generated token, exploiting column-aligned structure in gated-delta states, and selectively retaining higher-precision heads, PACE achieves competitive accuracy with eight-bit baselines at roughly two-thirds the memory footprint across models ranging from 4B to 35B parameters.

## Key Takeaways
- Periodic rounding dramatically reduces accumulated quantization error: existing quantizers round the recurrent state after every generated token, which compounds rounding errors over long sequences. PACE instead rounds only once every few tokens, mirroring the chunked-kernel strategy already used during prefill, and buffers intermediate tokens in a small buffer. This approach preserves the decoding speedup that the buffer provides while substantially lowering the error that accumulates in the state, enabling four-bit precision without the accuracy loss that prior methods required higher bit widths or fine-tuning to overcome.
- Channel-aligned quantization exploits structural regularity in gated-delta states: the authors discovered that large entries in the gated-delta state cluster in specific columns because certain channels of the per-token update remain large across many tokens. PACE leverages this by sharing a single quantization scale within each column rather than applying independent scales, which reduces quantization noise without requiring per-entry calibration and makes the scheme practical for deployment.
- Mixed-precision head selection provides a practical accuracy-memory tradeoff: PACE identifies which attention heads retain rounding error longest and keeps those heads at eight bits while quantizing the rest to four bits. On three larger hybrid models this mixed configuration matches eight-bit DAMP performance at about two-thirds the memory, and a fully four-bit configuration outperforms Q-Mamba at equal memory, demonstrating that selective precision allocation is more effective than uniform quantization.

## Context
Linear-attention and hybrid language models such as Mamba-based architectures store their entire context in a fixed-size recurrent state rather than a growing key-value cache, making state memory the dominant constraint on how many sequences an accelerator can decode simultaneously. Prior quantization work on these states, including DAMP and Q-Mamba, has shown that aggressive bit-width reduction after every token step degrades generation quality, forcing practitioners to either accept higher memory usage or fine-tune models. PACE reframes the problem by recognizing that the temporal structure of state updates and the spatial structure of gated-delta channels offer exploitable regularities that uniform per-token quantization ignores.

## Implications
For inference-serving teams operating hybrid or linear-attention models at scale, PACE offers a drop-in post-hoc quantizer that can nearly double effective batch throughput on a given accelerator without retraining, directly reducing serving cost and latency for high-concurrency workloads. The finding that quantization error accumulates primarily through per-token rounding rather than through the state representation itself suggests that future quantization research should focus on temporal scheduling and structural alignment rather than solely on bit-width selection, potentially informing hardware-aware kernel design and next-generation state-compression techniques for long-context generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29545v1)
