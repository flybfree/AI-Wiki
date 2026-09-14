---
title: A Graph-Based Approach for Mapping Kernel-Level Telemetry to MITRE ATT&CK
published: 2026-09-11T13:35:27Z
authors: Matteo Lupinacci, Luigi Arena, Francesco Blefari, Angelo Furfaro
url: http://arxiv.org/abs/2609.12841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Graph-Based Approach for Mapping Kernel-Level Telemetry to MITRE ATT&CK

## Abstract
Mapping observed system behavior to standardized frameworks like MITRE ATT&CK is essential for threat-informed defense, but remains largely manual. Existing automated methods depend on Cyber Threat Intelligence reports, which offer only retrospective accounts of attacks. Low-level telemetry, i.e. kernel-level system calls, instead provides evidence of adversary behavior, yet its volume and complexity have limited its use for automated mapping. We present a methodology that collects kernel-level events via eBPF, correlates attacker commands into a provenance graph, and derives compact graph representations suitable for LLM-based reasoning. These representations are mapped to the MITRE ATT&CK framework using both pure LLM prompting and retrieval-augmented generation (RAG) grounded in the ATT&CK knowledge base, producing ranked technique candidates along with supporting rationales. We implement this methodology as an end-to-end pipeline, named Trace2ATT&CK and evaluate it on 347 Linux Atomic Red Team tests using locally deployed open-weights LLMs. RAG consistently improves ATT&CK mapping performance over pure prompting, while provenance graph substantially outperforms raw telemetry. These results show that local inference over graph-based behavioral descriptions can make automated ATT&CK mapping from kernel-level telemetry operationally viable, without compromising data confidentiality.

## Metadata
- **Published**: 2026-09-11T13:35:27Z
- **Authors**: Matteo Lupinacci, Luigi Arena, Francesco Blefari, Angelo Furfaro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12841v1)