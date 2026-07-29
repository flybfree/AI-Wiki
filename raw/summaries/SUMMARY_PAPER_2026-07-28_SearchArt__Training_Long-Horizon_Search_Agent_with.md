---
title: SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task
url: http://arxiv.org/abs/2607.24850v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-25_06-47-46Z_SearchArt_TrainingLong_HorizonSearchAgentwithScala.md
generated_at: 2026-07-28 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SearchArt, a scalable framework for training long‑horizon search agents using synthetic and verified data. It demonstrates that a 27B parameter model can achieve competitive scores on multiple benchmark tasks. The approach combines verification pipelines with multi‑stage fine‑tuning and reinforcement learning to optimize the agent’s planning and reasoning over extended interactions.

## Key Takeaways
- SearchArt builds large datasets of QA pairs and search trajectories from web documents, then verifies consistency, trajectory quality, and evidence relevance before training.
- The framework uses supervised fine‑tuning followed by reinforcement learning to optimize the agent’s planning and reasoning over extended interactions.
- Results show that a 27B model matches or exceeds state‑of‑the‑art closed‑source agents on BrowseComp‑ZH (74.39), BrowseComp (70.06) and Deepresearch‑bench (52.55).

## Context
Long‑horizon search agents require massive, reliable data to learn complex planning and evidence aggregation across many steps. Existing methods struggle with scalability and verification of intermediate reasoning, limiting performance on long tasks.

## Implications
This work provides a practical pathway for developers to create high‑performing search agents without relying on proprietary benchmark datasets. Practitioners can adopt the verification‑driven pipeline to improve robustness and efficiency in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24850v1)
