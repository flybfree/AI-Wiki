---
title: Cybersecurity Detection Classification with Reasoning-enabled Language Models
published: 2026-07-30T16:22:13Z
authors: Amol Khanna, Manu Nandan, Cristian Viorel Popa, Joan Pujol-Roig, Diana Bolocan, Laura Vasilie, Alexandru Apostu, Chase Helwig, Mihaela Gaman, Michael Brautbar, Edward Raff, Chase Midler, Sven Krasser
url: http://arxiv.org/abs/2607.28460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cybersecurity Detection Classification with Reasoning-enabled Language Models

## Abstract
A major issue in Security Operations Centers (SOCs) is alert fatigue, as the number of detections reported is more than staff can triage in a given day. Prior work prompts or fine-tunes large language models (LLMs) to emit a triage label directly, but does not train them to reason about whether a detection is a genuine threat. We train a chain-of-thought (CoT) reasoning-enabled triage classifier on real, human-labeled Windows endpoint detections by combining automated prompt optimization, self-training, and reinforcement learning with verifiable rewards. We find that CoT reasoning also degrades the label-token probabilities that automated triage relies on, so we separately train a calibrator that reads the full reasoning trace and estimates the probability that the verdict is correct. Our system reaches 82.6% test accuracy and, at the high-confidence operating point that governs automated triage, improves benign recall by 43.0% and malicious recall by 18.3% over a direct-label LLM classifier. We further show that the trained calibrator is necessary - an untrained confidence judge collapses high-confidence recall to zero - and that a finetuned 30B model significantly outperforms frontier general-purpose models, motivating targeted training over scale.

## Metadata
- **Published**: 2026-07-30T16:22:13Z
- **Authors**: Amol Khanna, Manu Nandan, Cristian Viorel Popa, Joan Pujol-Roig, Diana Bolocan, Laura Vasilie, Alexandru Apostu, Chase Helwig, Mihaela Gaman, Michael Brautbar, Edward Raff, Chase Midler, Sven Krasser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28460v1)