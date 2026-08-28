---
title: Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper
published: 2026-08-27T04:24:29Z
authors: Rongjin Li, Yuanxin Liu, Hao Zhou, Fandong Meng, Jie Zhou, Xu Sun
url: http://arxiv.org/abs/2608.26596v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper

## Abstract
Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or evidence. However, existing work provides limited task paradigms or training studies for such issue- and evidence-absent verification. We study this challenge through scientific error detection, where models must determine whether errors exist and justify them with evidence-based reasoning. To fill this gap, we present VERA-RL, a reinforcement-learning formulation for scientific error detection over academic papers. Following a Reason--Verify--Scan progression, we construct VERA-13K, a 12,900-sample dataset organized into 4,300 matched chains, covering 6 scientific-error categories across the research workflow and broad natural-science domains. We further introduce fine-grained rewards for reasoning completeness, evidence alignment, and error precision. Training Qwen3-VL-8B with VERA-RL substantially improves verifiable reasoning, approaching flagship MLLMs such as Gemini 3 Pro and Qwen3-VL-235B-A22B on Scan.

## Metadata
- **Published**: 2026-08-27T04:24:29Z
- **Authors**: Rongjin Li, Yuanxin Liu, Hao Zhou, Fandong Meng, Jie Zhou, Xu Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26596v1)