---
title: A Feature-Major Codebook for Memory-Efficient Sparse-Binary Self-Organizing Maps: Scaling a MEDLINE Atlas to 1.05 Million Neurons on a Single Consumer GPU
url: http://arxiv.org/abs/2608.24067v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_04-55-07Z_AFeature_MajorCodebookforMemory_EfficientSparse_Bi.md
generated_at: 2026-08-25 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a feature‑major codebook for self‑organising maps that dramatically speeds up the best‑matching‑unit search, allowing training of extremely large maps on a single consumer GPU. By storing each feature’s weights contiguously and reusing them across a tile of samples, the BMU search is transformed into a tiled sparse‑dense product, yielding speedups of 4.5–8.5× while preserving exact argmin accuracy.

## Key Takeaways
- Feature‑major layout reduces BMU search time by 4.5–8.5× because each weight column is reused across a tile of samples during training.  
- The exact‑argmin BMU remains unchanged, so quantisation error matches the cuSPARSE baseline within 0.5% at every map size.  
- The approach enables training of maps with up to 262 144 neurons on one 24 GB GPU and reaches 1 048 576 neurons (1024×1024 edges) on a 141 GB H200, where other methods exceed memory limits.

## Context
Self‑organising maps are used to compress large corpora into two‑dimensional atlases, but the dominant BMU search is limited by bandwidth and memory. Traditional implementations cannot scale beyond a few thousand neurons due to these constraints, restricting their use for massive datasets like MEDLINE.

## Implications
This layout change makes SOM training feasible at map sizes that were previously impractical, lowering compute cost by roughly 82× compared with the legacy MedSOM implementation. Practitioners can now generate high‑resolution knowledge maps in seconds on consumer hardware, enabling real‑time or near‑real‑time large‑scale data visualisation and analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24067v1)
