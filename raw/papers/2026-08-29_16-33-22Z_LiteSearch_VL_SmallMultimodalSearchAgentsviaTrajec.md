---
title: LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO
published: 2026-08-29T16:33:22Z
authors: Saeed Khaki, Nima Safaei, Kamal Ginotra
url: http://arxiv.org/abs/2608.29357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO

## Abstract
Multimodal search agents answer visual questions by interleaving image understanding, web retrieval, tool use, and evidence synthesis. Strong systems exist, but in two expensive regimes: proprietary frontier models such as GPT-5 and Gemini, or large open vision-language backbones trained with substantial agentic data and reinforcement learning. We ask a different question: when released agent trajectories are distilled into much smaller backbones under a single-node budget, what is actually transferred? We study this with LiteSearch-VL, a low-compute recipe for Qwen3-VL-2B and Qwen3-VL-4B that uses only released OpenSearch-VL trajectories, parameter-efficient LoRA adapters, and synthetic step-level preferences: DPO on GPT-5-generated hard negatives targeting five local failure modes (premature answer, wrong tool, weak query, repeated query, ignored image). Across 12,400 GPT-5-judged rollouts on SimpleVQA, FVQA, LiveVQA, and VDR-Bench-testmini, the dominant effect is behavioral rather than a uniform accuracy lift: full-trajectory supervised fine-tuning transfers the agent contract, taking the 2B model from almost never emitting a usable answer (1,237/1,240 no_answer rollouts) to 28.4% macro Pass@1, matching or slightly exceeding the off-the-shelf 4B base (25.6%). Synthetic preference learning and compact tool distillation act as refinements rather than phase transitions (best 4B configuration: 30.8% macro Pass@1). Finally, a controlled VDR step-budget ablation shows that extra search turns convert abstentions into wrong_entity errors rather than correct answers, identifying answer verification, not search depth, as the next bottleneck for small multimodal agents.

## Metadata
- **Published**: 2026-08-29T16:33:22Z
- **Authors**: Saeed Khaki, Nima Safaei, Kamal Ginotra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29357v1)