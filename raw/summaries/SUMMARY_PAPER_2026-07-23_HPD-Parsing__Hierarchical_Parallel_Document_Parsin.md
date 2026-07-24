---
title: HPD-Parsing: Hierarchical Parallel Document Parsing
url: http://arxiv.org/abs/2607.18839v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_08-25-32Z_HPD_Parsing_HierarchicalParallelDocumentParsing.md
generated_at: 2026-07-23 23:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes HPD-Parsing, a hierarchical parallel decoding framework that replaces the sequential token‑by‑token generation of full‑page document parsers with a layout branch and concurrent block branches. Experiments on public benchmarks show it reaches 4752 tokens per second, delivering 2.62× the throughput of the fastest existing model and 3.06× faster than a vanilla autoregressive baseline while keeping parsing accuracy competitive.

## Key Takeaways
- Layout analysis must be performed globally because document structure cannot be captured locally.
- HPD-Parsing assigns block‑level content decoding to parallel branches that are dynamically linked to the layout branch.
- Progressive multi‑token prediction (P‑MTP) reduces the number of decoding steps within each branch, boosting speed.

## Context
Current unified Vision‑Language Model document parsers treat every page as a single sequential generation task, creating bottlenecks that scale with document length. This work introduces a paradigm that aligns parsing with the principle of teamwork: global coordination for layout and parallel execution for block content, offering a more scalable approach.

## Implications
Faster parsing enables real‑time processing of large documents in legal, medical, and enterprise settings without sacrificing accuracy. Practitioners can adopt HPD-Parsing to improve system responsiveness and reduce computational costs at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18839v1)
