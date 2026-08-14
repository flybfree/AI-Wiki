---
title: Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction
url: http://arxiv.org/abs/2608.12426v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_10-57-06Z_LargeLanguageModelsCanFollowInstructions_ButNotMan.md
generated_at: 2026-08-13 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models behave when required to satisfy multiple constraints simultaneously, using a systematic benchmark. It finds that while individual constraint pass rates remain decent, the probability of satisfying all constraints drops sharply as the number of constraints grows. The study also reveals differences in which types of constraints degrade most and explains why failures accumulate multiplicatively.

## Key Takeaways
- Per‑constraint pass rate declines gradually but the chance of satisfying all k constraints collapses, e.g., a model that passes 8 constraints at ~41% succeeds on all eight only about 5.7% of the time.
- Structural constraints lose twice as much baseline capability per added constraint compared to lexical ones, reflecting a comprehension‑maintenance gap for constraints that require sustained tracking versus binary decisions.
- Failures are nearly independent and driven by shared output features rather than pairwise interference, causing multiplicative accumulation of errors.

## Context
Large language models often need to obey several explicit rules at once, such as safety limits and output formats. Understanding the point at which instruction following breaks down is crucial for reliable deployment in complex settings. This work provides a quantitative measure of that threshold using an objective benchmark.

## Implications
For developers, the findings suggest limiting the number of simultaneous constraints to around five or six to maintain acceptable performance. Practitioners should prioritize structural over lexical constraints and design models to share output features across constraints to reduce failure propagation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12426v1)
