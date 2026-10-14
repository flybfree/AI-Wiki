---
title: Terrarium: Growing Personal Assistants via Scalable Synthesis of App Worlds
published: 2026-10-10T12:30:31Z
authors: Mengzhou Wu, Yuzhe Guo, Jiawen Tao, Xiaokun Yuan, Yuan Cao, Gang Cao, Yuetang Deng, Zhi Gong, Dezhi Ran, Linyi Li, Wei Yang, Tao Xie
url: http://arxiv.org/abs/2610.14860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Terrarium: Growing Personal Assistants via Scalable Synthesis of App Worlds

## Abstract
Advances in large language models (LLMs) have brought the vision of a general-purpose personal assistant closer to reality. Such assistants could provide a unified natural-language interface to a broad ecosystem of applications. However, real-world applications do not readily support training at scale because access is often restricted and their state is difficult to reset. To address this challenge, we introduce Terrarium, a framework that synthesizes executable App Worlds from real-world application information, generates training task packages with evaluator-side rubrics from these worlds, and iteratively validates and refines both through agent rollouts. For App World synthesis, Terrarium organizes public Web information and in-application observations into structured app specifications that guide the construction of self-contained runtimes with callable operations and mutable, resettable state. For task synthesis, Terrarium constructs tasks grounded in App World state together with evaluator-side outcome rubrics that assess success without prescribing reference trajectories. We construct a training suite of 275 App Worlds and 13,344 tasks for outcome-based reinforcement learning across three Qwen3 model scales (4B, 8B, and 14B parameters). Across these scales, models trained with Terrarium outperform the corresponding Qwen3 models by an average of 18.34 percentage points on the $τ^2$-bench and 10.94 percentage points on the AppWorld bench. These results suggest that app-grounded world and task synthesis offers a scalable path toward general-purpose assistants capable of operating across broad application ecosystems.

## Metadata
- **Published**: 2026-10-10T12:30:31Z
- **Authors**: Mengzhou Wu, Yuzhe Guo, Jiawen Tao, Xiaokun Yuan, Yuan Cao, Gang Cao, Yuetang Deng, Zhi Gong, Dezhi Ran, Linyi Li, Wei Yang, Tao Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14860v1)