---
title: Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects
url: http://arxiv.org/abs/2607.24645v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_16-45-08Z_SparseAutoencodersEncodeBothConceptsandFunctions_T.md
generated_at: 2026-07-27 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how sparse autoencoder features influence model logits when the same feature is deactivated across different contexts, revealing that such features rarely behave as stable one‑dimensional steering directions. The authors introduce Feature‑Effect Geometry Analysis (FEGA) to quantify these changes and distinguish value‑like features tied to static attributes from pointer‑like features linked to context‑dependent operations.

## Key Takeaways
- Value‑like features produce structured, low‑dimensional effects that span multiple directions rather than a single axis.  
- Pointer‑like features generate diffuse effects that vary widely across prompts and do not provide consistent steering.  
- A feature can be both interpretable and causally relevant without offering a stable direction for manipulation.

## Context
Understanding the causal impact of model components is crucial for building trustworthy AI systems, yet existing interpretability tools often fail to capture nuanced feature behavior. This research addresses that gap by focusing on the geometric patterns of logit changes rather than static activation profiles.

## Implications
For practitioners, these findings suggest that feature selection should consider both value and pointer characteristics, improving model robustness and explainability in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24645v1)
