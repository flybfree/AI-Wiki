---
title: Rushes: A Human Preference Dataset for Pluralistic Alignment
url: http://arxiv.org/abs/2607.20767v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_22-32-34Z_Rushes_AHumanPreferenceDatasetforPluralisticAlignm.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Rushes, a dataset that records how users interact with AI-generated branching narratives by selecting among small candidate choices at each decision point. It contains 44,226 decision events from 8,167 users across six games and shows that user choices follow structured patterns rather than random behavior.

## Key Takeaways
- User choice entropy is low compared to a uniform baseline indicating non‑random engagement.
- Classical SVD personalization captures about 37.7% of the signal while frontier LLMs such as GPT‑5 achieve only 34.23%, falling below the popularity baseline at 36.4%.
- The Engagement Gap reveals that single, population‑level objectives like those in modern RLHF cannot capture heterogeneous, context‑dependent signals.

## Context
Rushes addresses a gap between human preference modeling and large language model behavior in interactive storytelling. By providing a richly detailed dataset of sequential choices, it enables researchers to evaluate whether models can learn individualized engagement rather than defaulting to majority trends.

## Implications
For practitioners, Rushes suggests that improving personalization will require methods beyond simple popularity baselines, encouraging research into context‑aware alignment and multi‑level objectives. The release of code and data supports a shift toward more nuanced evaluation of generative systems in narrative contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20767v1)
