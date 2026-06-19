---

title: Reinforcement Learning from Rich Feedback with Distributional DAgger
published: "2026-06-03T17:54:04Z"
authors: Rishabh Agrawal, Jacob Fein-Ashley, Paria Rashidinejad
url: http://arxiv.org/abs/2606.05152v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Reinforcement Learning from Rich Feedback with Distributional DAgger



**Source**: [Original Paper](http://arxiv.org/abs/2606.05152v1)
## Abstract
Reasoning models have advanced rapidly, but the dominant reinforcement learning from verifiable rewards (RLVR) recipe remains surprisingly narrow: sample many responses and reward each with a single bit indicating whether the final answer is correct. Yet many settings provide rich feedback, including execution traces, tool outputs, expert corrections, and model self-evaluations. We study how to use such feedback through a distributional variant of the classic imitation learning algorithm DAgger, where the learner has local access to an expert distribution on states visited by the current policy. This yields a simple forward cross-entropy objective that admits a blackbox expert and whose sequence-level gradient {conduct rich credit assignment by propagating} future expert-student disagreement back to earlier decisions. We show that prior RL with self-distillation objectives based on reverse KL or Jensen-Shannon fail to guarantee monotonic policy improvement: even when the expert has higher reward, their updates may increase probability on worse actions. In contrast, we show that forward cross-entropy admits monotonic policy improvement and enjoys guarantees on regret. We further show that our objective optimizes a lower bound on teacher-weighted likelihood of success, leading to improved Pass@N. Empirically, our approach, DistIL, improves over RLVR and RL with self-distillation baselines across a variety of domains: scientific reasoning, coding, and solving hard mathematical problems.

## Metadata
- **Published**: 2026-06-03T17:54:04Z
- **Authors**: Rishabh Agrawal, Jacob Fein-Ashley, Paria Rashidinejad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.05152v1)