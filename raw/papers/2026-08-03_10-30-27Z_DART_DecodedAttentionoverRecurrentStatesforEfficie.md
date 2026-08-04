---
title: DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling
published: 2026-08-03T10:30:27Z
authors: Yixiao Qian, Song Chen, Pengkai Wang, Jiaxu Liu, Shengze Cai, Chao Xu
url: http://arxiv.org/abs/2608.02032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling

## Abstract
Modern language models are built primarily from Transformers, recurrent models, and their hybrid architectures. Transformers rely on token-level attention memories, while recurrent models such as state space models (SSMs) and linear attention maintain compact recurrent states. These architectures are typically instantiated separately or interleaved at the layer level, leaving open whether a shared memory representation can support both recurrent compression and attention-style retrieval. We study this question through the state space duality (SSD) view of Mamba-2, where the SSM state can be interpreted as a compressed associative key--value (KV) cache. We observe that Mamba-2 decodes token-conditioned values from this state but does not decode token-conditioned keys. Based on this observation, we propose DART (Decoded Attention over Recurrent sTates), which retains the chunk state contributions produced by the Mamba-2 chunked scan as chunk state memories, decodes token-conditioned keys and values from these memories, and performs state-memory attention (SMA) over the resulting KV pairs. The retrieved output is then combined with the native Mamba-2 output through a gated residual connection. DART supports practical training by reusing the Mamba-2 chunked scan and implementing SMA as a FlashAttention-style computation. Our analysis and experiments show that DART substantially reduces the length-dependent inference cache compared with a matched attention baseline (e.g., $75\%$ savings when the chunk size is $S=256$ and the state size is $N=128$). Compared with Mamba-2, DART substantially improves associative recall and retrieval while preserving general language-modeling quality.

## Metadata
- **Published**: 2026-08-03T10:30:27Z
- **Authors**: Yixiao Qian, Song Chen, Pengkai Wang, Jiaxu Liu, Shengze Cai, Chao Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02032v1)