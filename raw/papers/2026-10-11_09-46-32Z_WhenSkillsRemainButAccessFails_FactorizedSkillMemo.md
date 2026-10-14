---
title: When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization
published: 2026-10-11T09:46:32Z
authors: Haomiao Qiu, Yining Tang, Hongyi Wan, Changfeng Sun, Ziyue Qiao, Miao Zhang
url: http://arxiv.org/abs/2610.15492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization

## Abstract
Skill internalization aims to convert externally specified procedural skills into persistent model capabilities, allowing language-model agents to execute them without retrieving or reinjecting skill descriptions at inference time. Yet when new skills are learned continually, whether previously internalized skills remain usable is still poorly understood. We study forgetting in continual skill internalization and uncover a clear hierarchical structure. Early in subsequent training, a model may lose the ability to invoke an old skill from the raw request, while supplying only the correct canonical skill name substantially restores the learned behavior; with further optimization, this conditional execution also degrades. We call these two stages skill-addressing forgetting and skill-execution forgetting. Guided by this finding, we introduce Factorized Skill Memory (FSM), which separates continual skill memory into a plastic Address Memory and a stable Execution Memory. At each stage, FSM trains a new LoRA executor using only current-stage data, freezes it after acquisition, and appends it to Execution Memory; in parallel, Address Memory incrementally learns to map current requests to executors without replaying historical requests or execution trajectories. At inference time, Address Memory selects one executor from the raw request, and only that frozen executor performs a single language-model generation. On a five-stage benchmark built from 100 TaskBench skills, FSM achieves 65.95% mean exact match and 93.38% addressing accuracy across two task orders, improving over the strongest replay-free parameter-isolation baseline by 14.3 percentage points while remaining within 1.9 points of Replay, which retains historical training examples.

## Metadata
- **Published**: 2026-10-11T09:46:32Z
- **Authors**: Haomiao Qiu, Yining Tang, Hongyi Wan, Changfeng Sun, Ziyue Qiao, Miao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15492v1)