---
title: BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence
published: 2026-08-28T14:49:46Z
authors: Changze Li, Yutong Cheng, Tsania Camila Finnisa, Qian Cui, Wei Ding, Peng Gao
url: http://arxiv.org/abs/2608.28394v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence

## Abstract
Cyber threat intelligence (CTI) is foundational to modern cyber defense, yet much of it resides in unstructured reports whose volume and heterogeneity far exceed manual analysis, motivating research on automatically constructing knowledge graphs from CTI reports. However, existing approaches mainly extract partial information within a single report, leaving the cross-source setting unexplored, where the same threat is given unrelated names. Our key insight is that attack behaviors, once mapped to MITRE ATT&CK (a standardized catalog of attack techniques), can anchor the rest of a report. Attack behaviors are the adversarial actions a report describes, while contextual entities (e.g., threat actors, campaigns, and affected products) and Indicators of Compromise (IoCs; e.g., IP addresses) are their participants and traces. Attaching them to these anchors places every per-report graph in one canonical space.   We realize this insight in BEACON, an LLM-driven framework for cross-source CTI knowledge graph construction. Its first stage extracts each report into a graph under a propose-then-verify paradigm, grounding candidates in report evidence and official ATT&CK definitions, to suppress LLM misclassification and hallucination. Its second stage merges these graphs with a hierarchical alignment strategy that applies signals in decreasing order of determinism, from character-level and semantic similarity to overlapping technique neighborhoods, iterating as merges pool neighborhoods. No existing benchmark links entities to technique anchors or provides cross-source alignment ground truth. We therefore construct and release two human-annotated datasets from 34 sources: to our knowledge the largest for report-level CTI extraction (8,395 elements) and the first for cross-source consolidation (3,487). On them, BEACON outperforms all baselines by at least 23% and 9%, respectively.

## Metadata
- **Published**: 2026-08-28T14:49:46Z
- **Authors**: Changze Li, Yutong Cheng, Tsania Camila Finnisa, Qian Cui, Wei Ding, Peng Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28394v1)