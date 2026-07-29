---
title: Towards an Agent Operating System - Lessons from Classical and Cloud OS
published: 2026-07-27T21:10:59Z
authors: Gosia Steinder, Hubertus Franke
url: http://arxiv.org/abs/2607.25076v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards an Agent Operating System - Lessons from Classical and Cloud OS

## Abstract
Every major wave of platform software follows the same arc: an initial period of experimentation with competing frameworks and ad-hoc implementations, followed by the articulation of a small set of stable abstractions with well-defined semantics, and finally consolidation around those abstractions into a platform that applications can portably target. POSIX did this for classical operating systems; Kubernetes did it for the cloud. Agentic AI systems - autonomous, LLM-driven agents that plan, use tools, maintain memory, and collaborate - are currently in the experimentation phase of the third such wave. dozens of frameworks and protocols have emerged, but no community consensus exists on what the core abstractions are or what guarantees they carry. Without that consensus, agentic applications cannot be written portably, platforms cannot compose reliably, and the field cannot advance beyond prototype deployments. We argue that the path forward is to follow the prior-wave methodology: derive new agentic abstractions by extending classical OS and cloud OS primitives to stochastic, natural-language-mediated execution, specify their semantics precisely, and consolidate around them - just as POSIX and Kubernetes consolidated their respective waves.

## Metadata
- **Published**: 2026-07-27T21:10:59Z
- **Authors**: Gosia Steinder, Hubertus Franke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25076v1)