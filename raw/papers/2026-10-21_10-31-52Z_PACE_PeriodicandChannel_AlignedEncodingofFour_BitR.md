---
title: PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States
published: 2026-10-21T10:31:52Z
authors: Patrick Haller, Filipe Laitenberger, Alan Akbik
url: http://arxiv.org/abs/2610.29545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States

## Abstract
Linear-attention language models keep their context in a recurrent state of fixed size, where an inference system stores one copy of this state for every sequence it decodes at the same time. Storing the state at lower precision therefore lets more sequences share an accelerator. Existing state quantizers round the state after every generated token and report that four bits lose accuracy unless the bit width is raised or the model is fine-tuned.\par We introduce PACE, a post-hoc four-bit state quantizer. PACE rounds the state only once every few generated tokens, as chunked kernels already do once per chunk during prefill, and keeps the tokens generated in between in a small buffer. Rounding less often reduces the error that accumulates in the state. Additionally, we find that the large entries of the gated-delta state gather in columns, because some channels of the update written at each token remain large across many tokens. PACE therefore shares each quantization scale within one column. It also keeps the heads that retain rounding error longest at eight bits. On four hybrid models from 4B to 35B parameters, PACE with mixed four- and eight-bit heads is competitive with eight-bit DAMP on the three larger models at about two thirds of its memory, PACE with four-bit heads throughout scores higher than Q-Mamba at equal memory, and rounding every few tokens preserves the decoding speedup of the buffer.

## Metadata
- **Published**: 2026-10-21T10:31:52Z
- **Authors**: Patrick Haller, Filipe Laitenberger, Alan Akbik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29545v1)