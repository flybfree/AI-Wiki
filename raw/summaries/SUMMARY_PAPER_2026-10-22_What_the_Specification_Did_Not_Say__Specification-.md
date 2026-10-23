---
title: What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks
url: http://arxiv.org/abs/2610.30635v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_02-56-44Z_WhattheSpecificationDidNotSay_Specification_Oracle.md
generated_at: 2026-10-22 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies and formalizes a critical flaw in coding-agent benchmarks: the "specification-oracle gap," where natural-language task descriptions omit implementation details (such as constant names, module paths, or exact error messages) that the grading tests from upstream projects actually require. The author builds a static audit tool across five programming languages and demonstrates on SWE-Milestone that 25 of 98 graded milestones contain tests depending on unstated, non-inferable identifiers, causing those units to fail in 80.6% of agent runs compared to 48.4% for comparable units without such hidden dependencies.

## Key Takeaways
- The specification-oracle gap is formally defined as the discrepancy between what a benchmark's natural-language description states and what its test suite actually checks. The author builds a static audit tool covering five languages that classifies every name-, path-, and literal-level dependency of every scored test, achieving 89.2% held-out precision and 92.9% recall, providing a reproducible method for auditing any benchmark.
- On SWE-Milestone (98 milestones, 35 published runs), 25 milestones contain at least one test that depends on an unstated, non-inferable name or path. Build units with such a hidden dependency fail in 80.6% of runs versus 48.4% for comparable units without one. Withholding a single hidden name from the reference implementation prevents its unit's tests from compiling in 126 out of 128 cases, showing the gap is not a subtle scoring artifact but a hard compilation barrier.
- The prevalence of the gap is strongly tied to how a benchmark is constructed: a third or more of tasks are affected when specifications are drawn from release notes or LLM-generated summaries, while almost none are affected when tasks are screened or written specifically for their tests. The cost of the gap also depends on the grading harness, meaning benchmark authors have direct control over whether their evaluations inadvertently reward upstream reproduction rather than genuine problem-solving.

## Context
This work sits at the intersection of software engineering evaluation and AI agent benchmarking, a field that has grown rapidly with the deployment of coding agents like SWE-agent, OpenHands, and others evaluated on repositories such as SWE-Bench. As these benchmarks increasingly rely on upstream test suites as ground truth, the assumption that a natural-language task description fully defines the solution space has gone largely unexamined. This paper provides the first systematic, cross-language formalization of that assumption's failure, offering a methodological tool that benchmark designers and agent developers can apply before publishing new evaluation suites.

## Implications
For benchmark practitioners, the audit tool and corrected filter lists released alongside the paper offer a concrete mechanism to detect and remediate specification-oracle gaps before a benchmark is deployed, reducing the risk that leaderboard scores inadvertently reward agents for memorizing upstream identifiers rather than reasoning about code. For the broader AI community, the finding that gap prevalence tracks benchmark construction method (release notes versus purpose-written tasks) suggests that evaluation integrity is a design choice, not an accident, and that agents optimized against such benchmarks may develop brittle name-reproduction behaviors that do not transfer to real-world software engineering where specifications are genuinely underspecified.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30635v1)
