# Summary: 2026-08-03_10-30-27Z_DART_DecodedAttentionoverRecurrentStatesforEfficie.md
Saved: 2026-08-03 23:52
Source: 2026-08-03_10-30-27Z_DART_DecodedAttentionoverRecurrentStatesforEfficie.md
Model: None

---

## Summary  
The paper investigates whether a shared memory representation can simultaneously support the compact recurrent compression of state‑space models and the token‑level attention retrieval used in Transformers. By viewing the Mamba‑2 state as an associative key–value cache, the authors show that only values are currently decoded while keys remain undecoded. Their solution, DART (Decoded Attention over Recurrent States), decodes both keys and values from chunked scan memories and performs state‑memory attention to retrieve information efficiently. This approach reduces the length‑dependent inference cache dramatically compared with a matched attention baseline.

## Key Contributions  
- The authors discovered that Mamba‑2 stores token‑conditioned values in a compact recurrent state but does not decode token‑conditioned keys.  
- DART retains chunk‑state contributions from the Mamba‑2 chunked scan, decodes both keys and values from these memories, and performs state‑memory attention over the resulting KV pairs.  
- The combined output is fused with native Mamba‑2 output via a gated residual connection, enabling practical training with FlashAttention‑style computation.

## Methodology  
The authors adopt the state space duality (SSD) perspective of Mamba‑2, treating its hidden state as a compressed KV cache. They keep the chunked scan’s state contributions intact and implement a state‑memory attention (SMA) module that computes attention over token‑conditioned key–value pairs derived from these memories. SMA is realized using FlashAttention kernels to achieve O(N²) efficiency while reusing the existing chunked scan, thus avoiding additional memory overhead.

## Results  
Experiments on standard language‑model benchmarks demonstrate that DART cuts the inference cache length by up to 75 % when the chunk size S = 256 and state dimension N = 128 relative to a matched attention baseline. Moreover, DART improves associative recall and retrieval scores while preserving overall language‑modeling quality measured by perplexity.

## Significance  
By merging recurrent compression with attention‑style retrieval in a single memory representation, DART offers a path toward more efficient long‑context models that can scale to billions of tokens without exploding memory usage. The work bridges the gap between Transformers and SSMs, potentially enabling truly linear‑time inference for massive sequences.

## Related Concepts  
- State space model (SSM) / Mamba architecture  
- Chunked scan processing  
- Key–value cache representation  
- FlashAttention attention kernel
