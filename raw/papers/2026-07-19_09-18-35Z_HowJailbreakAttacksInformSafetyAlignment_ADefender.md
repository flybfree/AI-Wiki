---
title: How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions
published: 2026-07-19T09:18:35Z
authors: Yukai Zhou, Feiyang Lu, Xiaokai Mao, Jinfei Liu, Wenjie Wang
url: http://arxiv.org/abs/2607.17152v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions

## Abstract
Jailbreak attacks on large language models are usually evaluated by attacker-centric metrics such as attack success rate (ASR), yet an attack that breaks a model is not necessarily useful for improving its safety. We propose a defender-centric view of jailbreak evaluation, where attacks are evaluated by the downstream safety improvements they enable when used as red-teaming data for safety training. Building on this view, we introduce A-MESS (Minimal Effective Attack-Subset Selection), a setting-agnostic framework for attributing and selecting jailbreak attacks from black-box subset utility observations. A-MESS estimates AttackSHAP, a Shapley-based score that attributes marginal utility to individual attacks and selects compact attack subsets under user-specified budgets via greedy or surrogate-based optimization. Across controlled utility landscapes and real LLM safety settings, we find that ASR rankings are weakly aligned with defender-centric utility, that AttackSHAP can be estimated accurately with limited utility queries, and that directly optimizing subsets yields stronger safety utility than attacker-centric or attribution-only selection. These results suggest evaluating jailbreak attacks as resources for improving safety, not only as tools for breaking models.

## Metadata
- **Published**: 2026-07-19T09:18:35Z
- **Authors**: Yukai Zhou, Feiyang Lu, Xiaokai Mao, Jinfei Liu, Wenjie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17152v1)