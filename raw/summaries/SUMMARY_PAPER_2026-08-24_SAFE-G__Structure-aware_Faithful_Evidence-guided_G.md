---
title: SAFE-G: Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering
url: http://arxiv.org/abs/2608.21796v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_06-34-53Z_SAFE_G_Structure_awareFaithfulEvidence_guidedGener.md
generated_at: 2026-08-24 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
SAFE-G is a Structure-Aware Faithful Evidence-guided Generation framework designed for knowledge-based visual question answering. It outperforms prior methods by 8.9% on Encyclopedic-VQA and 3.5% on InfoSeek, showing improved reasoning accuracy.

## Key Takeaways
- The paper introduces a coarse-grained hybrid search that fuses visual and textual modalities to recall candidate documents.
- A structure-aware fine-grained graph retrieval is used to filter noise and locate precise evidence within complex contexts.
- An RL strategy with an evidence-grounded reward ensures the model only credits correct answers when the selected evidence is correct, enforcing faithful reasoning.

## Context
Knowledge-based VQA requires models to integrate external knowledge sources while maintaining strict factual alignment. Current fusion approaches often miss structural dependencies and generate hallucinated answers, limiting reliability in real-world applications.

## Implications
This work demonstrates that precise evidence localization can substantially boost accuracy in multimodal QA systems. Practitioners may adopt SAFE-G’s retrieval‑reward loop to build more trustworthy AI assistants that rely on verifiable knowledge bases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21796v1)
