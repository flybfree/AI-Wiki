---
title: MosaicJoin: Compact Semantic Sketches for Value-Level Join Discovery
url: http://arxiv.org/abs/2607.21781v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_19-55-19Z_MosaicJoin_CompactSemanticSketchesforValue_LevelJo.md
generated_at: 2026-07-26 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
MosaicJoin is a value-level semantic join discovery method that balances accuracy and scalability for high‑cardinality columns. The paper demonstrates that it outperforms existing approaches while running up to 66 times faster, requiring no training or fine‑tuning. It supports query columns with up to 57K values and data lake columns with up to 1M values.

## Key Takeaways
- MosaicJoin introduces a sketching strategy that approximates joinability without comparing all values.
- It scores candidate sketches at query time with cost bounded by the sketch size, enabling efficient retrieval even for high‑cardinality columns.
- The method scales to query columns up to 57K values and data lake columns up to 1M values.

## Context
Join discovery is essential for dataset search but traditional methods either compare all values or encode whole columns poorly. MosaicJoin bridges this gap with value‑level approximations that maintain accuracy while scaling.

## Implications
This approach reduces retrieval latency dramatically, making large‑scale semantic join queries feasible in data lakes and open repositories. Practitioners can deploy it without training overhead, improving efficiency across enterprise analytics pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21781v1)
