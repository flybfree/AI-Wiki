---
title: More Data, Worse Decisions? Preference Reversals in Neural Networks under Gram Incompatibility
url: http://arxiv.org/abs/2607.27255v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-28_18-52-47Z_MoreData_WorseDecisions_PreferenceReversalsinNeura.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how refitting neural networks on pooled data can reverse the ordering of preferences that were supported by each source, violating compositional reliability in case‑based decision theory. The authors derive exact and approximate conditions under which shared preferences survive union, introduce a scale‑invariant Gram mismatch measure, and propose geometry‑oriented regularization to mitigate reversals.

## Key Takeaways
- Pooled refitting recomputes the inverse‑Gram geometry that weights source evidence, which can flip the ordering of preferences supported by both sources.  
- The paper derives exact and approximate preservation conditions for these preferences when using ordinary least squares output heads.  
- A three‑stage audit is proposed to trace strict pairwise reversals through decision changes and quantify them via a task‑defined utility loss.

## Context
Neural networks increasingly combine data from multiple sources to improve generalization, but this raises concerns about preserving the logical consistency of preferences across those sources. The composition axiom in case‑based decision theory demands that union of source‑supported preferences remains valid, yet current refitting practices often violate it. This work provides a formal framework and practical tools to assess and correct such violations.

## Implications
For practitioners, the findings highlight that pooling data without accounting for geometric compatibility can lead to harmful decisions that appear consistent but are actually inconsistent with source evidence. The proposed audit and regularization methods offer actionable ways to ensure compositional reliability in AI systems used in load‑based bidding, medical diagnosis, and financial trading.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27255v1)
