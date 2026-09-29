---
title: PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety
published: 2026-09-28T06:30:49Z
authors: Ding Jia, Wei Liu, Xianglong Du, Yingjie Li, Yingqing Yang, Huili Yu, Zhangsong Zhan, Chu Zhou
url: http://arxiv.org/abs/2609.34415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety

## Abstract
The transition from Large Language Models (LLMs) to agents shifts safety stakes from toxic text to irreversible environmental harm. While current defenses remain largely retrospective, proactive runtime intervention is bottlenecked by the lack of large-scale, causally-consistent data. We propose PROACT-Agent, a framework for synthesizing high-fidelity trajectories to enable real-time guardrails. We identify a critical "safety drift" in prior benchmarks, where lenient annotation paradigms fail to enforce temporal consistency. PROACT-Agent addresses this through: (1) Progressive Trajectory Unrolling to reveal risks hidden in long-context interactions; (2) Reasoning-Augmented Causal Rectification to enforce monotonic causal consistency; and (3) Culturally-Aware Data Localization for cross-border robustness. We introduce PROACT-Bench, a bilingual safety benchmark with 155,780 states labeled through multi-model adjudication. Evaluating updated context before the next LLM inference, the trained guard achieves 91.46% unsafe-class F1 and 90.63% exact-boundary detection under complete source holdout. In AgentDojo, it reduces non-DoS targeted attack success from 20.82% to 0.40%.

## Metadata
- **Published**: 2026-09-28T06:30:49Z
- **Authors**: Ding Jia, Wei Liu, Xianglong Du, Yingjie Li, Yingqing Yang, Huili Yu, Zhangsong Zhan, Chu Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34415v1)