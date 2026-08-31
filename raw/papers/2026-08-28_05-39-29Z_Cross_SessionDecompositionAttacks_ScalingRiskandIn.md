---
title: Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense
published: 2026-08-28T05:39:29Z
authors: Disen Liao, Yihan Wang, Freda Shi, Yaoliang Yu
url: http://arxiv.org/abs/2608.27945v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense

## Abstract
Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model's excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \href{https://github.com/liaodisen/Cross-Session-Decomposition-Attacks}{our GitHub repository}.

## Metadata
- **Published**: 2026-08-28T05:39:29Z
- **Authors**: Disen Liao, Yihan Wang, Freda Shi, Yaoliang Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27945v1)