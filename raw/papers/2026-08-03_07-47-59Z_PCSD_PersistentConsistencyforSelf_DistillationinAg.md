---
title: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning
published: 2026-08-03T07:47:59Z
authors: Chunji Lv, Yangguang Wei, Junlin Liu, Yang Gao, Ming Liu, Xinming Wang, Jinyang Wu, Guoren Wang, Changsheng Li
url: http://arxiv.org/abs/2608.01837v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning

## Abstract
Large language model agents have shown strong potential in complex interactive tasks, yet their reinforcement learning (RL) is often hindered by sparse rewards, as a long multi-turn trajectory may receive only a single outcome-level signal. On-policy self-distillation (OPSD) provides dense token-level supervision from a privileged teacher, but the teacher may not be reliable at every position. Existing methods commonly rely on isolated token-level discrepancies, which can be sensitive to noise, or assign a shared step-level weight that may overlook positional variation. We propose Persistent Consistency Self-Distillation (PCSD), which derives token-level distillation weights from the local persistence of teacher-favoring signals. PCSD combines adaptive windows with exponentially decayed aggregation to capture persistent relative teacher support, applies trend-aware modulation to attenuate locally declining support, and produces continuous weights through sigmoid gating. The resulting objective is jointly optimized with GRPO, combining dense teacher guidance with sparse environmental feedback. Without inference-time skills, PCSD achieves the best ALFWorld Overall results among all baselines on both backbones, exceeding GRPO by 15.6 and 13.3 points and SDAR by 6.2 and 5.5 points, while remaining competitive on WebShop and gaining 15.8 points over GRPO on unseen ALFWorld split.

## Metadata
- **Published**: 2026-08-03T07:47:59Z
- **Authors**: Chunji Lv, Yangguang Wei, Junlin Liu, Yang Gao, Ming Liu, Xinming Wang, Jinyang Wu, Guoren Wang, Changsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01837v1)