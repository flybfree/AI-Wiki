---
title: Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies
published: 2026-08-13T00:30:04Z
authors: Conor F. Hayes, Elliot Meyerson, Kajetan Schweighofer, Roberto Dailey, Babak Hodjat, Risto Miikkulainen, Xin Qiu
url: http://arxiv.org/abs/2608.12679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies

## Abstract
Large Language Models (LLMs) are increasingly deployed in discovery domains such as math and science. The usual approach is to present the problem to the model and use its answer as the proposed solution. However, beyond this best guess, discovery can be enhanced by increasing test-time compute. In a process called pass@k, the model is allowed to explore the solution space and generate diverse candidate solutions. Unfortunately, the standard approach to post-training LLMs through Reinforcement Learning (RL) may limit pass@k: the model's output distribution narrows around high-reward outputs, causing the solution coverage to collapse. The alternative is to use Evolution Strategies (ES), a population-based, gradient-free post-training method that optimizes directly in weight space through random perturbations. As this paper shows, ES achieves consistently higher pass@k than RL and produces a broader output distribution with greater solution coverage. This coverage in turn makes it possible to achieve better results in e.g. standard math benchmarks. Thus, ES provides a better foundation for post-training in discovery problems and other domains where diverse solution coverage is critical.

## Metadata
- **Published**: 2026-08-13T00:30:04Z
- **Authors**: Conor F. Hayes, Elliot Meyerson, Kajetan Schweighofer, Roberto Dailey, Babak Hodjat, Risto Miikkulainen, Xin Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12679v1)