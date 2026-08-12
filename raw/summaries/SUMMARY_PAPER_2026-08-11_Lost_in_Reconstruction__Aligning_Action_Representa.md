---
title: Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models
url: http://arxiv.org/abs/2608.10484v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_04-57-17Z_LostinReconstruction_AligningActionRepresentations.md
generated_at: 2026-08-11 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the mismatch between verb semantics and how action representations are encoded in vision‑language‑action models. It demonstrates that reconstruction‑only tokenizers lose verb‑grounding information, leading to poor performance on BridgeV2. The authors introduce SALT, a tokenizer that aligns actions with language using an auxiliary objective.

## Key Takeaways
- Action trajectories contain verb‑grounding information that is erased by raw L1/L2 reconstruction losses.
- SALT adds a frozen vision‑language model to recover the episode instruction from quantized action latents, preserving semantic distinctions.
- Trained policies achieve 71.9% success on SimplerEnv compared with 42.7% (reconstruction) and 31.2% (FAST).

## Context
Vision‑language‑action systems aim to let robots understand language while performing tasks, but current tokenizers treat actions as mere numerical codes. This work shows that preserving linguistic structure can boost control quality.

## Implications
For robotics developers, aligning action representations with natural language may enable more reliable instruction following and reduce the need for costly retraining. The approach could be adapted to other multimodal agents seeking richer semantic grounding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10484v1)
