---
title: PICTURE: Enhancing Theory-of-Mind in Large Language Models by Revealing, Not Hiding, Characters' Lack of Knowledge
published: 2026-08-03T02:07:51Z
authors: Eojin Jeon, SangKeun Lee
url: http://arxiv.org/abs/2608.01598v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PICTURE: Enhancing Theory-of-Mind in Large Language Models by Revealing, Not Hiding, Characters' Lack of Knowledge

## Abstract
Simulating human-like Theory of Mind (ToM) has been a longstanding problem in natural language processing (NLP). To address this, existing works introduce a reasoning step of event hiding (a.k.a. perspective-taking), where events unknown to a character are removed before question answering. However, resorting to event hiding for ToM reasoning presents a performance degradation issue due to the strict output format constraints involved in event hiding. To mitigate this issue, we propose generating perspective-taking outputs as free-form explanations without event hiding, but this poses a notable yet underexplored challenge: LLMs need to inhibit responses to events unknown to characters, because the absence of event hiding exposes LLMs to these events throughout reasoning. To address this challenge, we hypothesize and empirically verify that LLMs can achieve such inhibition if a character's lack of knowledge about events is made explicit during reasoning. Based on this finding, we introduce PICTURE, a new prompting method that enables LLMs to generate a character's lack of knowledge within free-form Chain-of-Thought (CoT). Experimental results show that PICTURE outperforms existing prompting methods by an average of 7.3% on false-belief tasks.

## Metadata
- **Published**: 2026-08-03T02:07:51Z
- **Authors**: Eojin Jeon, SangKeun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01598v1)