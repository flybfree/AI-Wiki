---
title: VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities
url: http://arxiv.org/abs/2609.08040v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_22-52-09Z_VEX_Bench_BenchmarkingLLMAgentsforAssessingExploit.md
generated_at: 2026-09-08 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
VEX‑Bench is the first benchmark that evaluates LLM agents on assessing whether known software supply chain vulnerabilities are exploitable in downstream projects. The study contains 75 real‑world cases from Python, Java and Go repositories and tests nine models using three agent harnesses. While binary exploitability classification reaches about 80 % F1, only GPT‑5.5 exceeds 70 % macro‑F1 for fine‑grained justification.

## Key Takeaways
- VEX‑Bench introduces a benchmark that measures LLM agents’ ability to reason across repositories and determine if an upstream vulnerability can be exploited in a downstream codebase.
- Binary exploitability classification scores around 80 % F1, showing agents can generally identify vulnerable dependencies but still struggle with nuanced reasoning.
- Fine‑grained justification classification remains below 70 % for most models except GPT‑5.5, highlighting the gap between simple pass/fail answers and detailed explanations.

## Context
The rapid rise of large language model agents in cybersecurity suggests they could automate vulnerability assessments, yet existing benchmarks focus on zero‑day detection rather than supply chain security. VEX‑Bench fills this niche by providing a realistic dataset that tests reasoning across codebases, which is essential for evaluating agent usefulness beyond novelty.

## Implications
This benchmark will guide researchers and practitioners toward agents that not only detect vulnerabilities but also articulate why they are exploitable, improving trust in automated security tools. For industry users, reliable fine‑grained assessments can reduce false positives and streamline remediation workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08040v1)
