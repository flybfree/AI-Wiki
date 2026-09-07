---
title: Rhythms of Work: Multi-Scale Interpretation of Human Behavioral Traces for Workplace Agents
published: 2026-09-03T23:22:27Z
authors: Lin Ai, Scott Counts
url: http://arxiv.org/abs/2609.04556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rhythms of Work: Multi-Scale Interpretation of Human Behavioral Traces for Workplace Agents

## Abstract
Runtime traces are becoming a central substrate for understanding agentic systems, yet interpretation has focused largely on what the agent did. Workplace agents face the complementary problem: interpreting the human activity that surrounds them. Hours of low-level events carry rich evidence about a user's state but are too granular to reason over directly, and flattening them into one stream or compressing them into a single embedding both treat "summarize the user's behavior" as if it had one correct answer. We argue instead that behavioral interpretation is resolution-dependent: the same trace should admit multiple addressable interpretations at different temporal resolutions. We construct a multi-resolution vocabulary of semantically normalized operators, recurring motifs, coherent episodes, and day-level rhythms, each preserving the structure salient at its own horizon. Applied to 667 million human-attributed events from a large commercial productivity suite (50,000 users, 100 organizations), it yields 120 operator types, thousands of motifs, 25 episode types, and five day-rhythm archetypes. We validate it on real telemetry: re-running the entire pipeline on a disjoint 2,000-user sample recovers the same taxonomy (structural stability), and on held-out users the full representation forecasts a user's next episode more accurately than a flat-operator baseline, a 17% relative macro-F1 gain (predictive validity), so the abstractions preserve future-relevant information rather than merely describe it. A controlled resolution ablation then shows that no single level is optimal across questions: different agent-facing questions about the same trace are best answered at different resolutions. Behavioral trace interpretation for agents should therefore be multi-resolution and query-conditioned: an agent should access the temporal grain a question needs, not one universal summary.

## Metadata
- **Published**: 2026-09-03T23:22:27Z
- **Authors**: Lin Ai, Scott Counts
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04556v1)