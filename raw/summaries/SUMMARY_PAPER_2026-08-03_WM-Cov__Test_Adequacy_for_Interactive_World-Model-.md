---
title: WM-Cov: Test Adequacy for Interactive World-Model-Style Autonomous Driving Simulation
url: http://arxiv.org/abs/2608.00298v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_21-16-20Z_WM_Cov_TestAdequacyforInteractiveWorld_Model_Style.md
generated_at: 2026-08-03 23:45
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WM-Cov, a provider‑agnostic evaluation layer that transforms raw outputs from interactive world‑model simulations into valid evidence for autonomous driving testing. The study demonstrates that dangerous rollouts can be misleading and that adequacy should be measured by convergence of valid closed‑loop evidence rather than raw failure counts.

## Key Takeaways
- Dangerous-looking events may include valid ADS failures, duplicates, partial realizations, or artifacts, so coverage alone is insufficient for testing adequacy.  
- The DriveArena matrix produced 304 fully realized attempts and 56 partial ones, showing that only a subset of generated evidence meets the required validity criteria.  
- Valid‑evidence precision and failure‑mode diversity are essential metrics to ensure that interactive world‑model testing converges under budget constraints.

## Context
The rise of generative simulators creates an interactive testing paradigm where rollouts depend on the planner, challenging traditional fixed‑trajectory evaluation methods. This work addresses the need for a principled adequacy framework in this evolving landscape.

## Implications
Practitioners can rely on convergence of valid evidence to decide when to stop testing, reducing waste and improving safety validation. The methodology offers a scalable standard for evaluating world‑model‑style autonomous driving simulations across diverse environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00298v1)
