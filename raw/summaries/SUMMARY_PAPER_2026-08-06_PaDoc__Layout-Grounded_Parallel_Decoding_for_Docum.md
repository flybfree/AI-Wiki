---
title: PaDoc: Layout-Grounded Parallel Decoding for Document Parsing
url: http://arxiv.org/abs/2608.06146v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-16-18Z_PaDoc_Layout_GroundedParallelDecodingforDocumentPa.md
generated_at: 2026-08-06 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PaDoc, a layout-grounded parser that separates page layout and content decoding while sharing a common representation. It achieves high accuracy on OmniDocBench Full with an Overall layout F1 of 91.1 and a top-tier score of 94.24 among end-to-end parsers. The method also outperforms sequential baselines in speed and latency.

## Key Takeaways
- PaDoc uses a branching structure over a shared page representation to treat predicted layout as a factorization, allowing concurrent advancement of layout stream and regional content branches.
- It employs packed variable-length ancestor attention within a single MLLM, preserving visibility under standard next-token training while using masked parallel decoding for concurrent requests with cache reuse.
- On OmniDocBench Full PaDoc reaches an Overall score of 94.24, the best among end-to-end parsers, and improves valid-page throughput by up to 118% compared to a sequential baseline.

## Context
Document parsing remains a bottleneck in AI-driven document processing because current models treat entire pages as single sequences, limiting parallelism and increasing latency. This work addresses that limitation by decoupling layout and content decoding within a unified framework, aligning with trends toward efficient, scalable multimodal models.

## Implications
The approach enables faster document analysis for enterprise applications such as legal and medical record extraction where speed and accuracy are critical. By reducing P95 latency and improving throughput, PaDoc can support higher concurrency levels on limited hardware, making large-scale parsing more feasible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06146v1)
