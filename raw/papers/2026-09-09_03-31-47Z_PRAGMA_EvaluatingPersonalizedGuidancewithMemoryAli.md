---
title: PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations
published: 2026-09-09T03:31:47Z
authors: Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung
url: http://arxiv.org/abs/2609.09664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations

## Abstract
Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time. As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computational overhead, making it difficult for models to consistently identify and utilize the most relevant information for the current request. These challenges have motivated memory systems that structure and retrieve user-specific information. In realistic interactions, users often seek practical guidance such as recommendations, planning, and decision support. Unlike factual recall tasks, personalized guidance requires models to integrate information across multiple past conversations and reason about changing user preferences and experiences. However, existing conversational memory evaluations mainly focus on retrieval and factual recall. To study this challenge, we introduce PRAGMA, a benchmark for evaluating personalized guidance in long-term conversations. PRGAMA contains curated longitudinal conversation histories, evidence annotations, and guidance scenarios grounded in evolving user contexts and incorrect user assumptions. Experiments across retrieval systems, memory systems, and long-context models reveal that current systems struggle both to recover the appropriate conversational evidence and to effectively use it for personalized guidance. Our results highlight the need for memory architectures that support robust conversational retrieval and memory-grounded reasoning beyond evidence recall.

## Metadata
- **Published**: 2026-09-09T03:31:47Z
- **Authors**: Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09664v1)