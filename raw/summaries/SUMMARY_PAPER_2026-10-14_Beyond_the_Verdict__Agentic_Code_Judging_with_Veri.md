---
title: Beyond the Verdict: Agentic Code Judging with Verifiable Feedback
url: http://arxiv.org/abs/2610.18760v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_17-22-58Z_BeyondtheVerdict_AgenticCodeJudgingwithVerifiableF.md
generated_at: 2026-10-14 02:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the challenge of verifying and diagnosing code correctness in competitive programming without consuming official submission budgets. The authors formulate a novel task where a model judges and diagnoses candidate programs using only the problem statement and source code, generating counterexamples as checkable evidence. They introduce USACO-JUDGE, a benchmark built from USACO 2026 contests, and train ARBITER, a 35B mixture-of-experts agentic verifier using reinforcement learning in a generic execution sandbox, achieving substantial improvements in both verdict accuracy and counterexample generation.

## Key Takeaways
- The authors construct USACO-JUDGE from USACO 2026 contests, incorporating accepted and unaccepted programs written by human experts and multiple LLMs, creating a rigorous evaluation benchmark for code judging tasks that require models to diagnose failures without access to official judge feedback or failing test inputs.
- ARBITER, a 35B mixture-of-experts agentic verifier trained with reinforcement learning in a generic execution sandbox, improves counterexample success on incorrect programs from 40.61% to 62.67% and raises mean binary verdict accuracy on USACO-JUDGE from 71.41% to 87.41%, approaching frontier verification performance without consuming official submissions.
- Beyond static verification, ARBITER demonstrates practical utility in test-time scaling workflows: it outperforms baselines in both code selection and refinement, and in an IOI 2026 case study, ARBITER-guided refinement elevates GPT-OSS-120B's expected score above the gold-medal threshold under the official submission limit, demonstrating real competitive programming impact.

## Context
Test-time scaling strategies for large language models, such as generating multiple candidate solutions for selection or iteratively revising earlier attempts, depend critically on reliable verifiers that can estimate correctness and explain failures. In competitive programming, official judging systems provide only binary verdicts under finite submission budgets, creating a gap between the information needed for effective selection and revision and what is actually available. This paper bridges that gap by treating code judging as a standalone agentic task where the model must independently produce diagnostic evidence, positioning verification not as a passive check but as an active reasoning process that can guide downstream generation and refinement pipelines.

## Implications
For practitioners building LLM-based code generation systems, this work demonstrates that trained agentic verifiers can serve as practical substitutes for expensive human review or costly official judge submissions, enabling more efficient test-time scaling loops in competitive programming and software engineering. For the broader AI research community, the approach of training verifiers with reinforcement learning in execution sandboxes and using generated counterexamples as checkable evidence offers a generalizable recipe for building self-improving code pipelines, potentially extending to automated software testing, debugging assistance, and curriculum design for training future code-specialized models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18760v1)
