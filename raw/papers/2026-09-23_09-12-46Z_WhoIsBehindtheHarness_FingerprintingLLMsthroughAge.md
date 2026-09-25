---
title: Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior
published: 2026-09-23T09:12:46Z
authors: Chuyi Wang, Xiaohui Xie, Tongze Wang, Fangchen Luo, Yong Cui
url: http://arxiv.org/abs/2609.28559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior

## Abstract
LLMs increasingly operate through coding-agent harnesses that inspect repositories, invoke tools, and modify files. Substituting the model behind such an agent can therefore change security-relevant decisions, including whether it verifies changes or recovers safely from failures. Existing LLM fingerprints largely infer identity from direct text or token distributions. In coding agents, these signals are mediated by system instructions, controller logic, tools, and execution feedback, limiting their transfer.   We present LIDAR (LLM Identification from Decisions and Actions at Runtime), an active black-box fingerprinting method for coding-agent execution. Three coding probe pairs expose post-edit verification, transient-failure recovery, and specification--test conflict resolution under controlled changes. LIDAR represents the resulting trajectories with complementary instance-level and distribution-level features and compares them with clean references using a lightweight probabilistic identifier. It requires no access to model weights, logits, or provider internals.   Across 36 models from seven families and two agent harnesses, LIDAR achieves high Top-1 accuracy and MRR and outperforms four existing fingerprinting and API-auditing baselines. Ablations confirm that the two feature levels, all probe pairs, and their controlled variants contribute. These results show that agent execution behavior provides model-identity evidence beyond final outputs.

## Metadata
- **Published**: 2026-09-23T09:12:46Z
- **Authors**: Chuyi Wang, Xiaohui Xie, Tongze Wang, Fangchen Luo, Yong Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28559v1)