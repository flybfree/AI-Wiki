---
title: Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication
published: 2026-09-14T05:51:02Z
authors: Kushagra Agrawal, Yuming Feng, Man-Fai Leung
url: http://arxiv.org/abs/2609.15079v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication

## Abstract
Multi-agent LLM architectures, such as LangChain and AutoGen, largely assume English as the lingua franca for internal inter-agent communication, even when the end-user task is non-English. We fill this gap by evaluating a two-agent extraction-answer core, with an additional back-translation agent in the English-forced condition, across four typologically diverse languages (Hindi, Chinese, Spanish, Arabic; n = 300 per language) using the Aya-23-8B model. We compare a native-language pipeline to an English-forced one (which incorporates a final back-translation step from English to the user's language). We discover a statistically significant English-Forcing Tax (surviving a strict Bonferroni correction) that isolates the cost of English routing from general multi-agent orchestration overhead. Forcing inter-agent communication through English reduces Exact Match accuracy by 13.0 percentage points (Spanish) up to 30.6 percentage points (Hindi) compared to native-language multi-agent execution. Using chrF scores as a diagnostic measure of English-reference lexical overlap, we find that lower overlap is strongly associated with pipeline failure, consistent with translation loss being an important contributor to the observed performance drop. These findings suggest a compelling case for native-language routing in agent frameworks when the source and target languages are typologically distant, reducing a compounding translation tax.

## Metadata
- **Published**: 2026-09-14T05:51:02Z
- **Authors**: Kushagra Agrawal, Yuming Feng, Man-Fai Leung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15079v1)