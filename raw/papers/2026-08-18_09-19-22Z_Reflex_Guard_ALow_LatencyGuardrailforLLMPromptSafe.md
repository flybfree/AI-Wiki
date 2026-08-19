---
title: Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings
published: 2026-08-18T09:19:22Z
authors: Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon, Abu-fuad Ahmad, Thi Hong Tran
url: http://arxiv.org/abs/2608.17556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings

## Abstract
Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderation endpoints raises significant data privacy concerns. This paper introduces Reflex-Guard, a lightweight guardrail that runs locally. It uses jailbreak-aware preprocessing, compact sentence-transformer embeddings, and seven fast binary classifiers. Together, these components enable high-accuracy prompt safety filtering with much lower latency than existing solutions. Through systematic evaluation on a strategically balanced dataset of 30,568 samples drawn from five complementary sources, we demonstrate that Reflex-Guard achieves 95.9% recall on harmful prompts at 37.6 ms end-to-end latency. It is faster than existing baselines, including Llama Guard 2 at 255 ms and SafeDecoding at 723 ms. It can detect 100% of GCG suffix attacks and Base64-encoded prompts using the default threshold. However, DrAttack structured prompts required lowering the threshold to 0.03 for optimal detection, as they produced a distinct probability distribution. Reflex-Guard achieves Reflex Efficiency Score (RES) scores up to 16.79, significantly outperforming Llama Guard 2 (11.90) and SafeDecoding (9.80). This analysis offers practical deployment advice and shows that different attack types occupy distinct regions in the embedding probability space.

## Metadata
- **Published**: 2026-08-18T09:19:22Z
- **Authors**: Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon, Abu-fuad Ahmad, Thi Hong Tran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17556v1)