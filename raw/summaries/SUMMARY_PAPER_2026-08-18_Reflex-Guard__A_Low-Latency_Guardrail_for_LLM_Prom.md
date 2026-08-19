---
title: Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings
url: http://arxiv.org/abs/2608.17556v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_09-19-22Z_Reflex_Guard_ALow_LatencyGuardrailforLLMPromptSafe.md
generated_at: 2026-08-18 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents Reflex-Guard, a lightweight local guardrail that filters LLM prompts with sub‑100 ms latency using dense semantic embeddings and fast binary classifiers. It achieves 95.9% recall on harmful prompts while being faster than existing solutions such as Llama Guard 2 (255 ms) and SafeDecoding (723 ms).  

## Key Takeaways
- Reflex-Guard processes prompts locally, eliminating the 250‑900 ms delay caused by external moderation APIs.  
- The system detects all GCG suffix attacks and Base64‑encoded prompts at the default threshold, demonstrating robust coverage of common jailbreak techniques.  
- Residual Attack DrAttack requires a lower probability threshold (0.03) because its structured format creates a distinct embedding distribution.  

## Context
Current LLM safety systems often rely on cloud‑based APIs that introduce latency and privacy risks for real‑time applications. This work addresses the need for fast, on‑device filtering to meet sub‑100 ms response requirements while preserving user data.  

## Implications
For developers deploying LLMs in interactive settings, Reflex-Guard offers a practical path to safe interactions without sacrificing speed or privacy. Its high recall and low latency can be integrated directly into system pipelines, reducing reliance on external moderation services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17556v1)
