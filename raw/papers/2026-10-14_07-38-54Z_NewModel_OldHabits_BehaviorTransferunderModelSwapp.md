---
title: New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents
published: 2026-10-14T07:38:54Z
authors: Youngbin Choi, Sehyun Hwang, Suhyeon Jun, Seoyeon Lee, Sunghyun Choi, MoonJeong Park, Dongwoo Kim
url: http://arxiv.org/abs/2610.19712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents

## Abstract
Multi-session agents can switch between LLMs to balance performance and inference cost. Such switches require transferring a history for continuity, yet their effects on the recipient remain underexplored. Through controlled experiments with multi-session tasks, we uncover behavior transfer: recipients tend to adopt reasoning and action patterns from the models that generated their histories. This effect is most evident with raw-history transfer but is substantially reduced by summarization. Based on these findings, we propose Direction- and Authorship-aware Summarization of History (DASH) that preserves stronger-model behavior while minimizing weak-to-strong transfer via summarization. Experiments with repeated swaps show that DASH outperforms raw-history transfer and naive summarization baselines. These results suggest that effective multi-model orchestration requires considering not only which model to use, but also which behavioral patterns to carry forward.

## Metadata
- **Published**: 2026-10-14T07:38:54Z
- **Authors**: Youngbin Choi, Sehyun Hwang, Suhyeon Jun, Seoyeon Lee, Sunghyun Choi, MoonJeong Park, Dongwoo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19712v1)