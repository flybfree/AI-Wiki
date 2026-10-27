---
title: iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents
url: http://arxiv.org/abs/2610.34735v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_02-35-41Z_iPrefBench_AUser_CentricBenchmarkforPersonalizedMo.md
generated_at: 2026-10-26 23:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
iPrefBench introduces a user-centric benchmark designed to evaluate whether personal mobile-use agents can correctly handle underspecified user requests by inferring missing information from activity history and asking users for information that only they can provide. The benchmark comprises 130 underspecified tasks across 26 iOS apps grounded in a coherent persona with 3,051 past activity events, and evaluation of seven frontier agents reveals a substantial gap between task execution capability and personalization, with agents achieving up to 91.6% action completion but only up to 47.7% full task success due to failures in personalization and asking behavior.

## Key Takeaways
- iPrefBench constructs each omitted user-dependent requirement as either history-inferable or ask-only, creating a principled framework for testing whether agents can distinguish between information they should infer from a user's 3,051-event activity history versus information that genuinely requires asking the user. This binary design isolates the core personalization challenge: knowing what to infer and when to ask, rather than conflating execution skill with user understanding.
- Frontier agents demonstrate a critical failure mode: they achieve high action completion scores (up to 91.6%) but low full task success (up to 47.7%), revealing that current agents can execute fully specified tasks well but struggle dramatically when tasks are underspecified. They especially fail at ask-only information, not requesting enough necessary user input, which means agents make unsupported assumptions rather than engaging the user in a productive dialogue.
- The benchmark evaluates two distinct dimensions simultaneously—personalized task completion and user-agent interaction quality—through an executable iOS environment with an interactive simulated user. This dual evaluation framework exposes that agents which perform well on one dimension (executing actions) can fail catastrophically on the other (seeking appropriate user input), highlighting that personalization is not a byproduct of execution capability.

## Context
This paper addresses a fundamental gap in the AI agent research landscape: while computer-use agents have demonstrated impressive capability in executing fully specified tasks across applications, real-world user interactions are inherently underspecified and require agents to reason about individual user preferences, history, and context. iPrefBench fills a critical evaluation void by providing the first benchmark that systematically tests personalization through the lens of inference versus asking, moving beyond generic task completion metrics toward measuring whether agents truly know their users and collaborate with them appropriately.

## Implications
For practitioners building personal assistants and mobile agents, these findings signal that execution benchmarks alone are insufficient for predicting real-world deployment success, and that significant engineering effort must be dedicated to calibrating when an agent should infer from history versus when it should ask the user, avoiding both unsupported assumptions and excessive questioning. For the broader AI research community, iPrefBench provides a reproducible testbed that can drive progress toward agents that genuinely act on behalf of specific users, with direct implications for product design in consumer AI assistants where user trust depends on agents correctly navigating the boundary between autonomy and collaboration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34735v1)
