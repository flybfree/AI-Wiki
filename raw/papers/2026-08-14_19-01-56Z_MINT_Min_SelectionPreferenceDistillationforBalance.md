---
title: MINT: Min-Selection Preference Distillation for Balanced Multi-Objective Alignment
published: 2026-08-14T19:01:56Z
authors: Tony Tu, Sayan Chakraborty, Ruomeng Xu, Tony Qin, Austin Tian
url: http://arxiv.org/abs/2608.14828v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MINT: Min-Selection Preference Distillation for Balanced Multi-Objective Alignment

## Abstract
Aligning a language agent to several objectives at once is a persistent failure mode of preference-based training: when objectives are combined additively, optimization collapses onto whichever is cheapest to improve and sacrifices the rest, so a support agent learns to sound warm while giving no real help. The root issue is that an additive reward has no notion of balance. We introduce Mint (MIN-selection preference disTillation), a one-line change to preference distillation: rather than ranking sampled candidates by a weighted sum of rewards, we rank them by their weakest objective, distilling the best-balanced candidate over the most lopsided one with an unchanged DPO objective. This is the p -> negative infinity limit of a generalized-mean family spanning additive to worst-case selection. Across cooperative emotional support and adversarial negotiation, min-selection lifts both objectives while sharply cutting their imbalance; on emotional support it raises the weaker axis from 0.37 to 0.64 (p < 10^-40), surpassing human experts and persisting across full multi-turn rollouts. A turn-by-turn analysis yields our central finding: min-selection corrects imbalance in proportion to how imbalanced the reference policy is, and its benefit endures over an interaction precisely as long as that imbalance does.

## Metadata
- **Published**: 2026-08-14T19:01:56Z
- **Authors**: Tony Tu, Sayan Chakraborty, Ruomeng Xu, Tony Qin, Austin Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14828v1)