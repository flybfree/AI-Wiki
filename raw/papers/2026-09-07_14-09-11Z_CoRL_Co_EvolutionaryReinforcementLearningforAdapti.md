---
title: CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses
published: 2026-09-07T14:09:11Z
authors: Boyang Zhang, Qingxin Xiao, Lingwei Dang, Qingyao Wu
url: http://arxiv.org/abs/2609.07529v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses

## Abstract
Tool-augmented language agents are vulnerable to indirect prompt injection (IPI). Unlike direct prompt injection, IPI hides adversarial instructions in untrusted tool outputs and can covertly alter the execution of a legitimate task. Defenses trained on fixed attacks may fail as an attacker changes its strategy, injection site, and payload. To address this problem, we formulate adaptive IPI as an asymmetric, partially observable, general-sum Markov game: a multi-turn attacker adapts payloads at reached tool-return sites from the public trajectory, while a tool-using defender must block the injected objective and complete the user task. We propose CoRL, a verifier-grounded co-evolution and repair framework with three stages: Attacker SFT initializes multi-turn attacks from successful trajectories; bilateral Co-PPO jointly trains both agents with role-specific rewards and historical opponent populations; and Defender SFT consolidates verifier-accepted teacher repairs for population-discovered failures. Across 1,514 clean, fixed-template, and adaptive executions per defender, CoRL reduces overall ASR by 38.5 points to 0.0% and raises utility by 13.1 points to 76.3%. Stage-wise and controlled ablations show positive contributions from online Co-PPO and population-mined repair, while external-benchmark evaluation indicates transfer in attack resistance. The defender balances safety and task utility under the evaluated attacks, while the retained attackers provide candidates for adaptive red-team evaluation.

## Metadata
- **Published**: 2026-09-07T14:09:11Z
- **Authors**: Boyang Zhang, Qingxin Xiao, Lingwei Dang, Qingyao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07529v1)