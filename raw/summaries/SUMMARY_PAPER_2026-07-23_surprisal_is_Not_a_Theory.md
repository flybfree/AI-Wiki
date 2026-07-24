---
title: surprisal is Not a Theory
url: http://arxiv.org/abs/2607.20208v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-28-28Z_surprisalisNotaTheory.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that surprisal theory is often presented as a computational-level explanation but fails to account for the representational choices underlying large language model probabilities. It demonstrates through three analyses that algorithm and architecture significantly affect probability computation, showing that treating LLM outputs as interchangeable obscures these commitments.

## Key Takeaways
- The uncritical use of surprisal metrics hides the representational decisions made by different models.
- Model architectures and algorithms directly influence computed language model probabilities.
- Researchers testing surprisal theory must re-evaluate the assumption that large language model probabilities are interchangeable.

## Context
In AI research, computational-level theories like surprisal aim to explain model behavior without reference to internal representations. This paper highlights a gap: while such theories claim representation‑agnosticism, LLMs rely on specific architectures and algorithms that generate probabilities in non‑transparent ways.

## Implications
For practitioners, ignoring these representational details can lead to misleading conclusions about model performance. The field must adopt more nuanced approaches that consider algorithmic and architectural specifics when evaluating surprisal based theories.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20208v1)
