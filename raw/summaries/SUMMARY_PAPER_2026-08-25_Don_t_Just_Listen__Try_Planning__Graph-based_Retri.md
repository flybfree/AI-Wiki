---
title: Don't Just Listen, Try Planning: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding
url: http://arxiv.org/abs/2608.24048v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_04-16-42Z_Don_tJustListen_TryPlanning_Graph_basedRetrieval_G.md
generated_at: 2026-08-25 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LongAudioQA, a dataset and GRGA model designed to improve long-form audio meeting understanding by addressing acoustic information loss and weak context retention in speech QA tasks. The GRGA model encodes heterogeneous audio features into a multi‑dimensional graph and uses agent planning for retrieval and answer generation.

## Key Takeaways
- LongAudioQA is built to fill the gap of scarce task‑specific question answering datasets for long‑form audio meetings, enabling more realistic evaluation.  
- GRGA models audio features as nodes in a heterogeneous graph, preserving rich temporal and acoustic relationships across the meeting transcript.  
- The agent planning component explicitly selects relevant sub‑graphs for retrieval before generating answers, improving both recall and coherence.

## Context
Current speech QA systems often discard fine‑grained acoustic cues, leading to shallow understanding of spoken content. This work advances multimodal graph neural networks by integrating audio data directly into a structured representation, offering a pathway toward more faithful dialogue comprehension.

## Implications
For industry practitioners, GRGA can be deployed to extract actionable insights from lengthy meetings without manual transcription, reducing costs and improving decision‑making. Researchers will benefit from the LongAudioQA benchmark, which encourages novel methods that respect long‑term context in spoken language processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24048v1)
