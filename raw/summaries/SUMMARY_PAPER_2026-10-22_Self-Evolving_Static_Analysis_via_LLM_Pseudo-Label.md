---
title: Self-Evolving Static Analysis via LLM Pseudo-Labeling
url: http://arxiv.org/abs/2610.30184v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-20_10-17-26Z_Self_EvolvingStaticAnalysisviaLLMPseudo_Labeling.md
generated_at: 2026-10-22 22:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SESAA, a framework in which an LLM agent iteratively evolves a set of human-readable joern queries for static analysis, starting from zero rules and refining them through feedback from a second LLM critic that identifies false alarms and missed detections without access to ground-truth labels. On the OWASP Benchmark for Python, SESAA achieves a mean F1 of 0.742 across eight independent runs, surpassing the default configurations of five widely used static analysis tools and matching the performance of the strongest tool once that tool is manually tuned with ground-truth labels. A pilot on real-world Python projects further demonstrates that queries induced from pre-vulnerability code can detect 10 of 19 subsequent CVEs, suggesting the approach generalizes beyond benchmark settings.

## Key Takeaways
- SESAA eliminates the need for manually authored detection rules by having an LLM agent generate and iteratively refine joern queries from scratch, using only a second LLM critic for feedback on flagged and unflagged code. This pseudo-labeling loop replaces the traditional workflow where developers must discover failures and hand-encode new static analysis rules for every new framework, API, or coding idiom.
- The framework achieves a mean F1 of 0.742 on the OWASP Benchmark for Python across eight independent runs, exceeding the default configurations of five widely used static analysis tools. Notably, it matches the performance of the strongest tool only after that tool has been tuned with ground-truth labels that SESAA never accesses, demonstrating competitive detection capability without supervised training data.
- In a real-world pilot, queries induced from code available before a vulnerability was introduced successfully detected 10 of 19 subsequent CVEs, with 9 of those detections coming from rules written for the same repository. The final output is a set of executable, human-readable queries that engineers can independently inspect, modify, and run, preserving auditability and transparency.

## Context
Static analysis tools have long relied on manually curated rule sets that lag behind the rapid evolution of frameworks, APIs, and coding idioms, creating persistent blind spots for security vulnerabilities. This paper sits at the intersection of LLM-driven code understanding and program analysis, proposing a paradigm where rule maintenance becomes an automated discovery-and-repair loop rather than a human authoring task. It contributes to the growing body of work on LLM agents for software engineering by demonstrating that a critic-based feedback loop without ground-truth supervision can produce competitive detection performance.

## Implications
For security engineering and DevSecOps practitioners, SESAA suggests that the costly and error-prone process of maintaining static analysis rules can be substantially automated, reducing the time between a new vulnerability pattern emerging and its detection in CI/CD pipelines. The emphasis on human-readable, auditable joern queries means organizations can retain governance and compliance oversight while delegating rule generation to LLM agents. More broadly, the pseudo-labeling critic loop offers a template for self-improving analysis systems in domains where ground-truth labels are expensive or unavailable, potentially extending to vulnerability detection in other languages and to broader software quality assurance workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30184v1)
