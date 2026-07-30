---
title: Improving Item Discoverability in e-Commerce Search via Related Intent Generation
url: http://arxiv.org/abs/2607.27172v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_17-46-35Z_ImprovingItemDiscoverabilityine_CommerceSearchviaR.md
generated_at: 2026-07-29 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a discovery-augmented search system that expands recall by generating implicit user intents. It uses a two-stage hybrid architecture: closed-weight LLMs for head queries and a fine-tuned small language model via LoRA for tail queries. The approach raises discovery coverage from ~60% to 80% while reducing cost by ~30%.

## Key Takeaways
- The system generates implicit user intents to expand candidate recall, improving semantic relevance beyond strict keyword matching.
- It uses a two-stage hybrid architecture with closed-weight LLMs for head queries and a LoRA-finetuned small language model for tail queries, achieving high quality at lower inference cost.
- Evaluation shows discovery coverage increased from 60% to 80% of query traffic while maintaining relevance, validated by human preference metrics and purchase analysis.

## Context
This work addresses the precision-recall tradeoff in e-commerce search where substitute or complementary items are crucial. By integrating generative intent modeling into recall expansion, it aligns with broader AI trends toward multimodal and context-aware retrieval systems that balance cost and quality.

## Implications
For practitioners, this method offers a scalable path to deploy discovery‑enhanced search at large scale without prohibitive compute expense. It also suggests that such systems can act as marketplace balancing tools, giving long‑tail products visibility and supporting diverse inventory strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27172v1)
