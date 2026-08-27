---
title: Beam Search, Self-Consistency, and the Limits of Inference-Time Scaling for Grammar-Constrained Text-to-SQL in Small Language Models
url: http://arxiv.org/abs/2608.25761v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-07-06Z_BeamSearch_Self_Consistency_andtheLimitsofInferenc.md
generated_at: 2026-08-26 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the trade‑off between model size and inference compute changes when output generation is constrained by a strict grammar, using text‑to‑SQL as an example. Experiments on the Spider benchmark with Qwen2.5 models show that increasing inference compute does not consistently improve accuracy beyond what larger models already achieve.

## Key Takeaways
- Both beam search and sample+vote increase accuracy, especially for smaller models (0.5B–7B parameters).  
- The “model size vs. inference compute” trade‑off is not beneficial; larger models typically outperform higher‑compute runs on the same model size.  
- Beam search outperforms sample+vote when inference budget is matched, contradicting results from unconstrained settings.

## Context
The study highlights a nuance in large language model deployment: constrained generation can alter the efficiency of scaling strategies compared to unrestricted ones. It underscores that performance gains are not always linear with compute and may be better achieved by expanding model capacity.

## Implications
For practitioners, this suggests prioritizing larger base models over costly inference tricks when strict grammatical constraints exist. The findings guide resource allocation in real‑world text‑to‑SQL systems where latency and accuracy must balance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25761v1)
