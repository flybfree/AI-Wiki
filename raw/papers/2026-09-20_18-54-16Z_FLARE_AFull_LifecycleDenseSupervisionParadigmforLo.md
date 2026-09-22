---
title: FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model
published: 2026-09-20T18:54:16Z
authors: Jingxuan Xu, Gang Wu, Yanan Wu, Yutao Mou, Songwei Yu, Tianzhuang He, Zhengshuo Gong, Zhao Liu, Zihang Xu, Wenqiang Zhu, Xinping Lei, Weihao Li, Yuhui Bai, Zhongqiu Wang, Yan Wu, Ariel Deng
url: http://arxiv.org/abs/2609.23808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model

## Abstract
While test-time scaling enhances Large Language Model (LLM) agents in long-horizon software engineering (SWE), sparse binary rewards (Pass/Fail) create a severe credit assignment crisis and waste failed exploratory trajectories. Current trajectory optimization and scaling methods are costly and structurally limited, relying on heuristic state reuse without causal diagnosis or delayed scalar scoring without actionable online guidance. We propose FLARE (Full-Lifecycle Alignment and Reward Engine), a novel dense supervision paradigm driven by a lightweight Generative Reward Model (GRM). First, RADAR, an offline causal-aware diagnostic framework, extracts high-fidelity, hindsight-free supervision through causal-chain backtracking to distill a GRM providing real-time, step-level risk feedback. Second, FLARE uses this GRM to continuously optimize the agent across its entire lifecycle. During inference, FLARE acts as an Active Scaffold, autonomously intercepting high-risk generation steps for localized breakpoint re-execution, drastically reducing compute overhead. During post-training, the GRM's structured signals serve as process-supervised reranking scores for Supervised Fine-Tuning (SFT) and step-level dense rewards for Reinforcement Learning (RL), mitigating policy collapse in sparse environments. Extensive evaluations show that FLARE establishes a new Pareto frontier across the agent lifecycle: FLARE (N=1) outperforms Global Rollout (N=5) with a 5x reduction in token consumption. Extending FLARE to training overcomes the sparse reward problem in long-horizon interactive tasks, delivering relative performance gains of 19.13% in SFT through process-aware data curation and a consistent 9.19% improvement in RL.

## Metadata
- **Published**: 2026-09-20T18:54:16Z
- **Authors**: Jingxuan Xu, Gang Wu, Yanan Wu, Yutao Mou, Songwei Yu, Tianzhuang He, Zhengshuo Gong, Zhao Liu, Zihang Xu, Wenqiang Zhu, Xinping Lei, Weihao Li, Yuhui Bai, Zhongqiu Wang, Yan Wu, Ariel Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23808v1)