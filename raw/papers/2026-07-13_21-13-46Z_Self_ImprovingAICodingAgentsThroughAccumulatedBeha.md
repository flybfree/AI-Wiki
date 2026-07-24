---
title: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework
published: 2026-07-13T21:13:46Z
authors: Aditya Aggarwal, Nahid Farhady Ghalaty
url: http://arxiv.org/abs/2607.13091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework

## Abstract
LLM-based coding agents repeat the same classes of mistakes across sessions because they lack a mechanism to retain corrections from human review feedback. We present a closed-loop framework in which every accepted review comment is codified as a persistent behavioral rule, progressively expanding the set of error classes the agent can self-detect. The framework combines an accumulating rule set in a version-controlled instruction file, a self-review checklist executed before code submission, and automated validation that ensures rule set integrity as it grows. In deployment across a 35+ service microservices platform, the rule set grew from 5 to 18 behavioral rules, 15+ language-specific standards, and a 15-item self-review checklist, all derived from real review feedback. We present empirical results from 11 recorded working sessions spanning code generation, PR review, incident investigation, and cross service refactoring. We observe that accumulated rules shift review effort from low-level correctness toward design-level validation, achieve a measured 0% recurrence rate for ruled-against error classes, and transfer across heterogeneous agent interfaces. We compare our approach against related work in experiential LLM learning (Reflexion, ExpeL, Voyager) and automated code review (CodeReviewer, SWE-bench agents), showing that our framework achieves persistent cross-session learning without weight updates, operates on production codebases rather than synthetic benchmarks, and addresses an orthogonal dimension (behavioral consistency over time) that existing benchmarks do not measure. The result is a coding agent that improves with every review cycle, accumulating the engineering wisdom of its human collaborators without changing a single model weight.

## Metadata
- **Published**: 2026-07-13T21:13:46Z
- **Authors**: Aditya Aggarwal, Nahid Farhady Ghalaty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.13091v1)