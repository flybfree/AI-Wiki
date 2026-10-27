---
title: SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments
url: http://arxiv.org/abs/2610.34535v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_19-49-40Z_SentryBench_ACost_SensitiveBenchmarkforAdversarial.md
generated_at: 2026-10-26 23:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SentryBench introduces a cost-sensitive benchmark that evaluates adversarial robustness of tool-using LLM agents in public-safety deployments, where erroneous tool calls carry asymmetric real-world consequences. The paper demonstrates that naive caution strategies (refusing more aggressively) drive over-refusal to 100 percent on two of three frontier models while yielding only a marginal 3.7-point improvement in attack success, producing the worst overall harm, whereas a targeted trust-gating wrapper dominates the safety frontier across all tested models.

## Key Takeaways
- Existing agent-safety benchmarks implicitly treat refusal as the safe default, but in public-safety deployments an agent too cautious to dispatch help fails as surely as one triggering a false alert; SentryBench scores agents on a two-sided frontier jointly measuring attack success, over-refusal (missing a real emergency), and over-reaction (unwarranted action), grounded in real emergency-call transcripts, disaster messages, and real injection/jailbreak payloads.
- The authors formalize deployment harm as an asymmetric cost functional and prove that naive caution is harm-dominated whenever it refuses more genuine emergencies than the attack harm it averts, while also proving that a targeted trust gate adds zero over-refusal on clean input, establishing a theoretically grounded defense strategy.
- Across 840 scored episodes spanning three frontier models and three defenses, refuse-more caution strategies drive over-refusal to 100 percent on two of three models for at most a 3.7-point change in attack success and yield the worst harm everywhere, while the trust-gating wrapper achieves the lowest harm on every model, keeps over-refusal at or below baseline, and provides higher containment; additionally, provider content filters silently perform part of the defending and must be reported separately to avoid conflating model-level and infrastructure-level safety.

## Context
This paper addresses a critical gap in AI safety evaluation: as LLM agents are increasingly wired to consequential tools such as emergency dispatch systems, public alert senders, and citizen-record databases, the stakes of adversarial attacks shift from abstract text manipulation to tangible public-safety harm. Traditional benchmarks that measure prompt-injection success or generic harm fail to capture the asymmetric cost structure of these deployments, where both false positives and false negatives carry severe consequences. SentryBench fills this gap by grounding evaluation in real-world emergency scenarios and formalizing a cost-aware scoring framework.

## Implications
For practitioners deploying LLM agents in public-safety, healthcare, or emergency-response pipelines, this work demonstrates that simply increasing refusal thresholds is counterproductive and can eliminate the agent's ability to act on genuine emergencies entirely. The trust-gating approach offers a practical, theoretically justified defense that preserves agent utility while containing adversarial attacks, and the finding that provider content filters silently contribute to defense performance means that organizations must audit and report infrastructure-level filtering separately from model-level robustness to avoid overestimating their own safety engineering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34535v1)
