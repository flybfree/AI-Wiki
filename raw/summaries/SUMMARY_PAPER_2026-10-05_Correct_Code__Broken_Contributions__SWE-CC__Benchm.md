---
title: Correct Code, Broken Contributions? SWE-CC: Benchmarking Repository Policy Compliance for Coding Agents
url: http://arxiv.org/abs/2610.06193v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_12-08-33Z_CorrectCode_BrokenContributions_SWE_CC_Benchmarkin.md
generated_at: 2026-10-05 22:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SWE-CC, a benchmark designed to evaluate whether autonomous coding agents comply with repository-specific contribution policies beyond merely passing functional unit tests. The authors construct a semi-automated pipeline that converts developer documentation from 12 open-source repositories into 823 machine-checkable atomic policies, then evaluate four LLMs across 500 end-to-end software contribution tasks. The central finding is that while agents produce functionally correct patches, they violate 43.1 percent of applicable project policies, with nearly half of violations occurring during intermediate execution steps rather than in final deliverables.

## Key Takeaways
- SWE-CC extends evaluation beyond unit-test pass/fail metrics by introducing deterministic checker functions that verify compliance with repository governance rules spanning code style, git workflows, and testing procedures. The benchmark converts human-written developer documentation into 823 atomic, machine-checkable policies across 12 mature open-source repositories, creating a reproducible and auditable compliance framework that existing benchmarks like SWE-bench Verified do not provide.
- The evaluation reveals a critical distinction between functional correctness and real-world merge readiness: agents under two different scaffolds consistently produce patches that pass tests yet violate nearly half of applicable project policies. Crucially, approximately 50 percent of these violations occur during intermediate agent execution steps (such as commit formatting, branch naming, or test placement) rather than in the final code output, meaning that auditing only the final deliverable would miss the majority of compliance failures.
- The paper introduces a comprehensive auditing mechanism that inspects both agent runtime behaviors and final deliverables, demonstrating that process compliance is as important as output compliance. This dual-inspection approach exposes how agent scaffolds and LLM choices influence governance adherence, providing actionable diagnostic information for developers building production-ready coding agents.

## Context
As autonomous coding agents increasingly resolve real-world GitHub issues at scale, the field has relied almost exclusively on functional correctness benchmarks like SWE-bench Verified to measure agent capability. SWE-CC addresses a critical blind spot: mature open-source projects enforce contribution policies to ensure long-term maintainability, code quality, and collaborative workflow integrity, yet no existing benchmark measures whether agents respect these governance rules. This work bridges the gap between academic benchmarking and the practical requirements of open-source maintainers who must review, trust, and merge agent-generated contributions.

## Implications
For practitioners deploying coding agents in production open-source workflows, these findings indicate that functional test pass rates alone are insufficient to guarantee safe and trustworthy integration of agent contributions into maintained codebases. The 43.1 percent policy violation rate suggests that future agent architectures, scaffolds, and training pipelines must explicitly incorporate repository governance constraints into their decision-making processes, and that maintainers should expect to audit agent behavior throughout the execution pipeline rather than only inspecting final patches. This benchmark provides a concrete evaluation tool for developers building agents intended for real-world software engineering deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06193v1)
