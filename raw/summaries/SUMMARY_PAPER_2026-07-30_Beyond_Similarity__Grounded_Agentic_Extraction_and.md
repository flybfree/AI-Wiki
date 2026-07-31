---
title: Beyond Similarity: Grounded Agentic Extraction and Expert-Adjudicated Evaluation of Intertextuality in Classical Chinese Histories
url: http://arxiv.org/abs/2607.27595v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_02-34-23Z_BeyondSimilarity_GroundedAgenticExtractionandExper.md
generated_at: 2026-07-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an agentic extraction framework that forces large language models to ground intertextual reuse in exact character spans and label it within a five‑dimensional typology. Evaluated on the Analects versus Book of Han, the method yields high precision scores while exposing confidence gaps. Scaling to the Twenty‑Four Histories demonstrates how similarity metrics miss rich citation patterns.

## Key Takeaways
- The extraction requires models to produce precise character spans and apply a five‑dimensional reuse typology rather than simple similarity scores.
- Expert adjudication reveals that surface‑visible dimensions are reliably captured while intent‑based dimensions remain contested, limiting the validity of certain annotations.
- Scaling the validated extractor across 65,380 comparisons recovers corpus‑level structure that raw similarity cannot express.

## Context
Current AI systems treat intertextuality as a retrieval problem using similarity scores, which ignore how and why texts reference each other. This work shifts focus to grounded, human‑informed annotation that respects textual nuance and intent, aligning with the need for richer semantic understanding in historical corpora.

## Implications
For scholars of classical Chinese literature, this framework provides a reliable way to map citation practices across centuries without overstating similarity. Practitioners can use it to build more interpretable AI models that capture cultural attitudes rather than just textual overlap.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27595v1)
