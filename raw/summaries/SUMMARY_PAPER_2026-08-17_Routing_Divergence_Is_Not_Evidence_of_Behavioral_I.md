---
title: Routing Divergence Is Not Evidence of Behavioral Influence in Same-Weight MoE Self-Distillation
url: http://arxiv.org/abs/2608.15787v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_15-07-17Z_RoutingDivergenceIsNotEvidenceofBehavioralInfluenc.md
generated_at: 2026-08-17 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether routing divergence in same-weight MoE self-distillation indicates behavioral influence. It finds that while the routing term changes which expert processes a token, its impact on output is small compared to the dense-like content term. Across models, the routing term accounts for only $1.6\times$ as a fraction of block output versus $3.2$ for residual-stream exposure.

## Key Takeaways
- The routing term spans only $1.6\times$ as a fraction of block output, indicating minimal direct influence on model behavior.
- Residual-stream exposure ranges up to $3.2\times$, showing that routing changes are overshadowed by content-related effects.
- Full routing term movements are less than half the natural context effect and largely explained by matched-norm noise.

## Context
Mixture-of-experts architectures aim for efficiency, but self-distillation with shared weights raises questions about whether routing alone can drive learning. This study clarifies that routing is a minor component relative to content-driven changes in MoE behavior.

## Implications
For practitioners, focusing on residual-stream exposure rather than routing simplifies interventions. It suggests that training strategies should target content alignment rather than attempting to alter expert assignment for distillation gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15787v1)
