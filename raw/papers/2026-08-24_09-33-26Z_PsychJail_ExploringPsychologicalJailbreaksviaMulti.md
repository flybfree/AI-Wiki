---
title: PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies
published: 2026-08-24T09:33:26Z
authors: Zeyu Feng, Qingyu Wu, Yuzhe Luo, Hua Cheng
url: http://arxiv.org/abs/2608.23028v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

## Abstract
Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles-rationalist, credibility-driven, narrative-monoculture, and broadly persuadable-while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

## Metadata
- **Published**: 2026-08-24T09:33:26Z
- **Authors**: Zeyu Feng, Qingyu Wu, Yuzhe Luo, Hua Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23028v1)