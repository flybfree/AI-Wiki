---
title: HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews
url: http://arxiv.org/abs/2609.03580v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_09-27-54Z_HalluPeer_ATaxonomy_drivenBenchmarkforDetectingHal.md
generated_at: 2026-09-03 20:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HalluPeer, a benchmark designed to detect hallucinations in scientific peer reviews by providing aligned triples of paper content, human‑written reviews, and hallucination‑injected reviews with detection, classification, and localization annotations. Experiments on 12K papers and 38K reviews reveal that current detectors cannot reliably separate fabricated claims from legitimate critique, while HalluPeer‑defined patterns appear in authentic peer review documents.

## Key Takeaways
- HalluPeer creates a taxonomy‑driven dataset where hallucinations are injected with automated filtering to reflect real‑world peer‑review contexts.  
- Existing detection models fail to distinguish hallucinated statements from genuine scholarly criticism, indicating a gap in source‑aware verification.  
- The benchmark demonstrates that hallucination patterns defined by HalluPeer are present in authentic reviews, underscoring the need for specialized evaluation.

## Context
The rapid adoption of large language models as review assistants amplifies concerns about unsupported claims in high‑stakes academic workflows. Existing hallucination benchmarks focus on generic text generation tasks and lack the technical depth required for scientific papers, creating a mismatch between research and practice.

## Implications
For AI developers, HalluPeer highlights the necessity of domain‑specific evaluation frameworks to ensure reliability in peer review assistance tools. Practitioners must adopt source‑aware verification methods to prevent misinformation from undermining scholarly integrity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03580v1)
