---
title: LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO
url: http://arxiv.org/abs/2608.29357v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_16-33-22Z_LiteSearch_VL_SmallMultimodalSearchAgentsviaTrajec.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper LiteSearch-VL explores how to compress multimodal search agent trajectories into smaller models using lightweight LoRA adapters and synthetic DPO preferences. It demonstrates that a 2B model can achieve comparable performance to a larger 4B base on several VQA benchmarks by transferring behavioral patterns rather than raw accuracy.

## Key Takeaways
- The distilled 2B model improves macro Pass@1 from near zero to about 28% using only released OpenSearch-VL trajectories, LoRA adapters and synthetic step-level DPO targeting five failure modes.  
- Synthetic preference learning refines behavior but does not cause a phase transition; the best configuration reaches 30.8% macro Pass@1 matching the off‑the‑shelf 4B baseline.  
- Search depth is limited: extra turns convert abstentions into wrong_entity errors, indicating answer verification is the next bottleneck.

## Context
Current multimodal agents require either costly proprietary models or large open backbones trained with extensive RL data. This work shows that smaller models can inherit complex agentic behavior from released trajectories, reducing compute and cost while maintaining useful performance.

## Implications
For practitioners, LiteSearch-VL offers a pathway to deploy efficient, high‑performing multimodal agents on limited hardware without sacrificing core functionality. It also highlights the importance of evaluating search depth versus answer correctness in small models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29357v1)
