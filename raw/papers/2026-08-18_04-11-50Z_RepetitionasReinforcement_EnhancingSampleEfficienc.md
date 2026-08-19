---
title: Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning
published: 2026-08-18T04:11:50Z
authors: Hoda Yamani, Yuning Xing, Koen van Rijnsoever, Bruce A. MacDonald, Henry Williams
url: http://arxiv.org/abs/2608.17347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning

## Abstract
Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample efficiency by immediately repeating action sequences from successful episodes during environment interaction. Unlike conventional approaches such as Experience Replay and Self-Imitation Learning (SIL), which passively reuse past experience during training updates, IER directly influences the data collection process. Upon identifying a high-reward episode, the agent repeats its action sequence for a fixed number of subsequent episodes, reinforcing valuable behaviors through renewed interaction with the environment. We integrate IER into state-of-the-art SAC and TD3 algorithms and evaluate its effectiveness on continuous-control benchmarks, including MuJoCo, the DeepMind Control Suite, and a real-world dynamic object translation task with a robotic manipulator. Experimental results demonstrate that this simple mechanism improves learning performance over standard and self-imitation-based baselines.

## Metadata
- **Published**: 2026-08-18T04:11:50Z
- **Authors**: Hoda Yamani, Yuning Xing, Koen van Rijnsoever, Bruce A. MacDonald, Henry Williams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17347v1)