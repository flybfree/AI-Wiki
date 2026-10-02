---
title: Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents
published: 2026-09-30T19:13:16Z
authors: Katrina Drozdov, Oliver Chen, Langston Nashold, Rayan Krishnan
url: http://arxiv.org/abs/2610.00609v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents

## Abstract
Legal research is a core and time-consuming legal workflow. Lawyers must identify controlling authority, verify that it remains valid, reconcile statutes and cases, and synthesize a grounded answer. Language model agents are a natural fit for this retrieval-intensive workflow, and automating even part of it would be valuable. But that value depends on reliability: a single missing authority, stale citation, or wrong legal conclusion can make an otherwise plausible answer unusable. We introduce \textbf{Legal Research Bench} (LRB), a benchmark of 413 open-ended U.S. legal research questions written by experts, each paired with a gold answer, supporting authorities, and a binary grading rubric. We evaluate thirteen frontier models in a harness with web search, case-law search, page parsing, and retrieval tools. We score agent responses through all-pass grading with source verification, where a response is correct only if every required criterion is satisfied and its cited authorities verify. We also validate the LLM judge against expert attorneys ensuring that benchmark scores track attorney judgment. Agents remain far from reliable: among the models we tested, the strongest, Claude Opus 4.8, is fully correct on 42.9\% of questions. Performance also varies substantially by task setting: all-pass rates differ across areas of law and are lower on questions requiring reconciliation of conflicting authorities. Across models, more turns, tool calls, and inference cost do not predict higher accuracy.

## Metadata
- **Published**: 2026-09-30T19:13:16Z
- **Authors**: Katrina Drozdov, Oliver Chen, Langston Nashold, Rayan Krishnan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00609v1)