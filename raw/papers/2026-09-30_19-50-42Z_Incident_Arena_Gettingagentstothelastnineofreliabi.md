---
title: Incident-Arena: Getting agents to the last nine of reliability
published: 2026-09-30T19:50:42Z
authors: Andre Fu, Malik Drabla, Leon Liu, Meji Abidoye, Marek Suppa, Lata Mishra, Adnan El Assadi, Yiyuan Li
url: http://arxiv.org/abs/2610.00648v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Incident-Arena: Getting agents to the last nine of reliability

## Abstract
AI coding agents are ubiquitous in engineering workflows amongst industry and academia. Yet, despite their use in app coding, relatively less attention has been paid to their ability to execute on production incident response. This emerging field, termed agentic site-reliability-engineering (SRE) contains benchmarks limited by (1) unrealistic environments, typically toy repositories (2) non-standard framework implementations and (3) simple static verifiers. We introduce Incident-Arena, a human-built benchmark of 20 carefully selected tasks grounded in real-world deployed open source software. Each task deploys a production application to an ephemeral Kubernetes cluster, injecting a fault from the config layer through underlying images, and a sustained load profile given the task requirements. We also present a novel verification method, going beyond static checks to functional verifiers, holding systems level metrics stable, while ensuring repairs are done safely. Agent trials run an average of 2.81M tokens and 41 turns, going beyond existing benchmarks, demonstrating agentic long horizon reasoning. Across 20 tasks and 3 application substrates, frontier models score below 64.3%, with failures extending from diagnosis/localization errors, through incomplete repairs and unsafe regressions.

## Metadata
- **Published**: 2026-09-30T19:50:42Z
- **Authors**: Andre Fu, Malik Drabla, Leon Liu, Meji Abidoye, Marek Suppa, Lata Mishra, Adnan El Assadi, Yiyuan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00648v1)