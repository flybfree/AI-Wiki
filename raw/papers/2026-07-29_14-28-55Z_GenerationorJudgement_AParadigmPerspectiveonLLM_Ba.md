---
title: Generation or Judgement? A Paradigm Perspective on LLM-Based Emotion-Cause Pair Extraction in Conversation
published: 2026-07-29T14:28:55Z
authors: Weijie Feng, Hongchuang Wang, Binbin Liu, Zhiyong Cheng
url: http://arxiv.org/abs/2607.26967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generation or Judgement? A Paradigm Perspective on LLM-Based Emotion-Cause Pair Extraction in Conversation

## Abstract
Emotion-cause pair extraction in conversation (ECPEC) identifies utterance pairs in which one utterance causes an emotion expressed in another. Recent LLM-based approaches formulate ECPEC at markedly different granularities, ranging from generating complete pair sets to judging individual candidate pairs. In this paper, we make the surprising observation that task formulation substantially affects performance, where pair-level judgement outperforms dialogue-level generation in all 18 controlled comparisons. We investigate the sources of this paradigm gap and find that many relations omitted by dialogue-level generation remain recognizable under explicit pair queries, under which the model recognizes 92.7%-98.1% of emotion-cause relations. This suggests that LLMs can recognize emotion-cause relations but struggle to discover and return complete pair sets. Pair-level judgement alleviates this burden, although its candidate rankings are more reliable than the binary decisions produced by a shared threshold. Based on this diagnosis, we introduce an auxiliary retriever that selectively re-examines ambiguous boundary cases, yielding consistent F1 improvements of 0.50-1.46 points across three datasets while maintaining an inference time of only 1.49x that of the baseline paradigm. These findings show that task decomposition and candidate scope are critical to effectively utilizing LLMs for ECPEC.

## Metadata
- **Published**: 2026-07-29T14:28:55Z
- **Authors**: Weijie Feng, Hongchuang Wang, Binbin Liu, Zhiyong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26967v1)