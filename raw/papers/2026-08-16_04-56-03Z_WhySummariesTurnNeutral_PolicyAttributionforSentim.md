---
title: Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback
published: 2026-08-16T04:56:03Z
authors: Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova, Grigori Sidorov
url: http://arxiv.org/abs/2608.15530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback

## Abstract
Reinforcement learning with human feedback (RLHF) aligns LLMs with human preferences, improving summarization fluency and safety, but causes sentiment drift: overly neutral summaries stripped of emotional nuance. We diagnose why RL acts as a sentiment neutralizer and present Policy Attribution, a framework using gradient and logit decomposition to trace drift to reward model (RM) signals and KL (Kullback-Leibler) penalty. Sentiment drift reflects a strategic bias toward "low-risk" tokens maximizing expected rewards under preference uncertainty (Stiennon et al., 2020; Gao, Schulman, and Hilton, 2023). On Reddit TL;DR and CNN/DailyMail, RLHF summaries get higher rewards but show 30-40% lower sentiment variance. Cross-lingual analysis across eight languages shows language-independent drift, with morphologically richer languages more suppressed (Krasitskii et al., 2026). We propose and validate a sentiment-aware regularization technique reducing drift by 18-22% without harming summary quality. The code and toolkit will be public.

## Metadata
- **Published**: 2026-08-16T04:56:03Z
- **Authors**: Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova, Grigori Sidorov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15530v1)