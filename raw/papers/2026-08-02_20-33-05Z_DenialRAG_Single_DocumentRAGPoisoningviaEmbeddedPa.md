---
title: DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial
published: 2026-08-02T20:33:05Z
authors: Abay Zhurekbay, Tao Liu, Fan Li
url: http://arxiv.org/abs/2608.02678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial

## Abstract
Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning: an attacker who inserts a crafted document into the retrieval corpus can steer the underlying large language model (LLM) toward an attacker-chosen wrong answer. Prior single-document attacks typically avoid explicitly naming and refuting the correct answer inside the poisoned passage. In this paper, we examine a complementary design and propose \emph{DenialRAG}, a single-document poisoning attack that explicitly names the correct answer, denies it, and presents an attacker-controlled explanation for favoring the wrong answer. By placing both the correct answer and the corresponding poisoned answer inside the same retrieved passage, DenialRAG embeds the conflict directly into the context seen by the generator.   We evaluate DenialRAG against four published single-document poisoning attacks across three open-domain question-answering datasets, eight target LLMs from four vendors, and five inference-time defenses. The results show that attack effectiveness is strongly model-dependent: DenialRAG achieves the highest attack success rate (ASR) on all three Mistral-7B datasets and remains effective on several other target LLMs, while other attacks dominate in some model regimes. Defense results show meaningful ASR reductions but non-uniform protection, with each defense leaving residual ASR in some settings. Component-level and cross-model analyses further identify the embedded denial as the most influential tested component and show that different poisoning mechanisms lose effectiveness at different rates across model groups. Together, these results show that RAG poisoning risk cannot be fully characterized by a single attack family or a single target model.

## Metadata
- **Published**: 2026-08-02T20:33:05Z
- **Authors**: Abay Zhurekbay, Tao Liu, Fan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02678v1)