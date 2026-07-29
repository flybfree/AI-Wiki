---
title: Spatial Reasoning in LLM Game Agents: Impact of Causal Context and Multi-Step Planning
published: 2026-07-22T12:10:45Z
authors: Mohit Jiwatode, Ronja Fuchs, Robin Schmöcker, Bodo Rosenhahn, Alexander Dockhorn
url: http://arxiv.org/abs/2607.22732v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spatial Reasoning in LLM Game Agents: Impact of Causal Context and Multi-Step Planning

## Abstract
LLM-based game agents often perform poorly on more complex tasks. This work examines whether these failures are linked to limited spatial reasoning and evaluates whether causal prompt augmentation and multi-step planning can improve win-rates while managing response latency. Using the open-source Qwen3 model family, we conduct experiments across varying model scales, reasoning modes, and planning horizons. We further introduce a focused GVGAI benchmark consisting of three custom games with five difficulty levels to isolate spatial navigation. The evaluation follows two paradigms: an initial ``positioning experiment'' to test an agent's ability to find its exact coordinates, and a study of game-play success. Our results show that while larger models with an enabled thinking mode identify their positions more accurately, overall performance in coordinate matching remains limited for smaller models. Win rates decrease as game levels and layout complexity increase, validating the benchmark's difficulty scaling. Integrating causal context into the prompts tends to improve the agents' success rates, particularly for bigger models. While enabling thinking mode and longer planning horizons significantly improve performance, multi-step planning further reduces mean per-step response times, offering a practical trade-off between reasoning depth and execution speed.

## Metadata
- **Published**: 2026-07-22T12:10:45Z
- **Authors**: Mohit Jiwatode, Ronja Fuchs, Robin Schmöcker, Bodo Rosenhahn, Alexander Dockhorn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22732v1)