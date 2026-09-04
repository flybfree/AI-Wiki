---
title: You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring
published: 2026-09-02T18:07:14Z
authors: Aritra Das, Jaee Ponde, Mihir More, Debayan Gupta
url: http://arxiv.org/abs/2609.03035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring

## Abstract
LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are being monitored, and when they additionally receive feedback from the monitor. We keep the models, probes, and thresholds fixed and change only what the agents are told: nothing (baseline), that an activation monitor is present (aware), or that a monitor is present together with the previous round's score (feedback). We test two games, a four-agent blackjack game and a two-agent Simmons prisoners game, using Qwen3-32B-AWQ and GPT-OSS-20B in homogeneous and mixed pairings. Telling agents about the monitor does not hide them. The best probes stay accurate in all three conditions, and the agents keep colluding.

## Metadata
- **Published**: 2026-09-02T18:07:14Z
- **Authors**: Aritra Das, Jaee Ponde, Mihir More, Debayan Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03035v1)