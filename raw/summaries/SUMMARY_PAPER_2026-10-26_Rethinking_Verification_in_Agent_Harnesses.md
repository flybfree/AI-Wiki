---
title: Rethinking Verification in Agent Harnesses
url: http://arxiv.org/abs/2610.34577v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_21-17-26Z_RethinkingVerificationinAgentHarnesses.md
generated_at: 2026-10-26 23:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper systematically studies verification as a test-time scaling axis in agent harnesses, examining when to intervene, who performs the checking, and how checking leads to revision across four layers of the agent lifecycle. Through extensive experiments comparing 17 verification designs across seven frontier coding models on Terminal-Bench, SWE-bench Verified, and a new VisualBench benchmark, the authors find that independent review by a critic offers the most favorable accuracy-cost tradeoff, improving accuracy by 5.9–9.5 percentage points on Terminal-Bench and 3.9–6.6 on SWE-bench at only 1.00–1.25 times baseline cost.

## Key Takeaways
- Initial instructions and execution-time reminders produce only modest, model-dependent gains on coding benchmarks without substantially increasing output token usage, suggesting that lightweight verification interventions embedded in prompts have limited and inconsistent effectiveness across different frontier models.
- Completion gates can yield larger accuracy gains but may substantially increase computational cost, making them a less practical option for production agent systems where cost efficiency is a primary constraint.
- Independent review by a critic agent represents the most promising verification strategy, achieving 5.9–9.5 percentage point improvements on Terminal-Bench and 3.9–6.6 on SWE-bench at near-baseline cost multipliers, while on VisualBench it achieves net preference scores of 13.2–23.8 points over baseline across four designs, surpassing all evaluated lower-level verification approaches. Additional review rounds or multiple independent critics can further improve accuracy by up to 3.5 percentage points.

## Context
As large language models increasingly operate through tool-use agent harnesses that iteratively observe results and revise outputs, the question of how to structure verification within these loops has become a critical open problem in AI systems engineering. This paper addresses a gap in the literature by providing a structured four-layer framework spanning initial instructions, mid-turn reminders, completion gates, and independent review, and by introducing VisualBench to evaluate verification effectiveness on visual and interactive artifacts. It positions verification explicitly as an axis of test-time scaling alongside model scaling and training-time scaling.

## Implications
For practitioners building agent systems in production, this research provides concrete empirical guidance that independent critic review is the most cost-effective verification strategy, enabling meaningful accuracy improvements without prohibitive cost increases. For the broader AI research community, the findings suggest that test-time scaling through structured verification is a viable and practical complement to model scaling, and that agent harness design should treat verification as a first-class architectural concern rather than an afterthought. The introduction of VisualBench also signals a growing need for evaluation methodologies that go beyond code correctness to assess interactive and visual agent outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34577v1)
