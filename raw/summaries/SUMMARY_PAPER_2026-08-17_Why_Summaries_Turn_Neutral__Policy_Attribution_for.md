---
title: Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback
url: http://arxiv.org/abs/2608.15530v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_04-56-03Z_WhySummariesTurnNeutral_PolicyAttributionforSentim.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why reinforcement learning with human feedback (RLHF) produces summaries that are overly neutral, losing emotional nuance. It introduces Policy Attribution to trace sentiment drift caused by reward model signals and KL penalties, showing a systematic bias toward low‑risk tokens across multiple datasets.

## Key Takeaways
- RLHF summaries achieve higher rewards but exhibit 30–40% lower sentiment variance compared with non‑RLHF baselines.  
- The drift is language‑independent and more pronounced in morphologically rich languages, indicating a universal bias toward safe token selection.  
- A sentiment‑aware regularization technique reduces this drift by 18–22% while preserving summary quality.

## Context
Sentiment drift undermines the goal of RLHF to produce expressive outputs, as neutral summaries may not reflect human preferences fully. Understanding the mechanism helps researchers design better alignment strategies that balance safety with expressive richness.

## Implications
For practitioners, this research offers a diagnostic tool and regularization method to mitigate unwanted neutrality in AI‑generated text. It signals a shift toward sentiment‑aware RLHF pipelines that preserve emotional nuance without sacrificing safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15530v1)
