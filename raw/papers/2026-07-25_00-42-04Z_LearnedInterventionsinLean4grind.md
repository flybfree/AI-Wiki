---
title: Learned Interventions in Lean 4 grind
published: 2026-07-25T00:42:04Z
authors: Evan Wang, Simon Chess, Sophie Szeto, Theodore Meek
url: http://arxiv.org/abs/2607.22972v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learned Interventions in Lean 4 grind

## Abstract
Lean~4's \grind{} tactic combines congruence closure, \ematch{}ing, and case-splitting into a single automated solver, and like any such solver, it relies on hand-tuned heuristics to decide what to instantiate and where to case-split. These heuristics are tempting targets for learning, but there is a catch: because \grind{}'s search is non-monotone, a learned heuristic that helps one proof can break another, and an always-on replacement usually nets out near zero. We avoid this by invoking a learned intervention only after stock \grind{} has already failed: a failure-triggered cascade that, by construction, cannot lose a proof \grind{} already had. We apply it to two of \grind{}'s internal decisions. A cost-aware \ematch{} filter solves slightly more problems and runs about 5\% faster. A lookahead step, proves five theorems it otherwise times out on. We also report the negative result that motivated the design: across four feature-based models, statically predicting the correct case split is no better than random, because whether a split explodes is a runtime property that the features do not capture. Our results suggest that learning within theorem-proving tactics is most effective as a mechanism for deciding when and how to spend bounded search, backed by a reliable symbolic fallback.

## Metadata
- **Published**: 2026-07-25T00:42:04Z
- **Authors**: Evan Wang, Simon Chess, Sophie Szeto, Theodore Meek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22972v1)