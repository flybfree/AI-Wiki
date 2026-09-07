---
title: Generating Constructive Feedback on Stories via Reinforcement Learning
published: 2026-09-04T07:26:23Z
authors: Maja Stahl, Timon Ziegenbein, Henning Wachsmuth
url: http://arxiv.org/abs/2609.04824v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generating Constructive Feedback on Stories via Reinforcement Learning

## Abstract
Constructive feedback is crucial for creative writers to refine their storytelling abilities. Since receiving feedback from human experts is often costly and time-intensive, large language models (LLMs) offer a scalable and efficient alternative as automatic writing assistants. Despite their potential, research indicates that LLM-generated feedback is often generic, lacks actionability, and fails to identify which writing issue is most critical. To address these limitations, we present a reinforcement learning approach that steers LLMs to generate constructive feedback without the need for ground-truth feedback. We train our model using group relative policy optimization (GRPO) with a novel multi-component reward function aiming at constructiveness: it prioritizes feedback that is uniquely tailored to the story, helps to improve story quality, and addresses the most critical writing issue. In automatic and human evaluation across three story corpora, our approach outperforms state-of-the-art LLMs (including Gemini) and competitive baselines. We find that providing actionable suggestions is the main driver of feedback constructiveness.

## Metadata
- **Published**: 2026-09-04T07:26:23Z
- **Authors**: Maja Stahl, Timon Ziegenbein, Henning Wachsmuth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04824v1)