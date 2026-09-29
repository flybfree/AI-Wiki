---
title: ProTTT: Learning to Learn Semantic User Memory with Test-Time Training
published: 2026-09-26T12:36:59Z
authors: Sejun Park, Hyoungjo Bhang, Hyein Jeong, Yohan Jo
url: http://arxiv.org/abs/2609.32564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProTTT: Learning to Learn Semantic User Memory with Test-Time Training

## Abstract
Personalization requires language models to capture user-specific knowledge from a growing user history. Existing context-based approaches incur increasing inference costs as user history accumulates and rely on separate retrieval or summarization stages, while parametric-based approaches often require reconstructing user representations when new user data is added. We introduce ProTTT, a profile-supervised meta-learning framework for learning semantic user memory. The memory construction starts from a shared initialization and is updated for each user through test-time training on user history, allowing it to evolve continuously as the history grows. However, since test-time training alone does not explicitly encourage the memory to capture semantic user knowledge necessary for personalization, we learn this shared initialization using textual user profiles as supervision, so that test-time training on user history captures semantic knowledge more effectively. ProTTT consistently outperforms both full history ICL and all parametric baselines across diverse benchmarks, while substantially reducing inference cost by compressing user history into a lightweight parameterized memory. Our analysis also shows that profile supervision is a reliable objective for learning semantic user knowledge and that the resulting memory can track and retain evolving user preferences, while remaining robust across different history sizes. Overall, we demonstrate the effectiveness of test-time training for personalization and establish ProTTT as a baseline for continuously evolving user memory.

## Metadata
- **Published**: 2026-09-26T12:36:59Z
- **Authors**: Sejun Park, Hyoungjo Bhang, Hyein Jeong, Yohan Jo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32564v1)