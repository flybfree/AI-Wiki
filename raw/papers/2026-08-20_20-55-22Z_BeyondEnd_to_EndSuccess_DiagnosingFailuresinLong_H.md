---
title: Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents
published: 2026-08-20T20:55:22Z
authors: Wei Shao, Chongzhou Fang, Zuxiong Tan, Zequan Liang, Setareh Rafatirad, Avesta Sasan, Houman Homayoun
url: http://arxiv.org/abs/2608.20563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents

## Abstract
Long-horizon security LLM agents must carry information and decisions across many dependent interactions, where later actions often depend on services, state, or access discovered much earlier. This makes final task success difficult to interpret: an agent may fail before it ever reaches the point where the capability of interest can be exercised. We present a diagnostic methodology that instruments security tasks with checkpoints, separates failures before and after capability exposure, and uses controlled interventions to test suspected upstream bottlenecks. We evaluate the methodology across four task families involving delayed reuse of discovered information, reuse of observed state, recovery from failed strategies, and decision making after uncertain outcomes. On observed state reuse, checkpoint analysis shows that many Gemini 2.5 Flash failures occur before the model observes the state it is later expected to reuse. In a pre-specified 92-seed study, targeted protocol-disambiguation guidance increases state observation from 65.5\% under a matched non-guidance control message to 95.4\%. Repeating the same design with Gemini 3.7 Flash produces the opposite effect, while state observation no longer reliably predicts task completion. These results show that the dominant source of failure can shift across model generations, motivating evaluation that diagnoses where and why long-horizon security agents fail rather than relying only on aggregate task success.

## Metadata
- **Published**: 2026-08-20T20:55:22Z
- **Authors**: Wei Shao, Chongzhou Fang, Zuxiong Tan, Zequan Liang, Setareh Rafatirad, Avesta Sasan, Houman Homayoun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20563v1)