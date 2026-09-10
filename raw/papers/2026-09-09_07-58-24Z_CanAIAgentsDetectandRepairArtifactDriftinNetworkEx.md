---
title: Can AI Agents Detect and Repair Artifact Drift in Network Experiments?
published: 2026-09-09T07:58:24Z
authors: Tianzhu Zhang, Weichen Tao, Changgang Zheng, Yusheng Zheng, Long Chen, Xiaoyi Fan, Meikang Qiu
url: http://arxiv.org/abs/2609.09849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can AI Agents Detect and Repair Artifact Drift in Network Experiments?

## Abstract
In recent years, AI agents have evolved into capable assistants that carry out multi-step tasks in digital environments. The network systems community is beginning to explore these capabilities in operational and experimental settings. However, an agent operating in network systems should not be judged solely by whether it completes the immediate task. The experiment record it modifies must also remain trustworthy. We call this property artifact integrity: the record's claims must remain supported by the available evidence, confined to the scope established by that evidence, and traceable through the artifacts that encode their support.   To make this property measurable, we introduce NetArtifactBench, which tests whether AI agents can repair inconsistent records derived from public network-system artifacts while preserving claims that remain supported. The benchmark contains 52 instances with injected inconsistencies ranging from direct contradictions to unstated relations spread across several artifacts. We evaluate 23 agent configurations across three general-purpose AI agent runtimes using deterministic scoring. The average contract pass rate is 65.3 % across 5,980 outputs, but no agent runtime exceeds 30 % when repair requires recovering implicit relations and propagating changes across artifacts. These results reveal a sharp boundary between local correction and complete record-level repair. Therefore, we argue that artifact integrity should become a first-class design and evaluation requirement for AI agents operating on network systems.

## Metadata
- **Published**: 2026-09-09T07:58:24Z
- **Authors**: Tianzhu Zhang, Weichen Tao, Changgang Zheng, Yusheng Zheng, Long Chen, Xiaoyi Fan, Meikang Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09849v1)