---
title: Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B
url: http://arxiv.org/abs/2608.22975v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_08-34-57Z_Budget_ConstrainedEmbodiedPerception_FourResourceW.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ASP, a training‑free wrapper that enforces four resource walls for embodied multimodal agents operating under a fixed token budget. It achieves much higher episodic retrieval accuracy than naive sampling while showing that query‑conditioned access is the decisive factor.

## Key Takeaways
- ASP reaches 75 to 94% episodic retrieval accuracy on SEW‑Bench under a 4,096-token budget, compared with 3 to 19% for equal‑budget query‑independent sampling.
- Budget reallocation outperforms simply quadrupling the sampling budget across all seven open models from 3B to 31B.
- Removing the compressive state or using verbatim‑only retrieval reduces performance, indicating that the full three‑component architecture is needed and that parameter count alone does not solve the problem.

## Context
Embodied agents face a critical bottleneck where each decision consumes tokens, limiting how much observation can be processed. This work provides a principled framework to allocate those limited tokens efficiently.

## Implications
For practitioners, ASP shows that designing efficient access mechanisms is more important than scaling model size or context length. It encourages research into structured state compression and iterative query‑conditioned inference rather than brute‑force expansion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22975v1)
