---
title: DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption
url: http://arxiv.org/abs/2608.16536v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_13-11-51Z_DSPrompt_DynamicSoftPromptDefenseAgainstM_RAGCorru.md
generated_at: 2026-08-17 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DSPrompt, a defense method that protects multimodal retrieval-augmented generation from adversarial poisoning attacks by reshaping encoder embeddings with few learnable soft prompts. It trains these prompts using an online min‑max scheme where a malicious attacker creates harmful documents while the defender pushes them out of top‑k rankings without harming benign evidence. Experiments show DSPrompt cuts attack success and poison retrieval rates substantially while keeping retrieval utility near lossless.

## Key Takeaways
- DSPrompt inserts soft prompts into each layer of visual and textual encoders, using a shallow-to-deep schedule that adapts to model capacity.
- The defense is trained under a dynamic min‑max scheme where an online attacker crafts adversarial documents and the defender updates to push them out of top‑k rankings while preserving benign diversity.
- Implementation adds fewer than 1% extra parameters and incurs no per‑query optimization cost, making it compatible with standard dense retrieval pipelines.

## Context
Adversarial attacks on M‑RAG systems are a growing concern as models rely on retrieved evidence to generate responses. Existing defenses often require runtime computation or assume fixed attack distributions, limiting their practicality. This work addresses those limitations by providing an offline, low‑overhead solution that can be integrated directly into existing retrieval pipelines.

## Implications
For practitioners deploying RAG systems, DSPrompt offers a scalable way to harden models against poisoning without sacrificing performance or adding significant latency. The approach could become a standard component in security‑aware AI deployment strategies across enterprise and research settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16536v1)
