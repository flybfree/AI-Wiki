---
title: EmoS: A Theory-Grounded Framework for Evaluating and Aligning Emotional Intelligence in Spoken Language Models
published: 2026-08-10T06:58:30Z
authors: Junyu Wang, Siyuan Zhang, Peiyuan Jiang, Jian Zong, Jingyu Zhang, Tianrui Wang, Yuqin Lin, Zhenghui Chen, Shuqing Xie, Ziyang Ma, Meng Ge, Xiaobao Wang, Longbiao Wang, Jianwu Dang
url: http://arxiv.org/abs/2608.09189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EmoS: A Theory-Grounded Framework for Evaluating and Aligning Emotional Intelligence in Spoken Language Models

## Abstract
Despite significant advances in instruction-following and auditory comprehension, the evaluation of Emotional Intelligence (EI) in Spoken Language Models (SLMs) remains confined to rudimentary paralinguistic perception, lacking a systematic, theory-driven cognitive framework. We introduce EmoSBench, the first comprehensive EI evaluation benchmark for SLMs constructed upon the four-branch theoretical model, covering Perceiving, Understanding, Using, and Managing Emotion across ten sub-tasks. Preliminary assessments on EmoSBench reveal a substantial gap: even leading proprietary models like GPT-4o-Audio achieve only 52.6%, significantly trailing human baselines. To bridge this gap, we develop EmoS, a specialized evaluator model optimized via Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO). To facilitate its effective training, we curate EmoDialogue, a bilingual dataset providing necessary fine-grained supervision through response pairs with rigorously defined EI gradations. Concurrently, we introduce a reward mechanism integrating a Steep Exponential Accuracy Reward (SEAR) and a Rationale Fidelity Reward (RFR) to enforce precise ordinal scoring and valid reasoning. Experiments demonstrate that EmoS reaches 83.8% accuracy, approaching human-level performance. Furthermore, evaluations on authentic, unconstrained spoken interactions validate its robust real-world generalization, establishing a foundational framework for advancing emotionally intelligent dialogue systems.

## Metadata
- **Published**: 2026-08-10T06:58:30Z
- **Authors**: Junyu Wang, Siyuan Zhang, Peiyuan Jiang, Jian Zong, Jingyu Zhang, Tianrui Wang, Yuqin Lin, Zhenghui Chen, Shuqing Xie, Ziyang Ma, Meng Ge, Xiaobao Wang, Longbiao Wang, Jianwu Dang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09189v1)