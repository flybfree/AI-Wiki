---
title: What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents
url: http://arxiv.org/abs/2607.22868v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_19-14-26Z_WhatCanBeEnforced_ATheoryofCertifiedRuntimeSafetyf.md
generated_at: 2026-07-27 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a theory of certified runtime safety for tool-using agents that separates three distinct questions about policy enforcement. It shows how deterministic gates enforce only policies recognized by the register model and discusses undecidability and calibration limits.

## Key Takeaways
- A deterministic gate enforces exactly those nonempty safety policies whose good prefixes its register model recognizes, with policy nontriviality being undecidable for two decrementable counters but solvable in PSPACE for a separable monotone fragment.
- Under a fixed exogenous law Neyman-Pearson provides the exact false-block/miss frontier and conformal calibration yields a finite-sample marginal certificate possibly via block-all.
- Once blocking changes future proposals, static scores and ungated trajectories may not identify the closed-loop frontier; instead a specified finite controlled model produces an occupancy program.

## Context
Runtime guardrails are essential for safe AI agents that interact with external tools. This work clarifies theoretical limits of enforcement mechanisms in dynamic environments where policies evolve over time.

## Implications
For practitioners, this theory guides design of safe tool-use frameworks by highlighting when guarantees can be certified and where they cannot. It informs industry efforts to build robust calibration and representation defenses against bounded attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22868v1)
