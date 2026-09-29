---
title: When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM Agents
published: 2026-09-26T12:03:54Z
authors: Yanjie Zhang, Bowen Cao, Zixin Chen, Yushi Sun
url: http://arxiv.org/abs/2609.32520v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM Agents

## Abstract
LLM agents often operate over multi-turn interactions in which user intent changes before execution. We study intent drift: the failure mode in which superseded parts of the user's intent continue to influence the final answer or tool action. We introduce IntentFlux, an executable benchmark that converts verifiable tasks into dialogues with controlled intent changes while preserving their original graders. In a 627-case calibration, mean task score falls from 0.476 to 0.384 as dialogues contain more superseded and withdrawn information. Across eight models, the rate of fully correct solutions is significantly lower when the same final task must be recovered from an evolving dialogue rather than given directly in a single turn. We further introduce StateForge, which explicitly maintains the active requirements before generation. On General-Test, it improves mean task score from 0.367 to 0.467. Providing the ground-truth final state improves performance further but still does not recover single-turn performance, indicating that state-estimation errors explain only part of the gap. These results establish intent drift as a measurable multi-turn failure mode and explicit state maintenance as a partial mitigation.

## Metadata
- **Published**: 2026-09-26T12:03:54Z
- **Authors**: Yanjie Zhang, Bowen Cao, Zixin Chen, Yushi Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32520v1)