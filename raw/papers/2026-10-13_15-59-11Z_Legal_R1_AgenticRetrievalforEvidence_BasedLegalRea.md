---
title: Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning
published: 2026-10-13T15:59:11Z
authors: Huaiwen Pang, Jiale Han, Junying Chen, Wenjun Xiao, Benyou Wang
url: http://arxiv.org/abs/2610.18611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning

## Abstract
Legal question answering requires answers that are not only plausible, but also grounded in legally valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot semantic matching, which is insufficient when legal evidence must be selected according to authority, applicability, and diversity across heterogeneous sources. We introduce Legal-R1, an agentic retrieval framework for evidence-based legal reasoning. Legal-R1 decomposes legal reasoning into a multi-agent workflow, where a Lawyer agent learns when to retrieve, which legal source to query, what evidence to seek, and when the collected evidence is sufficient. A Legal Assistant agent retrieves from normative legal sources and precedent cases with authority-aware and diversity-aware selection, while a Judge agent generates the final answer from the complete evidence trajectory. We post-train only the Lawyer agent with masked supervised fine-tuning and trajectory-aware reinforcement learning. Experiments on multiple Chinese legal benchmarks show that Legal-R1 improves over general-purpose, legal-specific, and retrieval-augmented baselines.

## Metadata
- **Published**: 2026-10-13T15:59:11Z
- **Authors**: Huaiwen Pang, Jiale Han, Junying Chen, Wenjun Xiao, Benyou Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18611v1)