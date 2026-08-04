---
title: DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling
url: http://arxiv.org/abs/2608.02032v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_10-30-27Z_DART_DecodedAttentionoverRecurrentStatesforEfficie.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DART, a method that combines recurrent state compression with attention retrieval in language modeling. It shows that Mamba‑2’s chunked scan can be used as a memory cache and that decoding token‑conditioned keys and values from this cache yields significant speedups. Experiments demonstrate up to 75 % reduction in inference cache length while maintaining model quality.

## Key Takeaways
- DART retains the chunk state contributions of Mamba‑2 as memories, then decodes both keys and values from these memories instead of only values.
- The attention computation is performed over the resulting key‑value pairs using a FlashAttention‑style operation that reuses the chunked scan.
- This hybrid approach reduces length‑dependent inference cache size by about 75 % for typical chunk sizes, compared with a matched attention baseline.

## Context
Current large language models face long‑term memory limits because attention scales quadratically with sequence length. Recurrent architectures offer linear scalability but lack efficient retrieval mechanisms. DART bridges this gap by reusing existing recurrent states as associative caches, enabling fast token‑conditioned lookups without sacrificing performance.

## Implications
For practitioners, DART provides a practical way to extend model context while keeping training and inference costs low. The technique could be adopted in production systems where long sequences are common, such as chatbots or document summarization, improving both efficiency and recall of information retrieval.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02032v1)
