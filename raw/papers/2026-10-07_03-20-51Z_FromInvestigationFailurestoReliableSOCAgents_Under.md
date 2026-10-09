---
title: From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage
published: 2026-10-07T03:20:51Z
authors: Saimon Amanuel Tsegai, Alex Kantchelian,  Danfeng,  Yao, Peng Gao
url: http://arxiv.org/abs/2610.10608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage

## Abstract
Security operations centers (SOCs) must triage large volumes of alerts, most of which are benign, while missed attacks can remain uninvestigated. Tool-using large language model (LLM) agents can retrieve evidence during triage, but it remains unclear how reasoning strategies determine what to gather and when an investigation is sufficient to close an alert. We study five representative approaches spanning single-pass tool use, iterative retrieval, sampled investigations, self-review, and explicit verification. To support this study, we build ALERT-BENCH, an interactive benchmark that replays enterprise telemetry through a live SIEM and requires each system to retrieve evidence. Across 1,247 alerts from a multi-stage attack scenario, every approach missed at least 40.4% of attack-related alerts. Trace analysis shows that attack alerts are more likely to be dismissed when searches return no records, same-context review has negative net correction, and dismissal receives no consistently stronger investigation than escalation. Based on these findings, we further design AIDA (Adversarial Investigation and Dialectical Analysis), a multi-agent framework that requires an explicit proposed decision before independent challenge and stronger evidentiary requirements before dismissal. AIDA preserves investigation history in an append-only Investigation Ledger and keeps the challenge in a separate reasoning context. A separate Judge adjudicates the proposed decision and challenge against evidence, resolving the alert or requesting another round when evidence is missing. On the same alerts, AIDA achieves an F1 score of 0.958, compared with 0.371-0.744 for the studied approaches, and reduces the false-negative rate from 40.4% to 3.1% while escalating 18.4% of alerts to analysts. These results show that structuring evidence retrieval and decision review can substantially improve agentic SOC triage.

## Metadata
- **Published**: 2026-10-07T03:20:51Z
- **Authors**: Saimon Amanuel Tsegai, Alex Kantchelian,  Danfeng,  Yao, Peng Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10608v1)