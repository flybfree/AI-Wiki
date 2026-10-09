---
title: Cross-Provider Review as a Runtime Contract for Coding Agents: A Controlled Pilot and Fault-Injection Study
url: http://arxiv.org/abs/2610.10961v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_22-28-22Z_Cross_ProviderReviewasaRuntimeContractforCodingAge.md
generated_at: 2026-10-08 23:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces and evaluates an advisory cross-provider review contract for coding agents that share a workstation but draw on separate provider subscriptions and resource pools. Through a controlled pilot of 20 paired development turns, the authors demonstrate that a second agent from a different provider can produce material findings in a meaningful fraction of cases, while also uncovering critical runtime defects—including false success on truncated input, cancellation during process reaping, and misclassification of reviewer exit status—that undermine the reliability of such review pipelines.

## Key Takeaways
- The authors formalize a "review contract" with seven explicit requirements: distinct resource pools, bounded execution, restricted reviewer capabilities, complete input delivery, usable semantic output, explicit failure states, and durable per-attempt evidence. In their 20-turn pilot, eight turns yielded a material reviewer finding, with a 95% exact confidence interval of 19.1–63.9%, indicating a non-trivial but highly uncertain yield that cannot yet support production gating decisions.
- A boundary-condition scan across both reviewer backends reproduced a previously discovered false-success bug: four truncation levels that had historically passed now failed after repair, and a cancellation defect during process reaping was identified and fixed. Real CLI probes further revealed that Claude lacked writing tools entirely, while Codex attempted writes in five out of five read-only trials, each of which failed—confirming that capability restrictions must be enforced at the tool level, not merely assumed.
- A preregistered shadow study of 25 formal observations uncovered a third defect: a reviewer process that exited with a nonzero status but produced a well-formed verdict was incorrectly counted as a complete review. Because exit status was not recorded per attempt, the authors could not retrospectively resolve the true exposure, forcing them to restart the measurement-valid cohort at zero and treat the original 25 records as an audit cohort only.

## Context
As coding agents from multiple providers increasingly share development environments, the question of whether one agent can reliably audit another's output has become a practical engineering concern rather than a purely theoretical one. This paper addresses the gap between the intuitive idea of "having another model check your work" and the operational reality of resource contention, tool-capability mismatches, and silent failure modes that can make such reviews misleading or vacuous. It contributes to the growing body of work on multi-agent safety, runtime verification, and the operational integrity of agentic tooling pipelines.

## Implications
For practitioners deploying multi-agent coding workflows, this study underscores that cross-provider review cannot be treated as a simple API call; it requires explicit contracts governing resource isolation, input completeness, capability restrictions, and per-attempt telemetry. The discovery that exit status was not logged per attempt—and that a nonzero exit with a valid verdict was silently accepted—highlights a class of silent-failure bugs that could systematically inflate apparent review coverage in production systems. Until measurement-valid cohorts are completed and gate results are reported, teams should treat cross-provider review as an advisory signal with unresolved reliability bounds rather than a safety gate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10961v1)
