---
title: Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric
published: 2026-07-26T08:02:20Z
authors: Nikolaos Kekatos, Stylianos Basagiannis, Panagiotis Katsaros, Alexios Lekidis, Tom Nianios
url: http://arxiv.org/abs/2607.23532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric

## Abstract
Swarms of LLM-assisted autonomous robots are increasingly proposed for cooperative intelligence, surveillance, and reconnaissance (ISR) in contested environments. A growing class of their assurance failures arises not within any single platform but across the swarm: individually-compliant actions compose into a mission-level violation: a prohibited objective split across platforms to evade per-platform lim- its, or a collective budget quietly exceeded. Per-platform guardrails miss these by construction, and contested communications let the violation hide behind lost or delayed evidence. We present a three-tier (platfor- m/squad/mission) compositional runtime-verification framework that de- composes a mission policy into per-agent and cross-agent aspects, aggre- gates per-platform verdicts over a verification-aware messaging fabric, and fuses them with an evidence-aware, two-axis (security x complete- ness) algebra whose provenance names the platforms that jointly trig- gered a violation. Because the fabric makes evidence loss and silence observable, unsupported negative verdicts are downgraded to an explicit unknown rather than reported as mission-wide all-clears. On a simulated ISR mission, an indirect prompt injection that causes real LLM planners to split a prohibited collection task across four platforms is invisible to every per-platform monitor yet detected compositionally with full prove- nance; under an injected fault campaign a best-effort central monitor emits silent false all-clears while the verification-aware fabric emits none

## Metadata
- **Published**: 2026-07-26T08:02:20Z
- **Authors**: Nikolaos Kekatos, Stylianos Basagiannis, Panagiotis Katsaros, Alexios Lekidis, Tom Nianios
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23532v1)