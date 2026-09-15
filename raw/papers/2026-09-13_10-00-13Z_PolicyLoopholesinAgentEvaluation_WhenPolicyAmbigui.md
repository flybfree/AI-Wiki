---
title: Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error
published: 2026-09-13T10:00:13Z
authors: Hongliu Cao
url: http://arxiv.org/abs/2609.14400v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error

## Abstract
Agent benchmarks evaluate policy compliance but assume each policy determines a unique correct action. Natural-language policies can violate this assumption through silence, ambiguity, or contradiction, admitting multiple defensible readings that a single gold trajectory cannot capture. Auditing two $τ^2$-bench domains, we develop a taxonomy of such policy loopholes and show that affected tasks produce unreliable scores: they lower scores across different models in different ways and make every model less consistent across repeated trials. A cross-domain comparison reveals that exploitability requires both policy ambiguity and tool permissiveness: when policy complexity exceeds what tools can enforce, agents resolve gaps inconsistently and scores become unreliable. Policy specification quality sets the ceiling on evaluation quality. Benchmark developers should audit policies before collecting gold annotations.

## Metadata
- **Published**: 2026-09-13T10:00:13Z
- **Authors**: Hongliu Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14400v1)