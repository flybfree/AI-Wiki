---
title: Improving Diversity in LLM Short Story Generation
published: 2026-10-05T17:16:29Z
authors: Zahra Solati Dehkordi, Vasileios Lampos
url: http://arxiv.org/abs/2610.06729v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Diversity in LLM Short Story Generation

## Abstract
Large language models (LLMs) can generate accurate responses, but these are void of diversity. We attempt to address this for the task of creative short story generation. Drawing on established writing conventions and known LLM limitations, we target variation in genre, tone, style, and named entities. To promote diversity across these dimensions, we introduce DivLM, an LLM post-training framework consisting of two phases. First, we perform continued pre-training on a creative writing corpus and restore instruction-following capabilities using weight residuals. We then apply reinforcement learning with a custom, composite reward function that jointly maximizes diversity across the targeted narrative dimensions while maintaining response quality. Our empirical results on two LLM families show that DivLM increases diversity metrics by more than 9% on average compared to alternative approaches, while preserving instruction following, overall response quality, and similarity to human outputs.

## Metadata
- **Published**: 2026-10-05T17:16:29Z
- **Authors**: Zahra Solati Dehkordi, Vasileios Lampos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06729v1)