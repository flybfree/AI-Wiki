---
title: Toward Plasticity-Preserving KL Regularization for Capability Retention in LLM Reinforcement Learning
published: 2026-08-03T06:10:33Z
authors: Li Wang, Xiaodong Lu, Xiaohan Wang, Jiajun Chai, Wei Lin, Tianhao Peng, Guojun Yin
url: http://arxiv.org/abs/2608.01743v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Plasticity-Preserving KL Regularization for Capability Retention in LLM Reinforcement Learning

## Abstract
Reinforcement learning (RL) has become a central paradigm for large language model (LLM) post-training, but optimization toward new objectives can degrade capabilities already present in the base model. KL regularization is widely used to mitigate such forgetting by constraining policy drift toward a reference model. However, standard full-policy KL regularization constrains the entire response distribution and may unnecessarily restrict exploration and target-task learning. This raises a natural question: can a more precise constraint preserve existing capabilities while minimizing interference with learning new tasks? To this end, we propose \underline{Co}rrectness-Conditioned \underline{KL} Regularization (CoKL), a conditional regularization framework that narrows the preservation constraint from the full output distribution to correctness-conditioned response distributions. We instantiate CoKL with forward KL divergence and derive a practical finite-group training objective for RL-based LLM post-training. At the population level, CoKL decouples the total probability assigned to correct responses from their correctness-conditioned distribution, thereby regularizing the relative probability allocation among reference-supported correct responses without directly anchoring incorrect outputs or total correctness mass. We further show that full-policy forward and reverse KL regularization induce a strict optimal correctness gap when the reference policy is imperfect, whereas CoKL avoids this limitation. Experiments in controlled multi-solution environments and continual post-training settings across multiple model scales demonstrate that CoKL achieves a more favorable balance between target-task improvement and prior-capability retention than existing regularization methods. Our code is available at https://github.com/Lumina04/CoKL.

## Metadata
- **Published**: 2026-08-03T06:10:33Z
- **Authors**: Li Wang, Xiaodong Lu, Xiaohan Wang, Jiajun Chai, Wei Lin, Tianhao Peng, Guojun Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01743v1)