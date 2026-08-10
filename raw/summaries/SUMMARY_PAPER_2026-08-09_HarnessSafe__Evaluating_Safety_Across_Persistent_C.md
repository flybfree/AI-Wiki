---
title: HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses
url: http://arxiv.org/abs/2608.06984v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_09-03-49Z_HarnessSafe_EvaluatingSafetyAcrossPersistentCarrie.md
generated_at: 2026-08-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HarnessSafe, a benchmark that evaluates safety across seven families of persistent carriers in agent harnesses. It demonstrates that attacker influence can propagate through carriers and system boundaries to cause later benign triggers to violate safety constraints. The study shows containment effectiveness varies by carrier and harness configuration.

## Key Takeaways
- Attacker‑influenced content introduced early can persist across multiple carriers, leading to delayed safety violations.
- Containment is not universal; it depends on the specific carrier family and how the harness model is configured.
- Evaluation methods must capture full lifecycle progression rather than just final success rates.

## Context
Agent harnesses that retain state between tasks create opportunities for subtle attacks. Existing safety benchmarks often ignore this cross‑carrier risk, focusing only on isolated carriers or short‑term outcomes.

## Implications
Practitioners need to design containment strategies that account for carrier persistence and configuration quirks. Ignoring these dynamics can lead to false confidence in safety assessments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06984v1)
