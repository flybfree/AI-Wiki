---
title: Artifact-centered Claim-aware Observability for Autonomous Scientific Agents
published: 2026-08-18T20:47:24Z
authors: Xiangyu Yin, Ming Du, Michael H. Prince, Mathew J. Cherukara
url: http://arxiv.org/abs/2608.18312v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Artifact-centered Claim-aware Observability for Autonomous Scientific Agents

## Abstract
Autonomous scientific agents now increasingly propose ideas, write code, run experiments, analyze results, and even draft papers. Observe and audit those agents are necessary but logging every model call is not enough, scientists also need to inspect the artifacts and claims that the systems produced and their relations. This is driven by the fact that failures in scientific agent systems are often distributed across several objects. A manuscript claim may cite the wrong evidence, a search process may select a degenerate candidate, a laboratory novelty claim may depend on an unstated rule, or a multi-agent plan may change without a visible trigger. Existing tracing, experiment tracking, and archival provenance tools are valuable, but their native objects do not make these scientific audit relations first-class. We argue that autonomous scientific systems should emit portable, claim-aware artifact lineage as a minimum audit layer. We propose a compact observability profile organized around individuals, operators, fitness records, lineage, archives, runs, streams, and steering commands. In this profile, scientific claims are ordinary individuals with explicit evidence bindings and verification records. The profile is intended as a semantic layer that complements current telemetry and provenance standards. Execution details can remain in OpenTelemetry. Final packages can export to PROV-O or RO-Crate standards.

## Metadata
- **Published**: 2026-08-18T20:47:24Z
- **Authors**: Xiangyu Yin, Ming Du, Michael H. Prince, Mathew J. Cherukara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18312v1)