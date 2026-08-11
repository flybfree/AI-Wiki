---
title: FailForge: Distilling Procedural Competence from Persistent Failures into Code Agents
url: http://arxiv.org/abs/2608.08570v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_08-22-57Z_FailForge_DistillingProceduralCompetencefromPersis.md
generated_at: 2026-08-10 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FailForge, a method that transforms rejected rollouts from code‑agent training into useful skill instructions. By diagnosing failures and injecting distilled skills back into the agent’s context, it recovers over 26% of previously failed instances while keeping the model free of external hints at inference time.

## Key Takeaways
- The discarded failure samples are the hardest cases that standard rejection sampling fine‑tuning ignores.  
- FailForge converts each error feedback into a concise skill that is added to the training corpus and then removed before final training.  
- Augmented data boosts SWE‑bench Verified resolve by 6.6 points on Qwen3.5‑4B, especially for difficult problems.

## Context
Current code‑agent training relies heavily on successful trajectories, leaving a large gap in learning from failures that are costly to generate and informative for improvement. This work addresses the limitation of RFT by making use of the most challenging examples as training signals.

## Implications
Practitioners can integrate failure analysis into their fine‑tuning pipelines without sacrificing inference performance, potentially accelerating progress toward more robust code agents. The approach may also serve as a template for other domains where costly failures are abundant.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08570v1)
