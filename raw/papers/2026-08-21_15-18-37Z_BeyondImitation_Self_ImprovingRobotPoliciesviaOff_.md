---
title: Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning
published: 2026-08-21T15:18:37Z
authors: Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg
url: http://arxiv.org/abs/2608.21204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning

## Abstract
Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations. Reinforcement Learning fine-tuning offers a path to self-improvement but has proven difficult to scale to the multi-billion-parameter models underpinning modern robot policies. We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy Q-function. Because a Q-function estimates value rather than imitates actions, it can be trained on the same successful demonstrations as the BC policy and later absorb both successful and failed deployment rollouts, an asymmetry BC does not have. We exploit this asymmetry to enable value-guided action selection at inference (a single-step Q-weighted average over BC draws) and online self-improvement that fine-tunes only the Q-function, leaving the BC weights untouched. On LIBERO and bimanual RoboTwin, ten iterations of self-improvement lift every benchmark score we tested (LIBERO-10 93% to 99%, RoboTwin 83.8% to 91.4%) and shorten successful episodes on the near-ceiling suites (LIBERO-Object, LIBERO-Goal). On two contact-rich bimanual real-robot tasks, the same loop (BC frozen, no human intervention) improves purely from its own deployment rollouts: stack-cups 40% to 90% and insert-wallet 25% to 80% in five iterations, whereas SFT on successful rollouts alone stalls at 55% and 30%. Under an identical online budget Q-Planning is the only method, among Best-of-N, filtered SFT, IBRL, DSRL, and DAWR, that improves stably from failures without training an auxiliary actor.

## Metadata
- **Published**: 2026-08-21T15:18:37Z
- **Authors**: Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21204v1)