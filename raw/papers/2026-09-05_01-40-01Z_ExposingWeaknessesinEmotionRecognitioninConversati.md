---
title: Exposing Weaknesses in Emotion Recognition in Conversations
published: 2026-09-05T01:40:01Z
authors: Amir Ben Khalifa, Fanny Bezancon, Amine Trabelsi, Bessam Abdulrazak
url: http://arxiv.org/abs/2609.05806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exposing Weaknesses in Emotion Recognition in Conversations

## Abstract
Emotion Recognition in Conversations (ERC) aims to identify speakers' emotions in multi-turn dialogue. Accurate emotion recognition can support a wide range of applications, including empathetic conversational agents, mental health support, and educational technologies. While many recent approaches rely on task-specific fine-tuning, such models may exploit dataset-specific cues. A central yet rarely questioned assumption in ERC is that each utterance can be assigned a single unambiguous emotion label. To investigate this assumption, we study ERC using Large Language Models (LLMs) in a zero-shot setting while incorporating preceding conversational turns as context. We show that aggregate metrics mask systematic failures. Errors concentrate around utterances containing negations, exclamations, and interjections. This pattern is consistent across all evaluated models, suggesting limitations in the benchmarks rather than model-specific weaknesses. A controlled re-annotation study involving four human annotators supports this finding: strong agreement is observed in only 35 percent of cases, with neutral utterances dominating high-agreement instances, while many emotional categories fall into low-agreement regimes. These findings suggest that many apparent model errors reflect genuine annotation ambiguity rather than poor emotion understanding. Standard single-label evaluation is therefore insufficient. To address this limitation, we introduce an LLM-as-Judge framework that evaluates each emotion independently according to its plausibility in the conversational context rather than enforcing a single-label decision.

## Metadata
- **Published**: 2026-09-05T01:40:01Z
- **Authors**: Amir Ben Khalifa, Fanny Bezancon, Amine Trabelsi, Bessam Abdulrazak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05806v1)