---
title: Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning
published: 2026-09-30T10:35:41Z
authors: Quan M. Tran, Zhuo Huang, Zhen Fang, Jing Zhang, Mingming Gong, Tongliang Liu
url: http://arxiv.org/abs/2609.39473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning

## Abstract
Autonomous agents increasingly rely on memory to generalize beyond their training environments. However, agents are bounded by what they have seen and believed, and leveraging such memories in unseen environments can introduce biases into their internal beliefs. We formalize this phenomenon as \textit{false memory}, which can arise from spurious correlations, environment shifts, and knowledge conflicts. Despite its importance, false memory is difficult to evaluate because it stems from agent internal beliefs and is easily confounded with ordinary generalization failures. Therefore, we propose FAME, a training-free framework that evaluates false memory through the evolution of agent beliefs under counterfactual reasoning. Specifically, counterfactual scenarios reveal how beliefs change as the latent concept of memory shifts under hypothetical interventions; thus, measuring the resulting concept drift provides a signal for distinguishing faithful versus false memory. Such concepts can be estimated from agent hidden states before answer generation, avoiding the need for reward design or answer sampling. Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% - 96.7% across false-memory settings, and outperforms the best baseline by 3.4% - 23.3% across realistic benchmarks, spanning math reasoning (GSM-Symbolic), code generation (GitChameleon), and complex reasoning (BigBench-Hard). We further release corresponding counterfactual templates and facilitate future research on false memory.

## Metadata
- **Published**: 2026-09-30T10:35:41Z
- **Authors**: Quan M. Tran, Zhuo Huang, Zhen Fang, Jing Zhang, Mingming Gong, Tongliang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39473v1)