---
title: Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks
published: 2026-09-30T11:50:06Z
authors: Zezhong Wang, Xueyang Tang, Rui Lian, Yang Lou, Heqing Huang
url: http://arxiv.org/abs/2609.39549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks

## Abstract
As Large Language Model (LLM) agents are increasingly deployed in complex environments, multi-turn interaction attacks have become a significant security challenge. Existing detection methods typically rely on historical context. However, this retrospective logic struggles to identify deep malicious intents that are split across turns to hide future risks. Inspired by speculative decoding, we propose the Speculative Safety Honeypot (SSH) framework. SSH uses a multi-agent simulation system composed of small LLMs to build an action-level speculate-and-verify workflow. In the speculation stage, SSH predicts future behaviors of the target agent and asynchronously builds a trajectory tree to expose potential risks in advance. In the verification stage, the system uses the target agent's real actions to calibrate and prune the trajectory tree, effectively reducing false positives. As a plug-and-playable component, SSH provides existing detectors with rich decision redundancy beyond the current interaction slice. By judging risk based on the evolution of the entire trajectory tree rather than a single point in time, the system reduces the reliance on the absolute precision of individual detection components. This improves the defense resilience and the warning lead-time of agent systems against complex temporal attacks.

## Metadata
- **Published**: 2026-09-30T11:50:06Z
- **Authors**: Zezhong Wang, Xueyang Tang, Rui Lian, Yang Lou, Heqing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39549v1)