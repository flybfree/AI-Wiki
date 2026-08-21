---
title: SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation
url: http://arxiv.org/abs/2608.19425v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_20-24-29Z_SCAPE_Scenario_ConditionedSimulation_AugmentedPoli.md
generated_at: 2026-08-20 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
SCAPE is a scenario‑conditioned simulation‑augmented policy evaluation framework that predicts real‑world performance of robot policies using few paired sim‑and‑real samples together with extensive simulated rollouts. The method corrects bias in simulation labels, calibrates uncertainty via conformal prediction, and achieves significant reductions in scenario‑level prediction error compared to baseline approaches.

## Key Takeaways
- SCAPE reduces scenario‑level prediction error by 4.9% for autonomous driving and 14.5% for quadruped velocity tracking relative to scene‑conditioned baselines.  
- The framework improves testing sample efficiency, producing narrower calibrated prediction intervals that generalize better to out‑of‑distribution scenarios.  
- SCAPE enables fine‑grained deployment strategies by providing scenario‑specific guidance on when and where a policy can be safely deployed.

## Context
The field of robot learning faces a persistent challenge: evaluating policies in real environments is costly while simulation offers scalability but suffers from sim‑to‑real bias. Existing methods often rely on population averages that mask important variability across scenarios, limiting practical deployment decisions.

## Implications
SCAPE’s ability to deliver calibrated, scenario‑specific performance estimates will allow developers to allocate testing resources more efficiently and reduce risk in real‑world robotics deployments. Practitioners can trust predictions for targeted rollouts, accelerating innovation while maintaining safety standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19425v1)
