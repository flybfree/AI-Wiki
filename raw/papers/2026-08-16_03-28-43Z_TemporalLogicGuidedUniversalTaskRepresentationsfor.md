---
title: Temporal Logic Guided Universal Task Representations for Reinforcement Learning
published: 2026-08-16T03:28:43Z
authors: Hao Zhang, Zhangli Zhou, Zhen Kan
url: http://arxiv.org/abs/2608.15509v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Logic Guided Universal Task Representations for Reinforcement Learning

## Abstract
Task guided agents demonstrate strong performance in a wide range of complex tasks. However, most existing task representation algorithms are tailored to specific contexts and struggle to generalize across diverse scenarios. Moreover, they typically depend on gradient signals from reinforcement learning controllers to update their weights, which can degrade both representation quality and learning efficiency. To overcome these limitations, we propose LOTUS, a temporal logic inspired universal task representation framework that can be seamlessly integrated into any RL algorithm to enhance agent performance across diverse task settings. Specifically, we design a novel task representation architecture capable of modeling relationships and extracting task semantics from LTL formulas. We further introduce a more effective update mechanism that treats the LTL encoder as a policy, thereby improving representation capacity. To enhance stability and robustness, LOTUS leverages the bisimulation metric, which provides theoretical guarantees for LTL representation, including behavioral equivalence, optimality fidelity, and trajectory robustness. Experimental results show that LOTUS outperforms most existing methods in learning efficiency, generalization capability, and representation quality. Specifically, LOTUS accelerates convergence over 20% in single-task scenarios, achieves a 15%-45% higher success rate in unseen manipulation tasks, and improves generalization performance over 25% in complex multi-task environments with increased sub-goal depth or conjunctions. The corresponding code, videos, and appendix are available at: https://lotus-website.github.io/.

## Metadata
- **Published**: 2026-08-16T03:28:43Z
- **Authors**: Hao Zhang, Zhangli Zhou, Zhen Kan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15509v1)