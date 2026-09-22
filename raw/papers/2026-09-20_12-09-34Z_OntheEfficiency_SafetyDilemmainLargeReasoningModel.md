---
title: On the Efficiency-Safety Dilemma in Large Reasoning Models
published: 2026-09-20T12:09:34Z
authors: Yifei Yang, Zouying Cao, Xingrui Wang, Xiao Zhou, Yuexian Li, Dongjie Yang, Hai Zhao
url: http://arxiv.org/abs/2609.23587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Efficiency-Safety Dilemma in Large Reasoning Models

## Abstract
Large reasoning models (LRMs) incur high inference costs, often mitigated by efficiency techniques like quantization and pruning. However, the impact of these techniques on model adversarial robustness remains largely unexplored. This study provides the first comprehensive analysis of the interplay between efficiency, jailbreak vulnerability, and reasoning in LRMs. We find that while efficiency methods seemingly reduce the success rate of jailbreak attacks, this improvement is often superficial. It largely arises from degraded reasoning capabilities leading to "attempted but failed" malicious responses, rather than an increase in genuine alignment. Mechanistic analysis of representational drift confirms this, revealing a strict coupling between reasoning capability loss and the model's inability to maintain malicious semantic trajectories. Additionally, we identify quantization with pruning as the optimal strategy to balance efficiency and robustness. These findings clarify the distinction between true safety alignment and capability-induced failure, providing an empirical foundation for LRM deployment.

## Metadata
- **Published**: 2026-09-20T12:09:34Z
- **Authors**: Yifei Yang, Zouying Cao, Xingrui Wang, Xiao Zhou, Yuexian Li, Dongjie Yang, Hai Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23587v1)