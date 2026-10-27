---
title: RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization
published: 2026-10-26T12:16:14Z
authors: Jiawei Lu, Chen Zhang, Jinwei Lu, Yuanwei Song, Yuanfeng Song, Raymond Chi-Wing Wong
url: http://arxiv.org/abs/2610.35316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization

## Abstract
Users often request charts without knowing which database or table holds the relevant data. Such requests may be ambiguous, and users may ask follow-up questions to deepen their analysis or iteratively refine existing charts. A useful assistant must therefore discover relevant data sources among heterogeneous databases, ask clarifying questions when needed, and track evolving user intent while preserving constraints established in earlier turns. Yet recent text-to-visualization agents typically rely on static agent harnesses that are predefined and remain unchanged despite recurring failures across tasks. To address this limitation, we introduce RSIV-Harness, which keeps the language model weights fixed and applies Recursive Self-Improvement to revise the surrounding harness from the agent's own failure traces. To balance flexible self-improvement with stability, we introduce a four-layer framework that evaluates proposed harness revisions through anchor and memory checks, refining those that pass and restoring the best validated harness otherwise. We further introduce ODAC-Vis, a benchmark with 640 tasks for Open-Domain, Ambiguous, and Conversational text-to-visualization that jointly evaluates open-domain data discovery, ambiguity resolution, multi-turn visualization refinement, and executable chart generation. Experiments show that a single round of RSIV-Harness improves all six evaluation metrics relative to the seed harness, with particularly large gains in executability (+28.02 points) and chart structure (+34.01 points), demonstrating the ability to learn from task-solving experience and turn recurring failures across tasks into substantial performance improvements.

## Metadata
- **Published**: 2026-10-26T12:16:14Z
- **Authors**: Jiawei Lu, Chen Zhang, Jinwei Lu, Yuanwei Song, Yuanfeng Song, Raymond Chi-Wing Wong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35316v1)