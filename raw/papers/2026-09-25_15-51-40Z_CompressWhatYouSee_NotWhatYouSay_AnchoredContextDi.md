---
title: Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents
published: 2026-09-25T15:51:40Z
authors: Zhensheng Zou, Guoqing Wang, Dan Hao
url: http://arxiv.org/abs/2609.31430v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents

## Abstract
Tool observations dominate the context of software-engineering agents, making long interaction histories costly to maintain. Existing context compression methods can discard information needed by later actions, while adapting agents to soft-token representations can compromise their original behavior. To reduce context while preserving action-critical information and agent behavior, we combine Latent Observations, Hard Actions (LOHA), a context layout that separates compressed history from text needed for exact reference, with Anchored Context Distillation (ACD), a training method that enables latent reading while constraining behavioral drift. LOHA compresses older tool observations into soft tokens while retaining the agent's own turns and the last K observations in text, providing compact access to historical information and exact access to recent content. To enable the agent to use this representation, ACD distills the base model's full-text predictions into the latent view while anchoring its behavior on plain-text inputs to the same base model. On SWE-bench Verified, K=3 reduces context per call by 43% for Qwen3-4B and 57% for SWE-Master-4B-RL, with resolve rates of 12.1% and 21.8% versus 14.5% and 27.5% for their uncompressed bases. A single-run recency sweep reaches 14.4% and 23.0% at K=8, with larger windows generally favoring task performance over compression. Under a 32K-token limit, Qwen3 with K=3 resolves 21.1% of a 199-instance subset versus 11.1% for the same adapted agent using full text. In concurrent single-GPU serving, it achieves 1.9 times that full-text agent's instance throughput.

## Metadata
- **Published**: 2026-09-25T15:51:40Z
- **Authors**: Zhensheng Zou, Guoqing Wang, Dan Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31430v1)