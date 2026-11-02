---
title: Precedent or Intent? What Coding Agents Follow When Evolving Existing Code
url: http://arxiv.org/abs/2610.38244v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_03-50-17Z_PrecedentorIntent_WhatCodingAgentsFollowWhenEvolvi.md
generated_at: 2026-11-01 21:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how coding agents resolve conflicts between existing code patterns (precedent) and new task instructions (intent) when evolving software. Through 5,625 controlled trials across four coding agents and six implementation pairs, the authors demonstrate that agents overwhelmingly defer to repository precedent over their own default preferences, but that written priority rules can effectively override precedent when new intent must take precedence. The study further validates these findings in four real-world open-source repositories spanning three programming languages.

## Key Takeaways
- Agents share identical default implementation preferences across different models, yet when repository precedent conflicts with those defaults, agents follow precedent in 359 out of 360 trials, revealing a near-total deference to existing code patterns regardless of the agent's own tendencies.
- Precedent influence is highly sensitive to spatial and structural context: three supporting local files yield 96% adoption of a pattern, while sibling-resource files produce only 4% adoption, and merely changing file placement can shift adoption from 0% to 100% at a fixed example count, showing that proximity and organizational structure dramatically shape agent behavior.
- When new task intent conflicts with existing code, explicit written priority rules achieve substantially higher success than code examples alone (59/60 versus 38/60 joint successes), and this rule-based approach extends to open-source repositories, where a harness-loaded rule raises joint success from 0/120 to 117/120, demonstrating that explicit rationale documentation is far more effective than implicit pattern-following for guiding agent behavior.

## Context
As coding agents increasingly participate in software evolution tasks—modifying, extending, and refactoring existing codebases—the question of whether they should preserve established patterns or follow new instructions becomes a foundational design challenge. This paper addresses a gap in agentic software engineering research by isolating and measuring the competing influences of default preferences, repository precedents, and explicit task instructions through bidirectional controlled experiments. It contributes to the growing body of work on agent behavior, prompt engineering, and software maintenance automation by providing empirical evidence about how agents actually reason about conflicting guidance sources.

## Implications
For practitioners building agentic coding tools, this research argues strongly for design-decision traceability: repositories should preserve not only implementation choices but also the rationale and priorities behind them, so that agents can distinguish which precedents to follow and which to override. For the broader AI and software engineering community, the findings suggest that relying on code examples alone to guide agent behavior is insufficient and potentially misleading, while explicit written rules and priority documentation offer a far more reliable mechanism for steering agent decisions in complex, multi-file codebases. This has direct consequences for how teams structure documentation, onboarding materials, and agent harness configurations in production software development pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.38244v1)
