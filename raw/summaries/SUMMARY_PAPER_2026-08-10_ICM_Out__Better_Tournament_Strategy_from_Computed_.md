---
title: ICM Out! Better Tournament Strategy from Computed Continuations, vs. Solvers and LLMs
url: http://arxiv.org/abs/2608.09586v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_13-20-36Z_ICMOut_BetterTournamentStrategyfromComputedContinu.md
generated_at: 2026-08-10 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Strategic-Continuation Optimization (SCO) to improve tournament strategy beyond the standard Independent Chip Model by modeling action order and elimination pressure. It demonstrates that analytic ICM pricing yields a policy with lower value error than fixed‑ICM benchmarks in a three‑player jam/fold game.

## Key Takeaways
- SCO enumerates current‑hand outcomes, maps them to successor states, prices those states with continuation values from the finite tournament model and optimizes a frozen current‑hand policy. - The fixed‑ICM comparison only changes the pricing function; all else stays the same. - Analytic ICM reduces mean absolute value error to $9,036 across 2,838 state–seat entries.

## Context
Tournament strategy often relies on ICM which treats chips as static reference equity and ignores dynamic factors such as action order and seat rotation. This limitation can lead to suboptimal decisions that affect long‑term prize equity in complex games.

## Implications
For practitioners building AI agents for poker or other chip‑based tournaments, the paper shows that relying solely on ICM may underestimate true value of aggressive moves. Integrating continuation‑aware optimization is essential for robust policy design and competitive advantage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09586v1)
