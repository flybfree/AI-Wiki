---
title: When Is a Learned Command Adapter Worth It? Closed-Loop Identification and Counterfactual Auditing of Frozen Locomotion Policies
url: http://arxiv.org/abs/2607.21867v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_23-47-03Z_WhenIsaLearnedCommandAdapterWorthIt_Closed_LoopIde.md
generated_at: 2026-07-26 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when adding a learned adapter to a frozen, command-conditioned locomotion policy is beneficial. It introduces an audit that distinguishes global operating-point gain from same-state counterfactual headroom and deployment or state-allocation gains. On Go2 experiments the audit finds only modest improvements while most queries recommend no adaptation.

## Key Takeaways
- The adapter necessity audit separates global operating-point gain, same-state counterfactual headroom, deployment gain over a fixed action, and state-allocation gain over a randomized policy to produce GO NO-GO ABSTAIN decisions. 
- On Go2 the audit reveals only 5.2% same-state headroom but only 0.55% recovered allocation gain, leading most queries to NO-GO or ABSTAIN. 
- A learner-level synthetic control returns GO while a deployment-representative H1 audit returns NO-GO showing that observable signal may not justify state-dependent adaptation.

## Context
This work addresses the challenge of integrating learned components into frozen policies without overfitting to specific test conditions, which is crucial for safe and robust robotic locomotion. By providing an objective audit framework, it helps researchers evaluate whether theoretical gains translate to real deployment benefits.

## Implications
For practitioners, the audit reduces reliance on optimistic theoretical improvements and encourages evidence‑based decisions about adapter use. It supports safer integration of learned adapters in autonomous systems where safety margins must be preserved.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21867v1)
