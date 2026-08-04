---
title: CRISP: Critical Step Perception for Training Efficient Deep Search Agents
published: 2026-08-03T08:15:18Z
authors: Haosi Mo, Zihao Yan, Ruiqing Zhang, Zhongli Li, Hexuan Deng, Xuebo Liu, Min Zhang
url: http://arxiv.org/abs/2608.01867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRISP: Critical Step Perception for Training Efficient Deep Search Agents

## Abstract
Large language models (LLMs) are increasingly extended into deep search agents that solve complex questions through multi-step interaction with external search and browsing tools. However, existing agents often incur substantial computational and interaction costs, generating lengthy trajectories that contain redundant queries, inefficient exploration, and irrelevant observations. Existing efficiency-oriented methods usually encourage agents to use tools less frequently, but treating all tool interactions uniformly may also suppress steps that gather necessary evidence. In this paper, we propose CRISP, a framework for training efficient deep search agents through critical step perception. Unlike prior efficiency methods that uniformly penalize tool use, CRISP distinguishes interactions that gather necessary evidence from redundant ones and shapes the training reward to preserve the former while pruning the latter, improving efficiency without sacrificing the evidence needed for correct answers. Specifically, CRISP first constructs critical-step labels with Backward Evidence Induction: starting from the final answer, a strong model traverses a completed search trajectory backward and judges whether each tool-interaction step provides or preserves evidence for the final answer. We then distill these step-wise judgments into a smaller critical-step recognizer, enabling full-trajectory analysis in a single pass. During policy optimization, an efficiency-aware reward is applied only to successful rollouts. Experiments on BrowseComp and HLE-Verified show that CRISP maintains competitive final-answer accuracy while reducing average interaction turns by 15.1% and 33.2%, respectively, demonstrating substantial improvements in interaction efficiency.

## Metadata
- **Published**: 2026-08-03T08:15:18Z
- **Authors**: Haosi Mo, Zihao Yan, Ruiqing Zhang, Zhongli Li, Hexuan Deng, Xuebo Liu, Min Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01867v1)