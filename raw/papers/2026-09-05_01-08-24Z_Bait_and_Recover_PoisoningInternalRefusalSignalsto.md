---
title: Bait-and-Recover: Poisoning Internal Refusal Signals to Defend LLMs against White-Box Editing Jailbreaks
published: 2026-09-05T01:08:24Z
authors: Tian Gao, Zhipeng Xie, Yuhao Wu, Junhua Liu, Xin Fang
url: http://arxiv.org/abs/2609.05794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bait-and-Recover: Poisoning Internal Refusal Signals to Defend LLMs against White-Box Editing Jailbreaks

## Abstract
Open-weight large language models face a low-cost white-box threat from representation engineering attacks. Attackers can estimate refusal directions and search for projection-matrix edits that suppress safety alignment while preserving general capabilities, within minutes on a single GPU and without gradient-based training. We propose Bait-and-Recover, a weight-level defense that places a bait adapter where attackers read activations and a paired recovery adapter at the subsequent layer. Trained via gradient routing, this decouples the observation path from the behavior path. By actively poisoning the residual signal used for measurement, Bait-and-Recover disrupts the attacker's edit search, while the recovery layer restores clean downstream computation. Across four open-weight models, our defense raises the minimum refusal rate against white-box edit searches from 16.25% to 71.75% under a strict behavior-preservation budget (KL <= 0.10), with negligible impact on general benchmarks. By invalidating the core measurement assumption of these attacks, observation-path poisoning offers a practical complement to behavior-level safety training.

## Metadata
- **Published**: 2026-09-05T01:08:24Z
- **Authors**: Tian Gao, Zhipeng Xie, Yuhao Wu, Junhua Liu, Xin Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05794v1)