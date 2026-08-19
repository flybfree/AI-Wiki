---
title: Agent Lightning v1.0: Towards Harnessed Agentic RL
published: 2026-08-18T08:50:13Z
authors: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo
url: http://arxiv.org/abs/2608.17528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Lightning v1.0: Towards Harnessed Agentic RL

## Abstract
Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an approach later adopted by frameworks such as verl Uni-Agent, AReaL 2.0, slime, and Polar. We refer to this paradigm as harnessed agentic RL, where the deploy-time harness directly participates in model post-training. Harnessed agentic RL differs fundamentally from traditional agentic RL: the harness, rather than the training engine, owns the environment interaction loop, while the trainer observes only sequences of LLM request-response pairs. This introduces challenges in retokenization, sample merging, advantage calculation, loss normalization, and backend scheduling, which can substantially affect training stability and effectiveness. We present Agent Lightning v1.0, a lightweight framework for harnessed agentic RL implemented in approximately 3,500 lines of code. It supports arbitrary agent harnesses and serves as a practical testbed for studying these challenges. We evaluate it on instruction-following, search, and coding agents, and provide a complete reproducible pipeline for coding-agent RL. Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, a 14.6-point absolute gain. We release the complete workflow and training scripts to facilitate reproducible research on harnessed agentic RL.

## Metadata
- **Published**: 2026-08-18T08:50:13Z
- **Authors**: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17528v1)