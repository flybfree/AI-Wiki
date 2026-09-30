---
title: Towards Mitigating Deceptive Safety Alignment in Large Reasoning Models
published: 2026-09-28T20:45:10Z
authors: Xiangyu Zhou, Saleh Zare Zade, Rafi Ibn Sultan, Alexander Kotov, Dongxiao Zhu
url: http://arxiv.org/abs/2609.36254v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Mitigating Deceptive Safety Alignment in Large Reasoning Models

## Abstract
Large Reasoning Models (LRMs) are commonly trained with reinforcement learning (RL) to improve their generation of chain-of-thought (CoT) reasoning before producing final answers. However, RL rewards are typically assigned based on final answers, providing little or no direct supervision over intermediate reasoning. This can lead to deceptive safety alignment, where the reasoning trace and final answer convey inconsistent safety signals. To systematically investigate this phenomenon, we introduce DSAR (Deceptive Safety Alignment Rate), a metric that jointly assesses reasoning traces and final answers to quantify their safety inconsistency. Across multiple LRMs and benchmarks, we find that deceptive safety alignment is pervasive under standard prompting conditions and is substantially amplified under prefilling attacks. We further provide a hidden representation analysis showing that models exhibit stronger safety discrimination at the final-answer stage than during intermediate reasoning. To close this gap, we propose SARA (Safety-Aware Reasoning Alignment), an RL-based method that rewards both safety-aware reasoning and safe final answers, encouraging early harmful intent recognition and enforcing reasoning-answer consistency. Experiments show that SARA significantly mitigates deceptive safety alignment under both standard and adversarial settings while preserving helpfulness and utility. Code is available at https://github.com/xzhou98/SARA.

## Metadata
- **Published**: 2026-09-28T20:45:10Z
- **Authors**: Xiangyu Zhou, Saleh Zare Zade, Rafi Ibn Sultan, Alexander Kotov, Dongxiao Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36254v1)