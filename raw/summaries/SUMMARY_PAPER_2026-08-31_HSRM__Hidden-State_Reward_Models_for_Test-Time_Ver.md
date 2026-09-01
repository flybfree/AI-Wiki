---
title: HSRM: Hidden-State Reward Models for Test-Time Verification
url: http://arxiv.org/abs/2608.30841v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_14-12-19Z_HSRM_Hidden_StateRewardModelsforTest_TimeVerificat.md
generated_at: 2026-08-31 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HSRM, a hidden-state reward model that verifies candidate solutions by reading the generator’s internal representations at reasoning-step boundaries instead of re‑processing text. Trained from self‑generated trajectories with outcome labels, it uses only about 2 million parameters and matches or beats a 55 million‑parameter text‑only energy verifier on most settings.

## Key Takeaways
- HSRM extracts hidden states at reasoning-step boundaries and ranks candidates using a small Transformer encoder, avoiding the need to re‑read each solution.  
- The model is trained from self‑generated trajectories with outcome labels, requiring no human‑written process supervision or large pretrained verifier.  
- Across four mathematical reasoning benchmarks it matches or outperforms a 55 million‑parameter text‑only energy verifier in 15 of 16 generator–dataset settings while using only about 2 million parameters.

## Context
Current test‑time verification relies on costly text re‑processing, which limits the efficiency of large language model inference. HSRM addresses this bottleneck by leveraging representations already computed during generation, offering a lighter alternative that can be integrated without additional compute overhead.

## Implications
For practitioners, HSRM enables faster, cheaper verification pipelines that improve system reliability without sacrificing performance. In industry, this could reduce latency in real‑time reasoning applications and lower infrastructure costs for deploying robust LLM services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30841v1)
