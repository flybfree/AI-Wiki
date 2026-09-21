---
title: Talk to Me, Jarvis: An Open-Source Edge-Deployable Voice Assistant Framework for Autonomous Racecars
published: 2026-09-17T21:51:03Z
authors: Daniel Henel, Frederik Werner, Alexander Langmann, Johannes Betz
url: http://arxiv.org/abs/2609.21109v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Talk to Me, Jarvis: An Open-Source Edge-Deployable Voice Assistant Framework for Autonomous Racecars

## Abstract
Recent advances in large language models have improved their effectiveness as back-end components for voice assistants, particularly in intent understanding and context-aware input classification. However, online-hosted models introduce network dependency and variable inference latency, limiting their suitability for time-critical autonomous driving applications. In this work, we address these issues by developing Jarvis, an offline voice assistant for high-level behavioral commands of autonomous vehicles. Its architecture integrates speech recognition and synthesis with natural language command classification into a lightweight, local framework. Jarvis core component is a text-to-command classifier, built using a domain-specific fine-tuning of the Mistral 7B model, demonstrating low-latency inference. Our experimental evaluation demonstrates that our solution outperforms larger online-hosted models, achieving 97.63 % intent recognition accuracy with an average processing latency of 1.39 s, making it well-suited for operations requiring quick response times. To support further research and fine-tuning, we provide an open-source implementation.

## Metadata
- **Published**: 2026-09-17T21:51:03Z
- **Authors**: Daniel Henel, Frederik Werner, Alexander Langmann, Johannes Betz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21109v1)