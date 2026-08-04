---
title: Personalizing Large Language Model Agents with Small Policy Models
published: 2026-07-31T18:56:30Z
authors: Dian Jin, Zhi Zhang, Huichao Li, Yihe Pan, Rundong Huang, Doudou Zhou
url: http://arxiv.org/abs/2608.00215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personalizing Large Language Model Agents with Small Policy Models

## Abstract
Large language model (LLM) agents can retrieve memory, call tools, ask clarifying questions, and vary response style, yet adapting these execution decisions to an individual user remains difficult. Fine-tuning a separate LLM is costly or impossible for proprietary systems, while prompts and memory primarily expose user information to the agent rather than adapt its execution decisions from feedback. We formulate personalization of a frozen agent as online learning of a per-user execution policy from scalar feedback observed only for the executed action. We propose FABLE (Factorized Adaptive Bandit Layer for Execution), a lightweight policy layer outside a potentially black-box host agent. FABLE factorizes memory, information-acquisition, and response decisions so feedback updates related choices; filters actions through an externally specified feasible set before exploration; and learns user-specific residual preferences relative to a fixed default-and-cost score via Bayesian contextual Thompson sampling. Under a linear residual-reward model, a calibrated variant inherits an expected-regret bound against the best feasible action. We also characterize preferences unidentifiable under persistent feasibility constraints and provide anytime-valid false-promotion control. Across personalized-reasoning, controlled-feedback, and executable tool-use evaluations, FABLE improves several preference-sensitive behaviors relative to rule-only control while remaining competitive on end-to-end task performance.

## Metadata
- **Published**: 2026-07-31T18:56:30Z
- **Authors**: Dian Jin, Zhi Zhang, Huichao Li, Yihe Pan, Rundong Huang, Doudou Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00215v1)