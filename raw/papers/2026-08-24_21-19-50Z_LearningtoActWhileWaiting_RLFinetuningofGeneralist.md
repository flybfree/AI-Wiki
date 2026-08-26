---
title: Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency
published: 2026-08-24T21:19:50Z
authors: Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine
url: http://arxiv.org/abs/2608.23831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency

## Abstract
While reinforcement learning (RL) allows generalist robot policies to continually improve during deployment, the large model size of modern generalist policies, such as VLAs, poses a fundamental obstacle to effective RL improvement. In particular, their severe inference latency---which can lead to pauses or jerky movements---can alter the effective environment dynamics and, if not correctly accounted for, break the Markov assumption that RL relies on, causing standard RL algorithms to fail completely. In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays.   Our framework builds on asynchronous inference approaches, which interleave action generation with execution to hide latency, and addresses its incompatibility with RL by providing a low-latency RL policy design that maximizes reactivity within the inference window through two contributions: state augmentations that restore near-Markovian structure by incorporating committed actions and a mid-inference observation.   We evaluate our approach across simulated and real-world manipulation tasks, and find that it enables effective finetuning under inference delays where standard RL fails entirely, even matching or exceeding the performance of standard RL in idealized no-latency settings.

## Metadata
- **Published**: 2026-08-24T21:19:50Z
- **Authors**: Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23831v1)