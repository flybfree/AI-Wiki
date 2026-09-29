---
title: On Device Agentic Operation Caches -- Classifier-Centric NL-to-Action Generation
published: 2026-09-27T03:13:10Z
authors: Moghis Fereidouni, Anthony Arnold, Sumit Gulwani, Mark Marron, A. B. Siddique
url: http://arxiv.org/abs/2609.33141v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Device Agentic Operation Caches -- Classifier-Centric NL-to-Action Generation

## Abstract
Agentic AI is increasingly being embedded in software applications to provide natural language interfaces to features and functionality. In most cases these agents are powered by enterprise (100+ billion parameter) or frontier class large language models that require substantial computational resources run and depend on cloud hosted inference to handle the task of transforming natural language inputs into actionable software operations. This reliance on cloud-hosted inference introduces substantial network latency on top of LLM inference times, creates data privacy concerns, and, given the costs of running these models, can rapidly escalate expenses associated with supporting agentic features.   This paper introduces a novel means of converting the NL-to-Action problem from a generative one into a classification-centric formulation via on-device operation caches. These caches allow an agentic system to handle frequently occurring classes of actions completely on-device -- reducing latency, enhancing privacy, and lowering operational costs. We show that for a classic NL-to-Formula task, generating Excel Formula in response to user requests, this approach reduces total inference cost by 56% when compared to cloud-only model-routing based inference and, on cache hits, reduces the latency to response latency by 5x.

## Metadata
- **Published**: 2026-09-27T03:13:10Z
- **Authors**: Moghis Fereidouni, Anthony Arnold, Sumit Gulwani, Mark Marron, A. B. Siddique
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33141v1)