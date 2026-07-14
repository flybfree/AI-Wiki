---
title: "Summary: Sub-Billion, Super-Frontier: Small Language Models Rival Zero-Shot Frontier LLMs on General and Literary Relation Extraction"
url: http://arxiv.org/abs/2606.22606v1
type: paper-summary
date: 2026-06-22
source_paper: 2026-06-21_17-24-31Z_Sub_Billion_Super_Frontier_SmallLanguageModelsRiva.md
generated_at: 2026-06-22 22:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-22 Sub-Billion  Super-Frontier  Small Language Models

## Summary
The paper investigates how small language models can rival zero-shot frontier LLMs on relation extraction tasks across general and literary domains. It compares five models ranging from 360M to 3B parameters against state-of-the-art systems and a RoBERTa baseline, finding that task-specific adaptation yields superior performance despite smaller size. The study also notes that domain-adaptive pretraining offers little practical benefit over supervised fine‑tuning.

## Key Takeaways
- the best sub‑billion model Qwen2.5‑0.5B fine‑tuned on pooled general‑domain data achieves a 0.83 micro‑F1, outperforming GPT‑5.4 (0.69) and Claude Sonnet 4.6 (0.66) evaluated zero‑shot
- an in‑domain RoBERTa baseline exceeds both frontier models, indicating that the gain stems from task adaptation rather than generative decoding
- a targeted domain‑adaptive pretraining case study yields no practically meaningful gain over supervised fine‑tuning

## Context
This work highlights the efficiency of task‑specific model tuning, suggesting that smaller models can be deployed locally without sacrificing performance. The paper underscores the importance of task‑specific data for small models and aligns with trends toward privacy‑preserving AI and edge computing.

## Implications
Practitioners can adopt compact, fine‑tuned models for relation extraction, reducing reliance on proprietary APIs and lowering computational costs. This approach encourages a shift toward open‑source, locally run solutions that maintain accuracy while respecting privacy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.22606v1)
