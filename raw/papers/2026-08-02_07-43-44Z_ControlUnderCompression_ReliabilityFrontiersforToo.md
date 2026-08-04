---
title: Control Under Compression: Reliability Frontiers for Tool-Using Agents
published: 2026-08-02T07:43:44Z
authors: Yinghan Hou, Zongyou Yang
url: http://arxiv.org/abs/2608.01056v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Control Under Compression: Reliability Frontiers for Tool-Using Agents

## Abstract
Tool-using language-model agents are governed not only by task prompts but also by persistent system-side instructions that specify tools, arguments, policies, execution protocols, and recovery. Compressing these agent control contexts (ACCs) can reduce input cost and context use, yet existing prompt-compression evaluations do not reveal whether the resulting control remains operationally reliable. We introduce CompressAgent, an environment-verified benchmark for ACC compression across nine independently constructed ACCs, three task families, three fixed Qwen API model identifiers, six retained-context budgets, and 15,525 runs. We uncover a nonlinear, method-dependent reliability frontier. At 75% retained context, generic rewriting and section-based compression achieve 92.7% and 92.4% success, close to the 93.8% full-context baseline. Between 50% and 35%, methods diverge sharply; at 35%, section-based, obligation-aware, and generic rewriting achieve 47.0%, 39.0%, and 19.9%. At retained-context budgets from 25% to 10%, executable protocols become fragile. Reliability also varies substantially across ACCs, making universal compressor rankings inappropriate and motivating per-context qualification. Failure analysis shows that compression primarily surfaces as tool-execution and action-parsing errors. These findings recast ACC compression from token reduction into a runtime-reliability problem that must be evaluated through executable outcomes.

## Metadata
- **Published**: 2026-08-02T07:43:44Z
- **Authors**: Yinghan Hou, Zongyou Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01056v1)