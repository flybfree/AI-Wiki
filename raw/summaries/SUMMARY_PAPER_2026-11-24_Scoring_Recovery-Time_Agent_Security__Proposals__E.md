---
title: Scoring Recovery-Time Agent Security: Proposals, Effects, and Retry Instructions
url: http://arxiv.org/abs/2611.31318v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_07-46-22Z_ScoringRecovery_TimeAgentSecurity_Proposals_Effect.md
generated_at: 2026-11-24 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces an executable evaluation for recovery-time agent security that separately records tool proposals, runtime decisions, and committed effects, rather than judging an agent solely by whether its goal exists. It shows that auditing supplied traces can change apparent completion (10/12 to 8/12), and that original task wording yields only 39/576 valid recoveries when the initial write is absent, versus 576/576 with a combined clarification. The contribution is a measurement design and a diagnosis of availability, specification, and contract sensitivity, not a demonstrated general defense.

## Key Takeaways
- Goal-existence-only evaluation hides harmful recovery actions: auditing 12 supplied traces changes apparent completion from 10/12 to 8/12.
- In 3,456 model episodes, original task wording produced only 39/576 valid recoveries when the initial write was absent, while a combined clarification produced 576/576.
- In a further 1,584 episodes with three rollouts per absent-state cell, separating the effect definition from the recovery recipe shows definition alone yields 276/288 valid recoveries and recipe alone yields 288/288.
- For Luna, malicious text is associated with 11.1 percentage points fewer valid recoveries under both original and definition-only wording, an availability signal limited by shared tasks and templates.
- Stronger attacks produced no attempted unauthorized or changed-key action and no unsafe effect; a trajectory audit found six original-key retries after observing pending status (five denied and one deduplicated).
- Bounded checks distinguish atomic key enforcement from a delayed-commit race, and stale negative reads also invalidate the evidence gate; a separate Claude Code program added 720 successful episodes (288 under the original attacks and 432 stronger-attack calibration episodes across Opus, Sonnet, and Haiku 5.5) with no observed proposal or effect deviations.

## Context
Agentic systems increasingly perform tool writes that may time out and be absent, committed, or still in flight, making recovery behavior security-relevant. Existing evaluations that check only whether a goal exists can mask unsafe or incorrect recovery actions, so there is a need for executable, effect-aware measurement of proposals, runtime decisions, and committed effects.

## Implications
Practitioners should not rely on goal-existence checks alone; recovery-time evaluation should record proposals, decisions, and committed effects separately and test absent-state cells with multiple rollouts. The results diagnose specification and contract sensitivity and an availability signal for Luna, but they do not demonstrate a general defense, so they should be used as measurement guidance rather than proof of robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.31318v1)
