---
title: Scalable Context Orchestration for Serving LLMs Over Voice
published: 2026-09-03T09:27:00Z
authors: Linyi Jiang, Silvery D. Fu, Yifei Zhu
url: http://arxiv.org/abs/2609.04288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable Context Orchestration for Serving LLMs Over Voice

## Abstract
Voice AI applications are gaining popularity as advances in large language models (LLMs) enable more natural and accessible spoken interactions. Serving these applications requires accounting not only for what users say, but also for how they speak (e.g., speaking rate) and the conditions under which their audio is captured and transmitted (e.g., background noise and packet loss). However, existing LLM systems represent conversation context as a flat, growing sequence of messages, leaving voice-specific context implicit in the audio. As a result, they can generate responses that are poorly aligned with user preferences, degrade interaction quality under adverse environmental conditions, and incur high costs over long voice sessions.   We present llmovoice, a context-management middleware that explicitly models voice context and orchestrates its use. At each turn, llmovoice constructs a bounded voice context from the current user input, relevant interaction history, and explicit paralinguistic and environmental states. It then uses the serving LLM to reason over this context and generate runtime directives that guide how the system responds. We evaluate llmovoice on real-world voice applications and benchmarks. It reduces speaking-rate alignment error by 52.4%, lowers the false-interruption rate from 46.0% to 0.9% under packet loss, and reduces model usage cost by 79.2%. For long sessions, llmovoice reduces per-turn cost by up to 24.9 times while retaining up to 98.7% of baseline answer quality.

## Metadata
- **Published**: 2026-09-03T09:27:00Z
- **Authors**: Linyi Jiang, Silvery D. Fu, Yifei Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04288v1)