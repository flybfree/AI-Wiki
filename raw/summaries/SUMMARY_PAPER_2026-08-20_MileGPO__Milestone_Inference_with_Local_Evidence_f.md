---
title: MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents
url: http://arxiv.org/abs/2608.19803v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_08-58-27Z_MileGPO_MilestoneInferencewithLocalEvidenceforGrap.md
generated_at: 2026-08-20 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
MileGPO introduces a method for assigning credit to intermediate milestones in long-horizon agentic reinforcement learning, addressing the gap between final rewards and step‑level signals. By combining milestone discovery with reliability calibration and progress contrastive testing, the approach yields accurate process‑level credits without extra models or environment interaction.

## Key Takeaways
- Milestone Discovery uncovers candidate milestones on successful rollouts and recurring traps on failed ones, providing a structured set of points for credit assignment.
- Reliability‑Calibrated Shaping (RCS) assigns higher confidence weights to reliable milestones while down‑weighting uncertain candidates, improving the quality of inferred credits.
- Progress‑Contrastive Calibration (PCC) verifies that each candidate reflects genuine local progress and outperforms alternatives from the same state, strengthening the reliability of the discovered milestones.

## Context
Long‑horizon reinforcement learning struggles to allocate credit fairly across many steps when only terminal rewards are observed. Traditional techniques often rely on trajectory grouping or graph‑based advantage estimation, which can miss nuanced intermediate events that shape long‑term behavior.

## Implications
This work advances policy optimization by making milestone credit inference more precise and interpretable, enabling agents to learn from finer-grained progress signals. Practitioners can leverage MileGPO to improve training efficiency and reduce the gap between in‑distribution and out‑of‑distribution performance on complex environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19803v1)
