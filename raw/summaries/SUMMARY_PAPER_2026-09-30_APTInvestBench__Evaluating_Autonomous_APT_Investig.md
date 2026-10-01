---
title: APTInvestBench: Evaluating Autonomous APT Investigation under Varying Telemetry
url: http://arxiv.org/abs/2609.38954v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_04-21-45Z_APTInvestBench_EvaluatingAutonomousAPTInvestigatio.md
generated_at: 2026-09-30 20:50
model: qwen3.6-35b-a3b
---

## Summary
APTAInvestBench is a novel benchmark designed to assess the cross-telemetry robustness of autonomous LLM agents investigating Advanced Persistent Threats, revealing that aggregate performance metrics often mask significant instability in citation support when log collection conditions change. While agents can recover evidence for 44.3% of attack actions on average, formal citations are provided for only 25.0%, and transitions to reduced telemetry can cause substantial losses in citation reliability despite the underlying data remaining accessible.

## Key Takeaways
- The benchmark comprises 370 cases across seven SOC-inspired conditions derived from 16.4 million log records, utilizing fixed action-level support requirements to rigorously distinguish between genuine telemetry limitations and agent failures in evidence acquisition or report generation with record-level citations.
- Evaluation of eleven LLMs demonstrates a critical gap between evidence recovery and reporting accuracy, as agents achieve sufficient evidence for less than half of recoverable actions while formal citations support only one-quarter of these findings across diverse frameworks.
- The study exposes hidden fragility where aggregate coverage remains stable under telemetry shifts; for example, moving to endpoint-only logs caused a negligible 1.6 percentage point drop in overall coverage but resulted in 35.5% of covered actions losing sufficient citation support even when evidence was still recoverable.

## Context
As security operations centers increasingly integrate LLM agents into their workflows for threat investigation, it is essential to validate that these systems maintain reliability under the variable and often imperfect telemetry conditions found in real-world deployments. This research advances AI evaluation methodologies by shifting focus from static accuracy benchmarks to dynamic robustness testing, ensuring that agent performance does not degrade unpredictably when log retention, sampling, or collection mechanisms vary.

## Implications
Industry practitioners should avoid relying solely on aggregate

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38954v1)
