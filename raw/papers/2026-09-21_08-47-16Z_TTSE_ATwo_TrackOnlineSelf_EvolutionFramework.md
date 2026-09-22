---
title: TTSE: A Two-Track Online Self-Evolution Framework
published: 2026-09-21T08:47:16Z
authors: Ruimin Pei, Yongkang Wu, Shangyi Zheng, Yaqing Zhang, Deyang Li, Jianjun Tao, Xinyu Zhang, Xiang Zhang
url: http://arxiv.org/abs/2609.24289v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TTSE: A Two-Track Online Self-Evolution Framework

## Abstract
As Large Language Model (LLM) agents are applied in continuously interactive environments, driving the evolution of their own capabilities becomes a core problem for achieving long-term autonomy. Currently, environmental knowledge is typically treated as an external fixed input rather than as part of the agent's ongoing evolution. Reinforcement learning methods usually optimize policies through environmental interaction but tend to adapt only to fixed task distributions or single environments. This paper proposes TTSE (Two-Track Self-Evolution), a dual-track online self-evolution framework that separates evolving knowledge into FACT (environmental facts, whose reliability is continuously verified through interaction evidence) and TIP (task-conditioned implementation procedures). From a decision-theoretic perspective, we decompose the agent's excess risk into environment-representation regret and conditional-execution regret, characterize the conditions under which environment-conditioned policies strictly outperform condition-agnostic policies, and bound the downstream risk in terms of FACT identification error and cross-condition mismatch cost. In practice, TTSE's ablation experiments on GDPevo validate the advantage of dual-track evolution. On the classic agent task benchmarks ALFWorld and ScienceWorld, TTSE further demonstrates superior task adaptation. Moreover, TTSE is broadly compatible with existing skill self-evolution methods; combined with the Bayesian-Agent algorithm, a single-track ablation validates the dual-track advantage, substantially improving the aggregate score across the five major domains of SOPBench over three independent repetitions. Finally, on the real end-to-end task benchmark PinchBench, TTSE is integrated into a general agent framework via retrieval-based injection and stably outperforms the baseline across three independent runs.

## Metadata
- **Published**: 2026-09-21T08:47:16Z
- **Authors**: Ruimin Pei, Yongkang Wu, Shangyi Zheng, Yaqing Zhang, Deyang Li, Jianjun Tao, Xinyu Zhang, Xiang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24289v1)