---
title: Incident-Arena: Getting agents to the last nine of reliability
url: http://arxiv.org/abs/2610.00648v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_19-50-42Z_Incident_Arena_Gettingagentstothelastnineofreliabi.md
generated_at: 2026-10-01 21:14
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Incident-Arena, a human-built benchmark designed to evaluate AI coding agents on production incident response within the emerging field of agentic site-reliability engineering (SRE). Unlike previous benchmarks constrained by unrealistic environments and static verifiers, Incident-Arena employs real-world open-source software deployed in ephemeral Kubernetes clusters with injected faults and sustained load profiles. The study demonstrates that while frontier models exhibit long-horizon reasoning capabilities averaging 2.81 million tokens per task, they achieve scores below 64.3%, revealing persistent challenges in diagnosis, repair completeness, and safety.

## Key Takeaways
- Existing SRE benchmarks are limited by toy repositories, non-standard frameworks, and simple static verifiers; Incident-Arena overcomes these limitations with a benchmark of 20 tasks grounded in real-world deployed open-source software, utilizing ephemeral Kubernetes clusters where faults are injected at the config and image layers under sustained load to simulate production conditions.
- The authors introduce a novel verification methodology that transcends static checks by employing functional verifiers, which ensure system-level metrics remain stable throughout the repair process while guaranteeing that agent actions do not result in unsafe regressions or compromise system integrity.
- Agent trials reveal high complexity with an average of 41 turns and

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00648v1)
