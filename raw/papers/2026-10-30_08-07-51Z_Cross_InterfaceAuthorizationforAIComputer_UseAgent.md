---
title: Cross-Interface Authorization for AI Computer-Use Agents
published: 2026-10-30T08:07:51Z
authors: Genliang Zhu, Chu Wang
url: http://arxiv.org/abs/2610.41397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Interface Authorization for AI Computer-Use Agents

## Abstract
Computer-use agents act through graphical interfaces, command lines, APIs, scripts, and Model Context Protocol servers. A policy decision can be interface-invariant while its executable authorization is not: another route can bypass mediation, alter a security-relevant default, or commit after the authorized state has changed. We present a profile-bounded protocol for a fixed, versioned computer-use deployment. It enumerates effect-bearing routes and durable sinks, checks a route-to-sink enforcement cut, normalizes each concrete request to a canonical effect, issues a route-bound prepare ticket, and verifies the route, effect, grant, trace, profile, inventory, and authoritative state again at commit. A committed result requires an agreeing sink receipt. Under explicit assumptions, we prove profile-bounded refinement, matched-effect decision invariance, resistance to alternate-route laundering and declared cross-surface recomposition, commit-time state safety, and receipt-grounded outcomes.   The reference profile registers 12 effect families, five interfaces, and 60 routes. Two structurally distinct runtime mappings produce 3,464 traces over 1,732 scenarios each: 960 commits, 2,312 denials, and 192 commits after re-preparation. An independent checker accepts every retained trace and pair and rejects 26/26 semantic regressions; coverage and normalizer suites reject 24/24 and 720/720 mutants; and 168/168 commit probes match their declared outcomes. A frozen-source audit passes 52 checks over 12 files from two independent hybrid runtimes and one public authorization substrate. Source-shaped adapter refinements commit 48/48 instrumented calls and reject 15/15 unbound cases. The resulting guarantees bind the declared profile and its effect semantics.

## Metadata
- **Published**: 2026-10-30T08:07:51Z
- **Authors**: Genliang Zhu, Chu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.41397v1)