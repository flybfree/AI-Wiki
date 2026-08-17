---
title: What preferences can - and cannot - predict in multi-agent online learning
url: http://arxiv.org/abs/2608.13810v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_22-42-53Z_Whatpreferencescan_andcannot_predictinmulti_agento.md
generated_at: 2026-08-16 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how ordinal preference graphs influence the long‑term outcomes of multi‑agent online learning dynamics such as follow‑the‑regularized‑leader. It proves that the skeleton of any dynamically stable set must be preferentially stable and then shows that preferences alone do not guarantee dynamic stability, constructing a counterexample in three players.

## Key Takeaways
- Every dynamically stable set’s preference graph is closed under profitable deviations, meaning it is preferentially stable.
- Preferences can predict asymptotic stability only within subgames where action sets are restricted, but this does not hold for full games.
- A resilience condition based on aggregate payoff changes ensures that any span of pure strategies remains asymptotically stable.

## Context
In multi‑agent online learning the choice of a solution concept determines whether players converge to equilibrium profiles. Understanding which preferences reliably signal stability helps design robust learning algorithms in complex coordination settings.

## Implications
Practitioners can use resilience checks to validate dynamic stability without exhaustive game analysis, improving trust in algorithmic recommendations for distributed decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13810v1)
