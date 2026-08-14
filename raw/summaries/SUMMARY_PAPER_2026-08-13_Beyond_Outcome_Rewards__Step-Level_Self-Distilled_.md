---
title: Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents
url: http://arxiv.org/abs/2608.12764v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_03-13-18Z_BeyondOutcomeRewards_Step_LevelSelf_DistilledPolic.md
generated_at: 2026-08-13 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Step‑Level Self‑Distilled Policy Optimization (SSPO) to improve deep search agents by resolving the mismatch between teacher and student reward signals in on‑policy self‑distillation. By using step‑level evidence anchors and converting teacher‑student disagreement into advantage weights, SSPO updates only incorrect trajectories while preserving correct ones, achieving stronger performance than standard GRPO with fewer gradient steps.

## Key Takeaways
- Evidence Anchors are concise web snippets that serve as privileged step‑level teachers without exposing full answer paths.  
- SSPO injects teacher‑derived advantage weights into GRPO exclusively for wrong trajectories, decoupling direction (outcome reward) from magnitude (teacher modulation).  
- On Qwen3‑8B, SSPO consistently outperforms GRPO on BrowseComp, GAIA and FRAMES while adding only about 5 % overhead per step.

## Context
Deep search agents face sparse outcome rewards that hinder credit assignment across long trajectories. Traditional self‑distillation methods either ignore step granularity or risk leaking teacher knowledge, limiting learning efficiency in large language models.

## Implications
SSPO offers a scalable framework for training search policies with richer reward signals, reducing the need for extensive gradient accumulation and enabling faster iteration cycles. Practitioners can adopt this technique to enhance autonomous reasoning agents without sacrificing diversity of correct solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12764v1)
