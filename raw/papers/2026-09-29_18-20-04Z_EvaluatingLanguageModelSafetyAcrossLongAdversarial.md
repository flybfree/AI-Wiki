---
title: Evaluating Language Model Safety Across Long Adversarial Conversations
published: 2026-09-29T18:20:04Z
authors: Parisa Salmani, Peter R. Lewis
url: http://arxiv.org/abs/2609.38357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Language Model Safety Across Long Adversarial Conversations

## Abstract
Conversational safety evaluations often test language models with a single harmful prompt, even though real-world systems interact with users through long, adaptive conversations. This study examines whether models continue to respond safely when an adversarial user persists across multiple turns. We evaluate three open-weight, instruction-tuned models on two harmful prompts across different conversation lengths and random seeds. In each setting, a second language model acts as a persistent adversarial user, while a safety classifier labels every response as safe or unsafe. Across all model-prompt combinations, first-turn safe-response rates ranged from 85% to 100%. By depth 11, they dropped to 38-61%, and by depth 101, to 15-44%. This decline appeared across models and continued well beyond the short interactions typically used in multi-turn safety evaluations. These results provide proof-of-concept evidence that strong single-turn safety does not necessarily persist during sustained adversarial interaction. They highlight the need for long-horizon evaluations and conversation-level safeguards that account for risk accumulating across turns.

## Metadata
- **Published**: 2026-09-29T18:20:04Z
- **Authors**: Parisa Salmani, Peter R. Lewis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38357v1)