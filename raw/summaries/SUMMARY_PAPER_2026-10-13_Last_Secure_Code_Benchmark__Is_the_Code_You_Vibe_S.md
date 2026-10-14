---
title: Last Secure Code Benchmark: Is the Code You Vibe Secure?
url: http://arxiv.org/abs/2610.14766v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_09-42-56Z_LastSecureCodeBenchmark_IstheCodeYouVibeSecure.md
generated_at: 2026-10-13 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

The paper introduces the Last Secure Code Benchmark, a comprehensive evaluation framework designed to assess whether AI coding agents produce secure code when tasked with writing functional code without any explicit security instructions. Built from 150 real-world vulnerabilities across seven programming languages and 24 CWE categories, the benchmark tests six frontier AI agents across three "vibe-coding" scenarios. The central finding is stark: while 73.6% to 91.3% of tasks pass functional tests, only 16.4% to 25.1% of generated code is simultaneously functional and secure, revealing a critical gap between code that works and code that is safe.

## Key Takeaways

- The benchmark covers 450 tasks spanning seven widely used languages (Java, C, C++, JavaScript, Python, PHP, and Go), 24 CWEs including 21 of the 2025 CWE Top 25 and 8 of the Top 10 KEV weaknesses, making it the most comprehensive secure code evaluation benchmark compared to prior work. This breadth ensures findings generalize across the languages most commonly used in production software.

- Even the strongest model, Claude Fable 5, produces code that is both functional and secure for only 25.1% of tasks, while other frontier agents achieve between 16.4% and 24.7%. The best model passes only 12% of vulnerability scenarios across all vibe-coding settings, indicating that current AI agents systematically fail to avoid security vulnerabilities when security is not explicitly requested.

- The benchmark deliberately uses specifications that never mention security, grading results with hidden functional and security tests. This design mirrors real-world "vibe coding" workflows where developers ask AI agents to write code for functionality alone, exposing how security vulnerabilities emerge silently in production code shipped by AI agents.

## Context

As AI coding agents increasingly write the majority of code shipped in production software, the assumption that functional correctness implies code safety has become a dangerous blind spot. Prior benchmarks have evaluated security-aware code generation where security constraints are explicitly stated, but this paper addresses the more realistic and concerning scenario where developers request only functionality. The Last Secure Code Benchmark fills a critical gap in the evaluation landscape by testing whether security emerges as an implicit property of AI-generated code, which is the dominant mode of AI-assisted software development today.

## Implications

For industry practitioners and software teams adopting vibe-coding workflows, these findings demand immediate integration of automated security scanning, static analysis, and vulnerability testing into AI-assisted development pipelines, since AI agents cannot be trusted to produce secure code by default. For the AI research community, the results highlight an urgent need to train and evaluate models on security-aware code generation even when security is not explicitly prompted, and to develop benchmarks that test implicit security properties rather than only explicit compliance. The 12% pass rate across vulnerability scenarios suggests that current frontier models require fundamental improvements in understanding and avoiding common software vulnerabilities before their output can be safely deployed in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14766v1)
