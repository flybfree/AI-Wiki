---
title: Reflector: Arrangement-Aware Harmonic Retrieval for Sample-Based Composition
url: http://arxiv.org/abs/2607.22413v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_15-30-30Z_Reflector_Arrangement_AwareHarmonicRetrievalforSam.md
generated_at: 2026-07-26 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
Reflector is an interactive audio workstation that adapts harmonic retrieval as a composer builds arrangements on a timeline. The system uses a learned embedding of interval-class combinations to score compatibility and retrieves material based on the evolving harmonic identity of the session, preserving pairwise judgments while covering the whole library.

## Key Takeaways
- The learned 128‑dimensional embedding approximates a hand‑designed interval‑class oracle, allowing fast dot‑product similarity scores that respect degenerate solutions favored by direct scoring.  
- Sweep‑line analysis identifies co‑sounding regions and computes weighted centroids, enabling retrieval against the composite harmonic identity of the session as it evolves.  
- The pipeline runs locally with no copyrighted data, using a synthetic training set and an open‑source implementation that preserves the kernel’s pairwise judgments.

## Context
This work advances AI‑driven music composition by integrating representation learning with real‑time interactive workflows. It demonstrates how embeddings can capture nuanced harmonic relationships without relying on copyrighted audio, highlighting a bridge between symbolic interval analysis and neural similarity metrics.

## Implications
For composers, Reflector offers a dynamic tool that stays in sync with arrangement decisions, reducing the need for manual re‑querying. For researchers, it shows that normalized embeddings can preserve kernel properties while offering richer coverage than direct scoring rules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22413v1)
