---
title: ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents
published: 2026-08-10T11:45:03Z
authors: Hongwei Yao, Yiming Liu, Meihui Chen, Jieling Chen, Zikun Chen, Yiling He, Wangze Ni, Cong Wang, Kui Ren
url: http://arxiv.org/abs/2608.09476v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents

## Abstract
Cowork agents may complete benign tasks while disclosing protected data, manipulating unauthorized state, invocate unauthorized API. We define behavioral safety and introduce ActBench, a self-evolving benchmark that evaluates such behavior risk from execution trajectories rather than final responses. Each case pairs a benign task with an adversarial variant that preserves its instruction, configuration, initial state, rating model, and trusted records while injecting a task-reachable payload. ActBench contains 600 cases from 213 scenarios, spanning 15 risk behaviors, six execution spaces, and 48 web-service APIs.To move beyond static payloads, we propose a reward-guided beam search method that jointly optimizes attack effectiveness and task utility, while reflection diagnoses failed execution checkpoint and guides payload revision. Besides, we propose a dual evidence verification mechanism that verifies agent execution safety and utility through log evidence and LLM-based trajectory evidence.We evaluate 15 LLMs and 6 open-source cowork agents over 24,000 trajectories. Under a fixed harness, attack success rates ranges from 10.1% to 94.4% across models, while under a fixed base model, they range from 73.7% to 94.4% across agents.These results show greater variation across models than agent harness, while attacks remain highly successful across all tested harnesses.Our benchmark is released at: https://github.com/zjuicsr/ActBench.

## Metadata
- **Published**: 2026-08-10T11:45:03Z
- **Authors**: Hongwei Yao, Yiming Liu, Meihui Chen, Jieling Chen, Zikun Chen, Yiling He, Wangze Ni, Cong Wang, Kui Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09476v1)