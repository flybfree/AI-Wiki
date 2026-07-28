---
title: Invariant Discovery for Networked Systems
published: 2026-07-24T23:07:31Z
authors: Hongyu Hè, Alexander Krentsel, Sylvia Ratnasamy, Maria Apostolaki
url: http://arxiv.org/abs/2607.22944v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Invariant Discovery for Networked Systems

## Abstract
Invariants, the relations expected to hold among measured signals of a network, underpin applications from verification to traffic generation, telemetry imputation, and input validation, yet writing them by hand demands rare expertise in both formal logic and networking. Automatic miners can help but fall short on two fronts: they still require the hardest input (the grammar of admissible invariants) and they learn only exact, ``hard'' rules, struggling with real-world approximation caused by inherent noise in data. LLMs are tools that can provide semantic reasoning over data, but are non-deterministic and opaque in their learning. Our key idea is to partition the invariant search problem into an AI-driven grammar ``discovery'' problem, followed by a statistics-driven ``search'' problem within the learned grammar. Taken together, this allows non-deterministic, hallucination-prone AI to help produce auditable invariants with formal guarantees. We design and implement such a system, Autogram, and evaluate it on both public and production telemetry data, recovering expert-derived invariants with high coverage and low false positives. We close with discussion on open problems on the path toward fully open-ended discovery.

## Metadata
- **Published**: 2026-07-24T23:07:31Z
- **Authors**: Hongyu Hè, Alexander Krentsel, Sylvia Ratnasamy, Maria Apostolaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22944v1)