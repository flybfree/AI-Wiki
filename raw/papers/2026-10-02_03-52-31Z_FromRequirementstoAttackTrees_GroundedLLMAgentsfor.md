---
title: From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review
published: 2026-10-02T03:52:31Z
authors: Akash Iyer, Taha Demirkan, Keerthi Koneru, Aaryan Siddharthan, Sheethal Kumar, Ramesh Radhakrishnan
url: http://arxiv.org/abs/2610.03820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review

## Abstract
Design-level security weaknesses can arise from requirements, trust assumptions, missing controls, and data flows before implementation begins. Existing security practices often identify these issues after code is written. We present a multi-agent LLM framework for design-time security analysis from product requirement documents and architecture diagrams.   The proposed framework parses architecture diagrams into graph representations, generates misuse and failure cases, constructs attack trees, checks governance and compliance gaps, recommends mitigations, assigns enterprise security-domain tags, and produces a candidate revised architecture recommendation for expert review. The framework does not retrieve from Common Weakness Enumeration (CWE) databases at inference time. Instead, it analyzes system behavior, trust boundaries, component interactions, and data-flow assumptions. Misuse cases act as intermediate representations that link findings to system components and attack paths, while a validation and refinement loop filters unsupported findings and improves grounding, traceability, and actionability.   We evaluate the framework on a Microsoft reference-labeled threat-modeling example, labeled synthetic PRD--architecture pairs, and two open-ended systems: Berty and Gas Town. The reference-labeled case supports threat-recovery and actionability analysis, while the open-ended cases evaluate validity, noise, traceability, actionability, redundancy, and attack-tree quality. Results show that architecture-informed, misuse-driven reasoning improves review quality compared with single-shot and ablation baselines.   Keywords: LLM Multi-Agent Systems, Design-Time Security, Threat Modeling, Vulnerability Discovery, Architecture Diagrams, Security Analysis, Misuse Case Derivation, Attack Trees, Iterative Reasoning, Security Governance.

## Metadata
- **Published**: 2026-10-02T03:52:31Z
- **Authors**: Akash Iyer, Taha Demirkan, Keerthi Koneru, Aaryan Siddharthan, Sheethal Kumar, Ramesh Radhakrishnan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03820v1)