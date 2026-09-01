---
title: Geometry of Divergence: Tracking Hidden-State Trajectories for Adaptive Multi-Turn Reasoning
url: http://arxiv.org/abs/2608.30650v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_11-51-54Z_GeometryofDivergence_TrackingHidden_StateTrajector.md
generated_at: 2026-08-31 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper studies how LLM reasoning can be viewed as a hidden-state trajectory and uses geometric signals to improve multi-turn task success. By measuring temporal curvature and variance slope across four tasks with three LLMs, the authors show that these metrics can predict correct vs incorrect episodes before completion. The method also reveals action‑dependent separability in three‑action chains derived from four actions.

## Key Takeaways
- Temporal curvature captures directional consistency of turn‑to‑turn updates and helps distinguish correct reasoning paths from drift.
- Variance slope measures the growth or shrinkage of exploration space, providing a complementary signal for early error detection.
- The trajectory geometry identifies critical turns in multi‑action chains, boosting τ‑Bench success rates by 15.5 percentage points while cutting token cost by 11.2%.

## Context
Current LLM agents struggle with long interactions because accumulated context erodes task relevance, leading to representation drift that degrades performance. Traditional monitoring focuses on output quality rather than internal state dynamics, limiting proactive intervention.

## Implications
Understanding hidden‑state geometry enables more efficient reasoning pipelines that intervene before errors propagate. Practitioners can integrate curvature and variance metrics into real‑time agents to reduce token usage and improve success rates across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30650v1)
