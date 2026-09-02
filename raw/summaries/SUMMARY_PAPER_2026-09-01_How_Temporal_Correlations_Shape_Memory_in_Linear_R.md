---
title: How Temporal Correlations Shape Memory in Linear Recurrent Neural Networks
url: http://arxiv.org/abs/2609.00420v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_21-57-51Z_HowTemporalCorrelationsShapeMemoryinLinearRecurren.md
generated_at: 2026-09-01 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how temporal correlations in input sequences affect memory formation in linear recurrent neural networks (LRNNs). It derives exact learning dynamics and shows that correlation influences both the path of training and the final network behavior, leading to three key findings: correlation reshapes learning over time, a threshold determines when memory is retained, and zero‑error tasks can be learned with minimal memory. The study demonstrates that correlated data turns recurrent networks into change detectors.

## Key Takeaways
- Correlation reshapes the course of learning, not only its end; memory builds, overshoots, and is partly removed, resulting in a settled network that keeps less of the past.
- Memory switches off at a threshold set by how much each input resembles the previous one; neither sequence length nor longer‑range correlation moves this threshold.
- The best network changes too: zero error demands a feedthrough path that passes current input straight to output and remembers nothing, and training builds it unprompted when given one spare hidden dimension.

## Context
Understanding how input correlations affect learning dynamics is crucial for designing efficient recurrent models. This work provides an analytical framework that links input structure directly to memory behavior, offering insights beyond empirical tuning of network parameters.

## Implications
For practitioners, the findings suggest that correlated data can be leveraged to create detectors rather than memory‑heavy networks, potentially reducing computational cost. The theoretical link between correlation and learning may guide future research into adaptive architectures for time‑series prediction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00420v1)
