---
title: From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage
url: http://arxiv.org/abs/2610.10608v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_03-20-51Z_FromInvestigationFailurestoReliableSOCAgents_Under.md
generated_at: 2026-10-08 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why LLM-based agents fail to reliably triage security alerts in Security Operations Centers, studying five representative reasoning strategies across 1,247 alerts from a multi-stage attack scenario. The authors introduce ALERT-BENCH, an interactive benchmark that replays enterprise telemetry through a live SIEM, and demonstrate that all studied approaches miss at least 40.4% of attack-related alerts. They then propose AIDA (Adversarial Investigation and Dialectical Analysis), a multi-agent framework that dramatically improves triage performance, achieving an F1 score of 0.958 and reducing the false-negative rate to 3.1%.

## Key Takeaways
- All five studied LLM triage approaches—single-pass tool use, iterative retrieval, sampled investigations, self-review, and explicit verification—missed at least 40.4% of attack-related alerts, revealing a fundamental weakness in how current agentic systems decide when an investigation is sufficient to close an alert. Trace analysis showed that attack alerts are disproportionately dismissed when searches return no records, that same-context self-review provides negative net correction, and that dismissal receives no consistently stronger investigation than escalation.
- AIDA introduces a structured adversarial workflow: an explicit proposed decision must be challenged by an independent agent in a separate reasoning context, stronger evidentiary requirements are imposed before dismissal, and a separate Judge adjudicates the decision against evidence. An append-only Investigation Ledger preserves full investigation history, preventing agents from losing track of prior findings across reasoning steps.
- On the same benchmark, AIDA achieves an F1 score of 0.958 compared to 0.371–0.744 for the baseline approaches, cutting the false-negative rate from 40.4% to 3.1% while escalating 18.4% of alerts to human analysts. This demonstrates that structuring evidence retrieval and decision review through adversarial multi-agent design can substantially improve agentic SOC triage reliability.

## Context
This work sits at the intersection of agentic AI systems and cybersecurity operations, addressing a critical gap in how tool-using LLM agents handle high-stakes, evidence-dependent decision-making. As SOCs face increasing alert volumes and staffing constraints, the field has rapidly adopted LLM agents for automated triage, yet little research has systematically characterized why these agents fail or what reasoning structures improve reliability. ALERT-BENCH provides a reproducible, interactive evaluation platform grounded in real enterprise telemetry, filling a benchmarking void that has hindered progress in agentic security tooling.

## Implications
For SOC practitioners and security vendors, the findings suggest that simply deploying a single LLM agent with retrieval tools is insufficient for reliable alert triage; adversarial review, explicit decision proposals, and structured evidence requirements are necessary to avoid missing genuine attacks. The 18.4% human escalation rate in AIDA also highlights a practical hybrid model where agents handle routine triage while flagging uncertain cases for analyst review, offering a realistic deployment pathway. For the broader AI research community, the paper demonstrates that multi-agent adversarial architectures with separated reasoning contexts and persistent investigation ledgers can substantially outperform monolithic agent designs in evidence-grounded decision tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10608v1)
