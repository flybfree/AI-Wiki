---
title: MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-Term Human-AI Conversation
published: 2026-08-25T07:54:12Z
authors: Ryuichi Sumida, Koji Inoue, Tatsuya Kawahara
url: http://arxiv.org/abs/2608.24189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-Term Human-AI Conversation

## Abstract
Memory systems for conversational LLMs are conventionally evaluated by direct, fact-seeking questions about prior dialogue (Direct QA): can the model recall fact X from a prior conversation? We tested whether higher Direct QA accuracy correlates with higher user satisfaction in a 4-month deployment (40 users, 1,872 sessions, 7 memory conditions). Existing-benchmark Direct QA varies from 19.7% to 70.1% across the 7 conditions, but satisfaction does not change. We hypothesize that existing benchmarks and user satisfaction are tracking different capabilities: benchmarks measure elicited retrieval (recall when asked), while conversation requires natural integration (detecting relevance and naturally weaving prior context into a response). To examine this, we introduce MemUse, a set of real user-cued memory moments drawn from the deployment, scored by an integration-aware judgment of the natural conversational response. Holding the model and context fixed, the same system that scores 78.8% on Direct QA references only 7.9% of those facts in conversation -- a 71-point gap. Within these moments, Natural Integration is associated with satisfaction, whereas Direct QA is not. We release the deployment corpus and MemUse together with all judgments and scoring prompts at https://github.com/ryuichi-sumida/memuse.

## Metadata
- **Published**: 2026-08-25T07:54:12Z
- **Authors**: Ryuichi Sumida, Koji Inoue, Tatsuya Kawahara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24189v1)