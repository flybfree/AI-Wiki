---
title: AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation
published: 2026-10-05T15:08:14Z
authors: Jiaqi Xue, Yanjun Wang, Xiangci Li, Lingbo Mo, Aritra Sengupta, Shweta Garg, Murali Krishna Ramanathan, Myeongsoo Kim
url: http://arxiv.org/abs/2610.06481v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation

## Abstract
As AI agents increasingly tackle complex repository-level coding tasks, distributing work across multiple agents is a natural way to scale beyond the capabilities of a single agent. To coordinate their interdependent work, these agents share findings and agree on interfaces between modules. However, exchanged information often serves only as context, leaving individual agents to interpret it and incorporate it into subsequent work. Consequently, shared findings may go unused and deviations from interface agreements may go undetected, undermining the reliability and efficiency of collaboration. This motivates moving part of the coordination responsibility from individual agents to the execution harness. To make shared information actionable during execution, we introduce the Artifact-Exclusive Communication Protocol (AECP). AECP requires agents to communicate exclusively through structured artifacts and specifies how the harness processes them. The harness supplies findings when agents access relevant code, screens implementations for mismatches with recorded interface commitments, and requires affected agents to revisit revised agreements. These coordination steps become part of harness execution rather than actions that agents must initiate from prior messages. Across Doc2Repo, NL2Repo, and CodeProjectEval, using closed- and open-source models including Opus-4.8 and DeepSeek-V4-Flash, AECP improves average test pass rate by 28.2% and reduces average wall time by 16.5% relative to an agent team using free-form inter-agent messages. Artifact-exclusive communication also blocks the relay of malicious instructions between agents, reducing how often they reach other agents from 95% to 0% and how often those agents act on them from 40% to 0%.

## Metadata
- **Published**: 2026-10-05T15:08:14Z
- **Authors**: Jiaqi Xue, Yanjun Wang, Xiangci Li, Lingbo Mo, Aritra Sengupta, Shweta Garg, Murali Krishna Ramanathan, Myeongsoo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06481v1)