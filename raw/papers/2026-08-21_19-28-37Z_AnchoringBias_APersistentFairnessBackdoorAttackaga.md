---
title: Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning
published: 2026-08-21T19:28:37Z
authors: Yuyang Luo, Kai Shu
url: http://arxiv.org/abs/2608.21577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning

## Abstract
Multimodal Large Language Models (MLLMs) are increasingly deployed in high-stakes domains where fairness is a critical safety requirement. In practice, these models are continually updated through continual learning (CL) to adapt to evolving tasks and data distributions. Prior work has shown that backdoor attacks can manipulate MLLM responses through hidden triggers, but naively implanted backdoors degrade as models undergo subsequent updates of CL. Although fairness has emerged as a central concern for MLLM deployment, whether backdoor-induced fairness violations can survive CL remains unexplored, leaving two critical questions unanswered: (1) whether a backdoor can reliably induce fairness violations in MLLMs, and (2) whether such fairness-targeted backdoors can persist through continual learning. We bridge this gap by proposing Persistent Fairness Backdoor Attack (PFBA) to inject persistent and group-specific discrimination into MLLMs. Specifically, PFBA achieves this through two novel mechanisms. The Latent Space Fairness Reinforcement reshapes the model's deep feature geometry by anchoring privileged-group representations to preserve utility while repelling and clustering targeted-group representations to sustain discrimination, and the Continual Learning Simulation iteratively optimizes the trigger against simulated parameter drift to ensure backdoor persistence across future updates. Extensive experiments demonstrate that PFBA induces severe fairness disparities that persist across continual learning rounds, evading standard backdoor defenses. The data and code are publicly available at https://github.com/lyygua/PFBA.

## Metadata
- **Published**: 2026-08-21T19:28:37Z
- **Authors**: Yuyang Luo, Kai Shu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21577v1)