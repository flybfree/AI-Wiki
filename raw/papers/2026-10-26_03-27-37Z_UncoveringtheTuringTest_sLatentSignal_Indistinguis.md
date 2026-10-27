---
title: Uncovering the Turing Test's Latent Signal: Indistinguishability as a Reward
published: 2026-10-26T03:27:37Z
authors: Emanuele Rimoldi, Riccardo Neumarker, Tomaso Poggio, Daniel Mitropolsky
url: http://arxiv.org/abs/2610.34781v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncovering the Turing Test's Latent Signal: Indistinguishability as a Reward

## Abstract
Can a model learn by trying to fool another model? We show that it can. Inspired by the Turing Test and its recent generalization to arbitrary distinguishers, we introduce a domain-based teacher-Turing-Test, in which a stronger teacher model serves as both the target of imitation and the distinguisher, and a weaker student model is trained to make the teacher attribute responses to itself. We use this self-attribution (or fooling) probability as a reinforcement learning reward, without ever providing the student ground-truth answers, nor requiring the teacher to generate responses. We test our approach independently in four domains with verifiable answers: CommonsenseQA (reasoning), GSM8K (mathematics), KodCode (programming), and Spider (SQL), training a Qwen2.5-1.5B student/imitator model using DeepSeek V4 Flash as teacher/distinguisher. Beyond improving at passing the Turing Test, the student improves on independent, held-out evaluations in all domains and runs. To probe why being mistaken for the teacher can improve capability, our analyses reveal that self-attribution is associated with correctness -- substantially more than formatting changes -- and that it rewards partial correctness. Our results demonstrate a new, simple teacher-student training paradigm with a private and/or high-cost teacher. They also suggest that indistinguishability need not merely measure behavior -- it can also be a mechanism for learning.

## Metadata
- **Published**: 2026-10-26T03:27:37Z
- **Authors**: Emanuele Rimoldi, Riccardo Neumarker, Tomaso Poggio, Daniel Mitropolsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34781v1)