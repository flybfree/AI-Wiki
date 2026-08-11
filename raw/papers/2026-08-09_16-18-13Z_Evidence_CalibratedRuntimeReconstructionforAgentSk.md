---
title: Evidence-Calibrated Runtime Reconstruction for Agent Skills Across Heterogeneous Coding Agents
published: 2026-08-09T16:18:13Z
authors: Xueping Gao
url: http://arxiv.org/abs/2608.08793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Calibrated Runtime Reconstruction for Agent Skills Across Heterogeneous Coding Agents

## Abstract
Agent Skills package reusable instructions and assets for tool-using language-model agents. Progressive loading creates failure boundaries poorly represented by session-, model-, or tool-centric traces: a Skill can be discovered but not activated, activated without instructions, or appear successful without an independently verified outcome. We present Skill Runtime Intelligence, a passive runtime-intelligence system that reconstructs supported Skill-lifecycle stages across heterogeneous harnesses while preserving unsupported stages as unknown. Its Run Panorama separates immutable events, deterministic relations, inferred diagnoses, and controlled outcomes with four evidence grades; optional trace import and OTLP/HTTP export support existing observability deployments.   Across six frozen repository profiles, three coding agents, and seven clean or fault-injected conditions, all 126 executions preserve source worktrees and each correlates to exactly one source session. Yet adapters expose three distinct semantics: no Skill runs; complete runs but no failure-like events; or failure-like events in every operational-failure and clean session. In a seven-template diagnostic study, semantic aliases and Panorama localize the same six non-clean boundaries but differ in exact/status behavior; both Raw views emit a failure status on all 18 clean cases, while Panorama emits none. A known-rule graph conforms to 126/126 frozen contracts, whereas a second model completes only 228/378 calls. These observations motivate executable adapter qualification and show that event presence is not boundary fidelity, composite exact scores mask distinct errors, and model explanations must not overwrite deterministic facts.

## Metadata
- **Published**: 2026-08-09T16:18:13Z
- **Authors**: Xueping Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08793v1)