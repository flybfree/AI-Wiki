---
title: Cross-Provider Review as a Runtime Contract for Coding Agents: A Controlled Pilot and Fault-Injection Study
published: 2026-10-07T22:28:22Z
authors: Bowen Xu, Boyu Chen
url: http://arxiv.org/abs/2610.10961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Provider Review as a Runtime Contract for Coding Agents: A Controlled Pilot and Fault-Injection Study

## Abstract
Coding agents increasingly share a workstation while drawing on separate providers and subscription allowances. A second agent can inspect a completed answer, but the call spends another pool and may provide no substantive finding. We describe an advisory cross-provider review contract: distinct resource pools, bounded execution, restricted reviewer capabilities, complete input delivery, usable semantic output, explicit failure states and durable per-attempt evidence. In a controlled, agent-authored pilot of 20 paired development turns, eight had a material reviewer finding (95% exact interval 19.1-63.9%). A boundary-condition scan across both reviewer backends reproduced a previously discovered false success on partial input: four truncation levels passed historically and failed after repair. The scan also found and repaired cancellation during process reaping. In real CLI probes, Claude had no writing tools; Codex attempted writes in five of five read-only trials, each write tool failed, and no disposable repository changed. These tests cover specified paths and versions, not field reliability. A preregistered shadow study of metadata-only review allocation accrued 25 formal observations before an exact-runtime regression found a third defect: a reviewer exiting nonzero with a well-formed verdict was counted as complete. Exit status was not recorded per attempt, so exposure cannot be resolved retrospectively. The 25 formal and two pending records remain an audit cohort; the measurement-valid cohort restarted at zero and collection has begun. No gate result is reported.

## Metadata
- **Published**: 2026-10-07T22:28:22Z
- **Authors**: Bowen Xu, Boyu Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10961v1)