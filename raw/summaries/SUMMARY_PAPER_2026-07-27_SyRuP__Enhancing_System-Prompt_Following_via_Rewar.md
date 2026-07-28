---
title: SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding
url: http://arxiv.org/abs/2607.23991v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_04-39-13Z_SyRuP_EnhancingSystem_PromptFollowingviaReward_Gui.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SyRuP, a decoding‑time framework that improves system‑prompt adherence without retraining the base language model. By training a cross‑attention reward head on preference pairs conditioned on the system prompt, SyRuP generates token‑level adherence scores and reranks the model’s top‑k outputs at inference time, achieving consistent gains over prompting and decoding‑time baselines with modest overhead.

## Key Takeaways
- SyRuP trains a lightweight cross‑attention reward head that uses system‑prompt–conditioned preference pairs to produce token‑level adherence scores.  
- At inference, the model’s top‑k candidates are reranked by combining base logits with the learned reward signal and an optional contrastive term for system‑induced logit shifts.  
- Experiments show SyRuP outperforms prompting and decoding‑time baselines on system‑prompt following benchmarks while keeping the base LM frozen.

## Context
The growing reliance on system prompts to steer LLM behavior highlights a gap: models often follow these instructions implicitly, which can falter for complex or compositional tasks. Existing solutions typically demand model fine‑tuning or post‑hoc reranking, increasing computational cost and deployment complexity. SyRuP addresses this by embedding guidance directly into the decoding process.

## Implications
For practitioners, SyRuP offers a practical way to enforce system prompts at inference time without retraining heavy models, reducing latency and resource usage. In industry applications where reliable instruction following is critical—such as chatbots or automated assistants—the method can improve consistency and safety while preserving model efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23991v1)
