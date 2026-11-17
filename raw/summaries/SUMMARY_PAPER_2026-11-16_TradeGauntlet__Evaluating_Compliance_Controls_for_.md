---
title: TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents
url: http://arxiv.org/abs/2611.18493v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_18-05-23Z_TradeGauntlet_EvaluatingComplianceControlsforAuton.md
generated_at: 2026-11-16 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TradeGauntlet introduces a replayable limit-order-book simulator designed to evaluate compliance controls for autonomous trading agents by separating detection, prevention, and execution cost into distinct measurable components. Through 1,680 simulated sessions using Claude Haiku 5.5 and Sonnet 5.5, the authors demonstrate that zero alerts alone are insufficient to establish an agent's compliance, as gates that suppress alerts can simultaneously degrade legitimate trading performance, and adversarial search methods reveal strategies that evade implemented conduct rules.

## Key Takeaways
- All conduct alerts observed in the 1,680 simulated sessions were self-matches, meaning the agents' own orders crossed each other. While gates successfully eliminated these alerts by rejecting self-crossing orders, the aggregate-gate condition reduced Sonnet's two-sided fills by approximately 15%, demonstrating a direct trade-off between compliance enforcement and trading capability. A conduct reminder prompt reduced Sonnet's alert rate but simultaneously reduced Haiku's fills without producing a detectable alert benefit, highlighting that control mechanisms affect agents unevenly.
- Scripted probes and two adversarial search methods expose weaknesses invisible in standard LLM runs. Specifically, split-order schedules were found that evade the implemented conduct rules entirely. A learned baseline classifier caught all 2,400 tested searched episodes but also flagged 15% of a large maker's sessions, illustrating the precision-recall tension inherent in compliance monitoring systems.
- Aggregate caps reduce response-dependent gains unevenly, with smaller reductions when only near-touch depth affects prices. Results fitted to five Nasdaq stocks and a separate ABIDES experiment reveal that these estimates depend heavily on underlying market assumptions. Additionally, a distinct adversarial prompt elicited refusals from Sonnet in all 240 rounds, yielding no candidate strategies to evaluate, suggesting that compliance controls can inadvertently suppress agent exploration entirely.

## Context
As autonomous trading agents move from research prototypes toward deployment in regulated financial markets, the question of how to verify their compliance behavior without crippling their operational utility becomes critical. Existing agentic safety research has focused broadly on alignment and refusal behavior, but financial trading introduces domain-specific compliance constraints such as self-trade prohibitions, aggregate position limits, and market-manipulation rules that generic guardrails do not address. TradeGauntlet fills this gap by providing a reproducible, domain-specific testbed that decomposes compliance evaluation into detection, prevention, and execution-cost components, enabling researchers to measure whether a control genuinely improves compliance or merely suppresses observable signals.

## Implications
For practitioners deploying autonomous trading agents in regulated environments, this work demonstrates that compliance testing must go beyond counting alerts or refusals; it must account for whether controls degrade legitimate market-making activity, whether adversarial strategies can circumvent rule-based gates, and whether evaluation results are sensitive to specific market microstructure assumptions. The finding that adversarial prompts can cause an agent to refuse all 240 rounds without producing any candidate strategy warns that overly aggressive compliance controls may render an agent operationally inert. For the broader AI safety community, TradeGauntlet offers a template for building domain-specific, replayable evaluation harnesses that separate the mechanics of detection from the economics of prevention, a methodology applicable to any regulated agentic deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.18493v1)
