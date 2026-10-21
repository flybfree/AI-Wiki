---
title: An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context
published: 2026-10-19T22:24:34Z
authors: Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault
url: http://arxiv.org/abs/2610.27347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context

## Abstract
Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignty, carbon impact, compliance, and ethics. The agent relies on a large language model that scores a text on a fixed rubric, grounds its judgment in a reference legal corpus, and, when the score falls at or below a critical threshold, runs a corrective chain made of self-healing rewrites, a compliance label, an explainability report, and escalation to a human reviewer. We describe what the language model does at each step, how the memory of the agent is organized, and how the same implementation can be pointed at different reference corpora. We evaluate the agent in a Canadian and Quebec context, on a corpus of thirteen legal instruments that brings together federal and provincial texts, international treaties, and municipal documents of the City of Trois-Rivières. The evaluation relies on a hand-annotated gold standard of fifteen texts and combines classification metrics, a repeated-query stability test, retrieval precision, and a composite score. On this gold standard the agent separates every conforming text from every non-conforming one, its scores remain stable under repeated queries, and the index returns relevant passages.

## Metadata
- **Published**: 2026-10-19T22:24:34Z
- **Authors**: Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27347v1)