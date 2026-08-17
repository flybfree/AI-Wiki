---
title: When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics
url: http://arxiv.org/abs/2608.13835v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_23-54-41Z_WhenLexicalChangeMisleads_RethinkingDynamicTopicMo.md
generated_at: 2026-08-16 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how traditional coherence metrics perform when dynamic topic models are evaluated on datasets where vocabulary shifts but semantic meaning remains stable. It finds that LLM‑based semantic similarity aligns much better with human judgments than temporal coherence, especially for CoNTM topics in NYT, DBLP, and arXiv.

## Key Takeaways
- Traditional temporal coherence shows weak agreement with human judgments, ranging from ρ = -0.256 to 0.614 across the three datasets, indicating high variability.
- LLM‑based semantic similarity achieves strong alignment with human semantic judgments for CoNTM topics in NYT (ρ = 0.609), DBLP (ρ = 0.721) and arXiv (ρ = 0.502), while being less consistent for DLDA.
- Lexical‑change stratification reveals that aggregate evaluation masks important differences, underscoring the need to report both traditional and LLM‑based coherence measures.

## Context
Dynamic topic modeling is widely used to capture evolving language patterns in scientific and news corpora, yet standard evaluation relies on temporal coherence alone. This study highlights a limitation: when lexical changes occur without semantic drift, conventional metrics become misleading, prompting a call for alternative semantic assessment methods.

## Implications
For researchers, practitioners should adopt LLM‑based semantic similarity as a complementary metric to traditional coherence scores in dynamic topic modeling. Industry applications that rely on interpretable topics must therefore report both types of measures to avoid misinterpretation and ensure robust topic representation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13835v1)
