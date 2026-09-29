---
title: Before Acting, Change the State: Prospective State Intervention for Web Agents under Deceptive Interfaces
url: http://arxiv.org/abs/2609.34974v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_11-53-24Z_BeforeActing_ChangetheState_ProspectiveStateInterv.md
generated_at: 2026-09-28 22:59
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Veer, a runtime defense for LLM-based web agents against deceptive interfaces that intervenes on the web state rather than restricting agent behavior. By constructing and verifying prospective intervention trajectories to transition the environment to safe states before action execution, Veer prevents unauthorized consequences while maintaining high task completion rates across multiple benchmarks.

## Key Takeaways
- Veer identifies a critical failure mode where valid actions yield unauthorized outcomes due to deceptive web states, motivating a shift in defense strategy from behavioral blocking to active runtime control of the web environment as a primary safety target.
- The system implements prospective state intervention by generating and verifying safe trajectories that modify the live environment prior to action execution, utilizing runtime grounding and verification to ensure the transition to a secure state without disrupting task progress.
- Veer achieves superior performance on TrickyArena and WebDecept benchmarks, reducing dark-pattern success to 0.3% and outperforming existing defenses by up to 25 percentage points in safe task completion, with ablation studies confirming that active state intervention

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34974v1)
