---
title: Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces
published: 2026-09-21T08:26:07Z
authors: Songqi Li, Dongqing Li, Zheqiao Cheng
url: http://arxiv.org/abs/2609.24264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces

## Abstract
Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry codebook through open induction, recorded consolidation, and successive application audits. Two isolated LLM contexts annotate 32 trajectories disjoint from development at the trajectory level, producing 499 and 491 occurrences with anchor-label overlap A=0.982. Requiring identical context-event references reduces overlap to 0.798. These are structural repeatability measures, not semantic accuracy: 16 of 26 task IDs also occur in development, and historical tool payloads were truncated to 110 characters. Retrospective controls show that collapsing all labels raises overlap to 0.986, while simple endpoint rules reproduce the tool-anchored portion with 0.997 overlap. Assistant-message actions have 0.971 overlap, with a per-label minimum of 0.816. Applying the frozen codebook to 244 further trajectories yields 4,058 records, including eight diagnostic outcomes. The contribution is an explicit, auditable annotation instrument and a case study of its construction and measurement limits; human-reference validity and downstream utility remain to be established.

## Metadata
- **Published**: 2026-09-21T08:26:07Z
- **Authors**: Songqi Li, Dongqing Li, Zheqiao Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24264v1)