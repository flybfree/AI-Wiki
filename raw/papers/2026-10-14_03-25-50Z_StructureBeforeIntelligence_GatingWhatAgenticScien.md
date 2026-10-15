---
title: Structure Before Intelligence: Gating What Agentic Scientific Workflows Release
published: 2026-10-14T03:25:50Z
authors: Ashish Acharya, Aman Al Amin, Hong Qin
url: http://arxiv.org/abs/2610.19507v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structure Before Intelligence: Gating What Agentic Scientific Workflows Release

## Abstract
An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release decision. A harness around the workflow's directed acyclic graph (DAG) decides which outputs may be used: it enforces mandatory checks, contains failures to the affected branch, recomputes from tracked versions, adds validators, and releases a result only if a risk model estimates its probability of being invalid as low. Language-model agents work inside the harness, choosing corrective actions and reviewing releases, but cannot override it. On 60 held-out paired instances of two workflows with injected faults, we switched components on and off. Each supplied a different property. Containment and recovery raised the number of correct results. Validation supplied safety: fixed rules without validation released 37 invalid results, while validating every candidate released none. Risk estimation supplied efficiency, matching that safety with 31% fewer validators at somewhat lower yield, although better targeting than random validation was not shown. Lineage evidence helped on one workflow. The language model added no measurable benefit: whether invalid results escaped depended on the harness, not the model. This proof of concept points to a practical path: placing agents inside explicit release-control structure can keep released scientific results trustworthy, and it gives more capable agents a measurable baseline to improve on.

## Metadata
- **Published**: 2026-10-14T03:25:50Z
- **Authors**: Ashish Acharya, Aman Al Amin, Hong Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19507v1)