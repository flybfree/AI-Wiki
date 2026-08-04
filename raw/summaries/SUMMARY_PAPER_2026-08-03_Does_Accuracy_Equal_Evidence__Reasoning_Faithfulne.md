---
title: Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression
url: http://arxiv.org/abs/2608.01631v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-03-53Z_DoesAccuracyEqualEvidence_ReasoningFaithfulnessund.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether compressing the key‑value cache in large language models reduces both answer accuracy and the supporting reasoning that justifies those answers. Experiments across multiple tasks show a divergence: some compression methods keep final‑answer accuracy high while eroding chain consistency, highlighting an “answer‑evidence gap”. The findings suggest that accuracy alone does not guarantee faithfulness to the evidence behind it.

## Key Takeaways
- Token‑eviction compression can maintain competitive final‑answer accuracy but often degrades answer‑chain consistency and perturbation faithfulness. - The paper introduces a controlled replay protocol that isolates whether compression preserves usable information from an existing trace, revealing that the gap stems from losing parts of the reasoning trace rather than mere memory reduction. - A coverage‑preserving quantization method shows less impact, indicating that failure is tied to trace loss more than KV memory size.

## Context
Large language models rely on KV caches to maintain context during generation; compression techniques aim to reduce memory usage for efficient inference. Evaluating only final accuracy overlooks the quality of intermediate reasoning, a gap that can affect trustworthiness and safety in high‑stakes applications.

## Implications
For practitioners, compressing KV caches must be balanced with preserving reasoning traces to avoid misleading outputs. The research urges systematic evaluation beyond accuracy, such as chain consistency metrics, to ensure compressed models remain reliable for complex tasks like medical or scientific QA.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01631v1)
