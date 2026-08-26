---
title: ReproAgent: Contract-Guided Paper-to-Code Reproduction
published: 2026-08-25T09:19:00Z
authors: Xue Hu, Zewei Pan, Zhongyuan Wang, Zhou Liu, Zeli Su, Wentao Zhang
url: http://arxiv.org/abs/2608.24291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReproAgent: Contract-Guided Paper-to-Code Reproduction

## Abstract
Paper-to-code reproduction asks scientific AI agents to turn research papers into executable repositories that preserve the paper's method, protocol and artifacts. This is difficult because the specification is split: explicit paper content such as algorithms, metrics and artifacts is often lost across long agent trajectories, while implicit details such as framework defaults and conventions inherited from related work are absent from the paper. We introduce ReproAgent, a four-stage Prepare--Plan--Generate--Repair pipeline built around a persistent implementation contract with two channels: an implementation-requirement channel that turns paper snippets into code obligations, and a reference-evidence channel that retrieves content and structure evidence from related repositories. Both are bound to work packages, projected into file-level contracts, and consumed across generation and repair. On PaperBench Code-Dev, ReproAgent reaches the highest mean score among same-backbone scaffolds under both Claude-Sonnet-4.5 and Gemini-3-Flash. End-to-end channel ablations and per-paper cases support the contribution of both channels. Code and experimental artifacts are publicly available.

## Metadata
- **Published**: 2026-08-25T09:19:00Z
- **Authors**: Xue Hu, Zewei Pan, Zhongyuan Wang, Zhou Liu, Zeli Su, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24291v1)