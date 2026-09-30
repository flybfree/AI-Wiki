---
title: Lost in Conversation or Lost in Translation? Diagnosing Multi-Turn Degradation in RAG
url: http://arxiv.org/abs/2609.36700v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-29_04-39-41Z_LostinConversationorLostinTranslation_DiagnosingMu.md
generated_at: 2026-09-29 20:43
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the performance gap between single-turn evaluations and real-world multi-turn interactions in Retrieval-Augmented Generation (RAG) systems. Through a large-scale simulation of 1.5 million conversations involving ten LLM assistants and eight retrieval systems, the authors demonstrate that conversational follow-ups significantly degrade system accuracy and reliability compared to fully specified queries. The study identifies two primary failure modes: "lost in translation," where user rephrasing harms retrieval quality, and "lost in conversation," where models struggle to synthesize evidence distributed across multiple turns.

## Key Takeaways
- RAG systems exhibit severe performance degradation during multi-turn interactions, with relative accuracy drops of up to 21% and unreliability increasing by 47%, revealing a critical mismatch between standard single-turn benchmarks and actual user behavior where queries evolve through follow-ups.
- The "lost in translation" failure mode occurs when conversational rephrasing distorts the retrieval query, causing the system to fetch irrelevant or insufficient evidence even when the information is available in the corpus, highlighting sensitivity to natural language variations in dialogue.
- The "lost in conversation" failure mode arises when retrieval succeeds but the LLM fails to effectively synthesize and integrate evidence distributed across multiple turns into a coherent response, indicating limitations in multi-turn reasoning and context aggregation capabilities.

## Context
Retrieval-augmented generation has become the industry standard for enhancing large language models with external knowledge, yet current evaluation protocols predominantly rely on static, single-turn

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36700v1)
