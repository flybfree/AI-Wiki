---
title: The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning
published: 2026-08-22T09:30:29Z
authors: Jing Yu, Shengchao Chen, Yiyun Tan
url: http://arxiv.org/abs/2608.21871v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning

## Abstract
Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejecting post hoc, never learning where along an environment's difficulty axis to place a task, and credit the solver with sparse terminal rewards alone. We recast zero-data self-play as a pursuit-evasion game: in LURE, an LLM evader positions tasks along each environment's difficulty axis to stay one step ahead of a planner-executor pursuer that hunts it down through verifiable interaction. The evader is trained on a capture-frontier reward that peaks when the solver captures it on exactly half of its rollouts, turning barely catchable into a learned positioning strategy rather than a hand-tuned rejection band. The pursuer earns capture-anchored dense process credit, in which monotone verifier progress is group-normalized jointly with the terminal capture under a round-anchored KL that keeps the co-evolution stable. Across three verifiable reasoning environments and three backbone families, LURE outperforms advanced baselines under unified/specialist settings, while the unified model attains stronger aggregate OOD zero-shot accuracy than all trained baselines across nine held-out benchmarks from three task families.

## Metadata
- **Published**: 2026-08-22T09:30:29Z
- **Authors**: Jing Yu, Shengchao Chen, Yiyun Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21871v1)