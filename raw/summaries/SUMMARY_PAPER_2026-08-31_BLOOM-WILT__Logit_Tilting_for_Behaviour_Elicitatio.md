---
title: BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing
url: http://arxiv.org/abs/2608.31105v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_17-10-59Z_BLOOM_WILT_LogitTiltingforBehaviourElicitationinAu.md
generated_at: 2026-08-31 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
BLOOM-WILT introduces a logit‑tilting technique that enables automated auditors to elicit rare, multi‑turn behaviours from language models without retraining or accessing the model’s full context. The method improves over existing baseline auditing by achieving 30 out of 32 settings where it outperforms the prior approach and raises behaviour presence to 100 % for self‑harm encouragement in Qwen3.5‑4B, surpassing all ported elicitation methods at matched compute.

## Key Takeaways
- WILT’s auditor revises its conversational strategy across rounds, learning from previously scored interactions to guide the next turn.  
- The model’s own decoding is reweighted using a conditioning prompt, biasing sampling toward behaviour‑relevant outputs while keeping other equally probable generations at baseline probabilities.  
- In evaluation across four target models and eight behaviours, WILT beats the baseline in 30 of 32 settings and overturns previous safety rankings.

## Context
Automated model auditing aims to detect harmful or undesirable outputs cheaply and at scale, but typical methods are sample‑inefficient because they cannot exploit the model’s own generative dynamics. BLOOM-WILT addresses this by integrating logit tilting directly into the inference pipeline, allowing the system to steer sampling without external training data.

## Implications
For practitioners, BLOOM-WILT offers a more reliable way to verify safety claims of deployed models, reducing false negatives that could lead to real‑world harm. The approach sets a new benchmark for automated auditing, encouraging the industry to adopt logit‑tilting techniques as standard practice in model evaluation and deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.31105v1)
