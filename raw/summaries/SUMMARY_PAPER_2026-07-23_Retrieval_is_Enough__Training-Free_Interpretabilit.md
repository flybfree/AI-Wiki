---
title: Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent
url: http://arxiv.org/abs/2607.16448v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_18-47-31Z_RetrievalisEnough_Training_FreeInterpretabilitywit.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HARP, a training‑free interpretability framework where an LLM agent retrieves activation samples from a vector database and builds hypotheses that are validated with linear probes. Despite lacking any model training, HARP surpasses state‑of‑the‑art training‑based methods on concept discovery, detection, steering, and secret elicitation.

## Key Takeaways
- HARP reaches state‑of‑the‑art performance on concept discovery without ever training the underlying neural network.  
- The retrieval‑driven pipeline uncovers insights that are not present in the original training data, suggesting training‑based methods may be limited to what is already stored.  
- By using a vector database and activation manipulation tools, HARP remains cheap, flexible, and can index new datasets on demand whenever existing ones prove insufficient.

## Context
Interpretability research balances cost versus insight extraction: expensive training‑based techniques rely on large activation datasets, while cheaper training‑free methods often fall short. This work demonstrates that retrieval can match or exceed those expensive approaches, highlighting a gap in current interpretability tooling.

## Implications
Practitioners should weigh whether the additional insight gained justifies the cost of training models for interpretability. Benchmarking must require evidence that new insights go beyond what is recoverable from the original data, encouraging more rigorous evaluation standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16448v1)
