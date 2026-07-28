---
title: GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models
url: http://arxiv.org/abs/2607.23913v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_01-06-20Z_GOTS_GreedyOrthogonalTokenSelectionforHigh_Resolut.md
generated_at: 2026-07-27 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Greedy Orthogonal Token Selection (GOTS), a method for reducing the token count in high‑resolution vision‑language models without retraining. By selecting tokens that maximize orthogonal residual energy to an already retained span, GOTS improves performance retention and lowers inference time.

## Key Takeaways
- GOTS selects each new token based on its largest residual energy orthogonal to the current retained visual span rather than pairwise importance or coverage.
- The selection rule maximizes the one‑step augmented Gram determinant, providing a local geometric guarantee for greedy expansion.
- Experiments across five high‑resolution VLM backbones and eleven benchmarks show higher average performance retention compared with strong baselines.

## Context
Vision‑language models now process thousands of visual tokens, inflating downstream language inference costs. Traditional token‑reduction techniques often rely on expensive importance scores or pairwise diversity metrics that do not scale well to high‑resolution inputs. GOTS offers a training‑free, query‑agnostic alternative grounded in linear algebra.

## Implications
For researchers and practitioners, GOTS demonstrates that geometric considerations can drive effective model compression without sacrificing quality. This approach reduces latency for real‑time applications and eases deployment on resource‑constrained devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23913v1)
