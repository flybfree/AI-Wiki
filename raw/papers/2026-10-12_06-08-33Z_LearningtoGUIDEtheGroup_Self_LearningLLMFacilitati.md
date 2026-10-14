---
title: Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks
published: 2026-10-12T06:08:33Z
authors: Ziyi Liu, Tzu-Sheng Kuo, Jiale Liu, Deqing Fu, Nithum Thain, Crystal Qian
url: http://arxiv.org/abs/2610.16231v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks

## Abstract
As large language models are increasingly adopted as multi-party communication facilitators, there is a growing demand for agents capable of balancing diverse group dynamics across contexts. However, existing LLM facilitators are often fine-tuned for task-specific objectives; generalized LLM-based facilitation methods that can adapt to different types of tasks and diverse group dynamics are underdeveloped. To address this gap, we present GUIDE (Generalized Unified Intervention for Dynamic Exchanges, a framework for developing generalized LLM-based facilitators across different multi-party contexts. GUIDE evaluates facilitation across both objective task outcomes and subjective metrics, including psychological safety and perceived friction. Within this framework, we study whether LLMs can self-learn generalized facilitation strategy offline to real-time interventions. We first collect multi-party human interactions guided by task-specific expert LLM facilitators (N=432 conversations). We then employ a self-learning method in which an LLM induces an actionable strategic playbook from conversations and iteratively refines it using feedback from an LLM judge aligned with human annotators (N=20), developing a single generalized facilitator that outperforms the three task-specific expert facilitators on held-out conversations 61.4% win rate. Finally, we evaluate these improvements empirically; in a real-time online empirical study, the self-learned generalized facilitator preserves facilitator performance and group productivity, improves speaking comfort and reduces interpersonal friction, while using 24.7% fewer turns and 29.0% fewer words than the expert prompts. These findings provide empirical evidence that LLMs can learn generalizable, task-agnostic social facilitation from task-specific human interactions, on-par with hand-crafted task-specific prompts across diverse group settings.

## Metadata
- **Published**: 2026-10-12T06:08:33Z
- **Authors**: Ziyi Liu, Tzu-Sheng Kuo, Jiale Liu, Deqing Fu, Nithum Thain, Crystal Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16231v1)