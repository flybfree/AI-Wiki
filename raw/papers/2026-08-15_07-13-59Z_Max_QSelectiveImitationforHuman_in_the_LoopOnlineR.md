---
title: Max-Q Selective Imitation for Human-in-the-Loop Online Robot Learning
published: 2026-08-15T07:13:59Z
authors: Zihang Wang, Yishan Wang
url: http://arxiv.org/abs/2608.15088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Max-Q Selective Imitation for Human-in-the-Loop Online Robot Learning

## Abstract
Human-in-the-loop (HIL) online reinforcement learning for real robots must absorb human interventions quickly while continuing to improve beyond the human prior. We present a training method for this setting based on two components. First, an \emph{MC Q-chunk} critic regresses chunk-level action values onto Monte Carlo returns from the replay buffer, performing sample-average (behavior) policy evaluation so that intervention trajectories are credited directly rather than diluted by current-policy TD backups. Second, \emph{max-Q selective imitation} updates the actor by imitating, at each state, the higher-$Q$ action between the current policy action and a buffer sample under a hard winner-take-all rule. This rule automatically switches between learning from interventions and on-policy self-improvement: when the autonomous policy is stronger, targets align with the policy distribution, reducing the policy--target-sample gap that otherwise induces execution-time distribution shift. In practice we score candidates with a standard critic ensemble mean to reduce comparison noise, without softening targets or introducing score-gap thresholds. On a real USB pick-and-insertion task with 20 demonstrations, ACT QChunk-MCBC attains 99\% success within 30 minutes of HIL training, whereas HIL-SERL requires about 5 hours to converge. In simulation on Peg Insertion and Square, ACT/Flow Q-chunk variants similarly reach $\ge$96\% success within roughly half an hour of effective training, outperforming HIL-SERL, EXPO, and E2HiL on the success--time frontier.

## Metadata
- **Published**: 2026-08-15T07:13:59Z
- **Authors**: Zihang Wang, Yishan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15088v1)