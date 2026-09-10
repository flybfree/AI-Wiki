---
title: Do Agents Know When They Succeed? Calibrating Agent Confidence from Internal Representations
url: http://arxiv.org/abs/2609.09448v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_20-58-49Z_DoAgentsKnowWhenTheySucceed_CalibratingAgentConfid.md
generated_at: 2026-09-09 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper explores whether an agent’s internal representations can reliably signal task success in multi‑turn interactive settings. By introducing Latent Trajectory Dynamics and Action Representation Probe, the authors demonstrate that these methods outperform conventional calibration baselines across several benchmarks and model families, providing a zero‑overhead confidence monitor.

## Key Takeaways
- LTD captures systematic shifts in residual‑stream representations throughout an interaction trajectory, offering a continuous measure of confidence that evolves with each step.  
- ARP extracts action‑decision representations to predict success directly, bypassing the need for separate post‑hoc evaluation.  
- Both methods achieve consistent improvements over surface‑level generation and sequence‑based calibration while requiring no changes to prompts or extra rollouts.

## Context
Agentic systems are increasingly deployed in safety‑critical domains where failure is unacceptable. Traditional confidence calibration relies on surface outputs, which often miss the nuanced internal dynamics that drive success or error. This work bridges that gap by leveraging latent dynamics and action representations as intrinsic signals.

## Implications
For practitioners, these methods enable real‑time monitoring without altering system architecture or incurring computational overhead. In industry, they can improve reliability of autonomous agents in high‑stakes applications such as robotics, medical assistance, and financial trading.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09448v1)
