---
title: ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software
published: 2026-09-15T22:23:17Z
authors: Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan, Yuying Zhao, Eugene Siow
url: http://arxiv.org/abs/2609.17885v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software

## Abstract
Computer-use agents that operate through screenshots and simulated actions are advancing rapidly, yet their evaluation remains anchored to general desktop and web tasks. Enterprise Resource Planning (ERP) systems run the finance, procurement, inventory, and customer operations of organizations worldwide, and pose distinct challenges for computer-use agents: dense interfaces, coordinated multi-step interactions, and errors that alter persistent business records rather than surfacing on screen. Existing enterprise benchmarks rely on proprietary platforms or on simulated approximations of such software. We introduce ERPBench, a benchmark that evaluates screenshot-only agents on a live and reproducible ERP system and scores each task against ground-truth values in its database. Beyond the benchmark, we present a production-grade harness that gates agent actions behind human approval for safe deployment, which ERPBench runs autonomously. Evaluating six closed and open-source agents, we demonstrate that strong general GUI performance does not transfer to enterprise reliability. Even when an agent reaches the right form and saves it, the stored record is often wrong: some agents save in up to 85% of runs but write the correct value in as few as 3%. We further characterize failure modes specific to enterprise workflows.

## Metadata
- **Published**: 2026-09-15T22:23:17Z
- **Authors**: Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan, Yuying Zhao, Eugene Siow
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17885v1)