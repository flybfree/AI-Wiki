---
title: SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills
published: 2026-10-26T11:07:04Z
authors: Chenxu Zhang, Zhou Liu, Wu Xin, Wentao Zhang
url: http://arxiv.org/abs/2610.35215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills

## Abstract
Web agents reuse skills whose stored code, selected version, and loaded implementation can diverge across tasks and updates. SkillLifeBench links these states to task outcomes in 388 paired scenarios spanning implementation, interface, runtime, composition, and version changes. We evaluate 14 models on two paired decision tracks: 89 runtime tasks and 60 autonomous lifecycle tasks spanning 12 templates derived from introduced cases. Lifecycle tasks allow agents to inspect, select, and reconfigure skills while completing verifiable user requests. Joint success requires task completion without the registered attack goal. GPT-5.6-Sol and Sonnet 4.6 both achieve 82.0% on runtime tasks, but reach 96.7% and 56.7% on lifecycle tasks. Across lifecycle evaluations, challenged task success is 77.5%, while joint success is 65.2%; 103 runs complete the task and the attack goal. Adding execution provenance in a matched recovery study raises utility joint success from 49.35% with logs and metadata to 65.58%. A deterministic execution-consistency rule reaches 64.94% with higher benign utility, while full restoration reaches 69.48%. Lifecycle tasks distinguish models with similar runtime scores, and execution evidence improves recovery.

## Metadata
- **Published**: 2026-10-26T11:07:04Z
- **Authors**: Chenxu Zhang, Zhou Liu, Wu Xin, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35215v1)