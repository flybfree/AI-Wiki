---
title: Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit
published: 2026-08-30T06:53:13Z
authors: Haoxuan Jia, Yang Liu, Yingguang Yang, Yancheng Chen, Chongyang Zhang, Hao Zheng, Qian Li, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Shang Luo, Kefu Xu, Hao Peng, Junyu Lu, Du Cheng, Philip S. Yu, Bin Chong
url: http://arxiv.org/abs/2608.29605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit

## Abstract
Memory operations of long-horizon LLM agents are hard to supervise: an operation's value is unobservable when it is taken. But they are special -- they leave machine-readable evidence in the trajectory: retrieval hits and answer-time citations. Hindsight Memory-PRM exploits this audit trail twice: offline to train an operation-conditioned memory-utility critic, and online, where retrievals, citations, and one controlled deletion-and-reanswer per probe settle an intervention-calibrated entry-level presence credit, propagated along version chains as an action-level proxy reward -- no per-operation human labels, no Monte-Carlo replay of continuations. On held-out LoCoMo a local 8B policy reaches 77.5% under a fixed shared reader, surpassing its API teacher (65.1%) and all reproduced external systems, at one eighth the context of Mem0's official operating point; on LongMemEval, 79.0%. Ablations attribute the gain to causal calibration rather than signal density, and the policy converges to a multi-version memory organization whose gains no tested open-loop baseline reproduces.

## Metadata
- **Published**: 2026-08-30T06:53:13Z
- **Authors**: Haoxuan Jia, Yang Liu, Yingguang Yang, Yancheng Chen, Chongyang Zhang, Hao Zheng, Qian Li, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Shang Luo, Kefu Xu, Hao Peng, Junyu Lu, Du Cheng, Philip S. Yu, Bin Chong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29605v1)