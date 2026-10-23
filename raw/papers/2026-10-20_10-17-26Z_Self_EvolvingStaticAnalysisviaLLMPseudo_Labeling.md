---
title: Self-Evolving Static Analysis via LLM Pseudo-Labeling
published: 2026-10-20T10:17:26Z
authors: Rui Melo, Andre Duarte, Aditya Oke, Shubham Gandhi, Nachiket Kotalwar, Rui Abreu, Lei Li, Carolyn Rose
url: http://arxiv.org/abs/2610.30184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Static Analysis via LLM Pseudo-Labeling

## Abstract
Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failures and manually encode new rules. We present SESAA, a framework in which an Large Language Model (LLM) agent starts from no rules and iteratively evolves a set of readable and auditable joern queries.   The agent receives feedback only from a second LLM critic, which inspects flagged and unflagged code to identify likely false alarms and suspected misses, without access to ground-truth labels. The agent then uses this feedback to revise its queries. On the OWASP Benchmark for Python, SESAA reaches a mean F1 of 0.742 across 8 independent runs, well above the default configurations of five widely used tools and comparable to the strongest of them once it is tuned with access to ground-truth labels that SESAA never sees. In a pilot on real-world Python projects, queries induced from code available before a vulnerability was introduced detect 10 of 19 subsequent CVEs, including 9 detected by rules written for the same repository.   The resulting detector is a set of executable, human-readable queries that engineers can inspect, modify, and run independently. These results suggest that LLM agents can turn static-analysis rule maintenance from a manually authored process into an iterative process of automated discovery and repair.

## Metadata
- **Published**: 2026-10-20T10:17:26Z
- **Authors**: Rui Melo, Andre Duarte, Aditya Oke, Shubham Gandhi, Nachiket Kotalwar, Rui Abreu, Lei Li, Carolyn Rose
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30184v1)