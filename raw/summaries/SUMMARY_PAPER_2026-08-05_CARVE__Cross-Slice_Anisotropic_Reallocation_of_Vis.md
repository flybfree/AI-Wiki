---
title: CARVE: Cross-Slice Anisotropic Reallocation of Visual Evidence for Efficient 3D Medical Volume Understanding
url: http://arxiv.org/abs/2608.04515v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-49-49Z_CARVE_Cross_SliceAnisotropicReallocationofVisualEv.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CARVE, a training‑free method that reduces the number of visual tokens representing 3D medical volumes before feeding them to large language models. Experiments on two VQA benchmarks show that allocating the token budget more selectively yields better performance than simply increasing token count, with CARVE achieving up to 6.2 points higher report‑generation scores and preserving over 98 % of full‑token quality.

## Key Takeaways
- The study demonstrates diminishing returns in accuracy when visual tokens are added uniformly across slices, highlighting the inefficiency of expanding token budgets without strategic allocation.  
- CARVE compresses roughly 80 % of tokens on Hulu‑Med‑7B while outperforming all prior baselines across AMOS‑MM report‑generation metrics, indicating that selective token reduction can maintain high performance.  
- By partitioning the depth axis into windows and allocating tokens based on normalized cross‑slice evidence, CARVE creates spatial anchors that retrieve locally varying evidence from the full volume, effectively merging redundant tokens.

## Context
3D medical language models rely heavily on slice‑wise token sequences, which generate thousands of tokens per volume. This approach suffers from redundancy across adjacent slices, inflating computational cost without proportional gains in understanding. The paper’s work addresses this inefficiency by proposing a compression strategy that is independent of training and compatible with existing 2.5D token allocation models.

## Implications
CARVE offers a practical way to reduce memory usage and inference latency for large‑scale medical LLMs, enabling deployment on edge devices or lower‑cost cloud instances. For researchers and industry practitioners, the method underscores the importance of budgeting tokens based on content redundancy rather than sheer volume, paving the way for more efficient 3D vision‑language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04515v1)
