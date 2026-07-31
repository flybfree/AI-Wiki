---
title: SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them
url: http://arxiv.org/abs/2607.27703v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_05-39-01Z_SpatialCLI_LearningtoReasonWithSpatialTools_ThenWi.md
generated_at: 2026-07-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SpatialCLI, a framework that teaches vision-language models to use spatial tools and then internalize their capabilities. The method improves performance on complex perception tasks by gradually moving from tool reliance to self‑reliance.

## Key Takeaways
- The three‑stage pipeline exposes specialist vision models as tools, learns tool usage via cold‑start SFT and agentic RL, and finally verbalizes successful trajectories to internalize the specialists. 
- SpatialCLI-Bench provides a comprehensive benchmark with 516 examples across localization, segmentation, depth, and pose. 
- On MindCube, the model reaches 84.6% with tools, exceeding GPT‑5.6 Sol’s 72.1%, while retaining 73.8% performance after internalization.

## Context
Vision‑language models struggle to bridge detailed visual perception and high‑level reasoning, limiting their utility in embodied agents. This work addresses the mismatch by integrating specialist vision tools into a learning pipeline that gradually embeds those capabilities internally.

## Implications
The results show that systematic tool integration can dramatically boost agent performance without sacrificing long‑term efficiency. Practitioners can adopt similar staged approaches to enhance model robustness and reduce reliance on external specialists.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27703v1)
