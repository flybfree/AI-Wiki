---
title: Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners
published: 2026-10-07T20:13:03Z
authors: Xilin Jiang, Shun Zhang, Tejas Jayashankar, Yinghao Aaron Li, Osama Hanna
url: http://arxiv.org/abs/2610.10868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners

## Abstract
We introduce Conversational Voice Aesthetic Model, a speech large language model for describing the voice aesthetics of real or synthetic speech responses in natural conversational contexts. Given a context and a response speech, CVAM describes salient moments that characterize the voice and predicts nine categorical attributes spanning gender, pitch, pacing, emotion, and delivery. The key challenge lies in perceptual fields such as emotion and delivery, which are inherently subjective and lack definitive ground truth. Therefore, we collect ~10 human annotations for each of 3k real and synthetic responses derived from the CANDOR corpus. CVAM is supervised finetuned on synthesized aesthetic descriptions and labels, then optimized with Group Relative Policy Optimization on human judgments. Experiments show that CVAM better agrees with human listeners than Gemini 3.1 Pro and open-source speech LLMs, and outperforms single-human-vs.-rest agreement. Together, we demonstrate the importance of grounding voice aesthetics in human perception and propose a principled framework for human alignment.

## Metadata
- **Published**: 2026-10-07T20:13:03Z
- **Authors**: Xilin Jiang, Shun Zhang, Tejas Jayashankar, Yinghao Aaron Li, Osama Hanna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10868v1)