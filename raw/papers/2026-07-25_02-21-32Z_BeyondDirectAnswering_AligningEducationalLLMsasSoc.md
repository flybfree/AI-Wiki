---
title: Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning
published: 2026-07-25T02:21:32Z
authors: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
url: http://arxiv.org/abs/2607.22996v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning

## Abstract
Large language models (LLMs) deployed in educational settings often behave as direct answerers: they disclose target concepts in the opening turn instead of guiding students through progressive inquiry, as Socratic pedagogy prescribes. We present HeuristicEdu, a two-phase pipeline that aligns Qwen2.5-7B toward Socratic tutoring via supervised warm-up and Group Relative Policy Optimization (GRPO). Training uses SocraticEdu, 797 multi-turn Chinese children's science dialogues reconstructed from a live platform, with a heuristic reward over cognitive depth (R_cog), curiosity engagement (R_eng), and directness (R_dir), together with a K_query correction for student-introduced terms. We introduce Scaffolding Effectiveness (SE) and Conversation Depth (CD) to evaluate outcomes beyond surface fluency. On 30 held-out questions, the best GRPO variant improves SE from 30.0% to 63.3% and lowers keyword leakage from 30.0% to 13.3%. Notably, this best variant omits the directness penalty during optimization, suggesting that explicit anti-leakage terms can conflict with gradient-based behavioral alignment. An unaligned Qwen-72B baseline reaches 0% SE and 96.7% leakage, showing that scale alone does not induce Socratic behavior.

## Metadata
- **Published**: 2026-07-25T02:21:32Z
- **Authors**: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22996v1)