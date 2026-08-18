---
title: What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics
published: 2026-08-17T10:21:36Z
authors: Shuyu Liu
url: http://arxiv.org/abs/2608.16370v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics

## Abstract
Task completion is the standard metric for evaluating context compression, yet it is incomplete: compression can increase an agent's interaction cost by forcing it to reacquire dropped state while leaving completion statistically unchanged.   We introduce a controlled runtime measurement protocol for reacquisition cost in a bounded-horizon tool-using agent. The agent acts in a deterministic planning environment under a fixed 24-turn horizon. We vary compression severity, compare a dropping operator with a fact-preserving operator, restore dropped state through controlled oracle interventions, and decompose tool calls into retrieval and execution. We evaluate three models across two task regimes.   Retrieval calls increase in all six model-regime comparisons and account for almost all added interaction; five of six remain significant after Holm correction. At the prespecified 5x comparison point, completion changes are not significant in any cell. DeepSeek shows a significant completion drop only at 10x compression. GPT-5.5 is the clearest case: completion changes from 80% to 85% (p = 1.0) while retrieval increases from 21.0 to 63.9 calls (p = .002).   Retention interventions further separate state quantity, state type, and content validity. Random selection is comparable to an offline hindsight oracle, while replacing retained D-state with semantically irrelevant content increases retrieval by 57% (p < .001) without a significant completion change. In a second environment, ALFWorld, sliding compression produces no retrieval surge, showing that the reacquisition signature is environment-dependent rather than intrinsic to shortening context.   Overall, compression can impose hidden interaction costs when execution-relevant state becomes absent and must be reacquired, while completion alone may not expose those costs.

## Metadata
- **Published**: 2026-08-17T10:21:36Z
- **Authors**: Shuyu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16370v1)