---
title: Training Skills Like Parameters via Self-Supervised Semantic Diffusion
published: 2026-07-30T01:03:59Z
authors: Mo Li, Zixin Yin, Ting Cao, Yunxin Liu
url: http://arxiv.org/abs/2607.27557v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Skills Like Parameters via Self-Supervised Semantic Diffusion

## Abstract
While Large Language Models (LLMs) demonstrate remarkable general instruction-following capabilities, they often fall short of human experts in highly specialized, open-ended domains such as creative screenwriting. Prior approaches typically adopt post-training, yet both supervised fine-tuning and reinforcement learning require weight access that closed-source frontier models do not offer, and demand heavy compute. Moreover, what is learned is tied to a single checkpoint and cannot be inspected by humans. Recent advancements in agentic continual learning instead attempt to bridge this gap by accumulating external textual skills. However, these methods heavily rely on costly human expert annotations or unreliable LLM-as-a-judge feedback for reflection. To overcome this bottleneck, we propose a novel, unsupervised self-evolving agent framework inspired by the corruption-and-reconstruction paradigm of diffusion models. Instead of relying on explicit external scoring, we leverage existing high-quality human artifacts to construct self-supervised signals. Training then follows the familiar loop of neural network training, forward, loss, and backward, with the loss coming from contrasting the agent's reconstruction against the human original. What is updated is not model weights but an external library of textual skills. We evaluate our framework on the challenging task of short drama screenwriting. Experimental results demonstrate that our method enables the agent to autonomously extract and internalize highly generalizable skills, significantly enhancing its domain-specific generation capabilities. Furthermore, this self-contrastive reflection paradigm offers a scalable pathway for agents to teach themselves the production of complex, high-quality human artifacts, without requiring external supervision.

## Metadata
- **Published**: 2026-07-30T01:03:59Z
- **Authors**: Mo Li, Zixin Yin, Ting Cao, Yunxin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27557v1)