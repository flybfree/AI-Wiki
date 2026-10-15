---
title: Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach
published: 2026-10-14T02:21:09Z
authors: Jiarui Qin, Junjie Huang, Yunjia Xi, Di Yin, Yong Yu, Weinan Zhang, Xing Sun, Weiwen Liu
url: http://arxiv.org/abs/2610.19425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach

## Abstract
Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but provide limited visibility into how base models behave in interactive environments. We introduce ASAP (Agent Scaffold Adaptation for Pretraining Evaluation), a lightweight framework for eliciting and evaluating agentic behavior from pretrained base models on end-to-end tasks. Rather than converting base models into chat-style agents, ASAP preserves the completion interface and adapts existing agent scaffolds through structured trajectory continuation, short reference prefixes, and minimal recovery mechanisms. Across software-engineering and deep-research benchmarks, ASAP yields discriminative end-to-end performance across base models and pretraining checkpoints. Beyond aggregate scores, ASAP exposes model-generated execution trajectories, enabling analysis of exploration, editing, testing, recovery, and task completion across training stages. These trajectories provide a behavioral view of how agent-relevant capabilities change during pretraining and how execution patterns differ after post-training. Our results suggest that end-to-end agent evaluation can complement conventional pretraining benchmarks by providing a practical diagnostic of interactive model behavior.

## Metadata
- **Published**: 2026-10-14T02:21:09Z
- **Authors**: Jiarui Qin, Junjie Huang, Yunjia Xi, Di Yin, Yong Yu, Weinan Zhang, Xing Sun, Weiwen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19425v1)