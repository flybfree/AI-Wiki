---
title: AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies
published: 2026-08-07T10:14:29Z
authors: Jinhe Tang, Weiming Zhi
url: http://arxiv.org/abs/2608.07065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies

## Abstract
Action-chunking visuomotor policies learn from demonstrations and improve temporal consistency by predicting short action sequences rather than single-step commands. Yet perception errors and execution drift can move the robot outside the demonstration distribution, while the policy continues to produce smooth action chunks that are inconsistent with the observed state. We present AutoIntervene, an online framework that selectively transfers control between an action-chunking policy and an operator during deployment. AutoIntervene evaluates proposed chunks against a visual-action support memory built from successful task executions, combining visual similarity with consistency between proposed and reference actions. Phase-local support governs policy-to-operator transfer within the current task phase, whereas global support governs the return to policy control after operator recovery. We calibrate separate switching thresholds for the two directions from empirical quantiles of evaluation-level scores on held-out expert demonstrations, avoiding direct manual tuning of score cutoffs. Intervention segments retained from successful rollouts target learner-induced states and provide corrective supervision for subsequent policy updates. Experiments on real-world bimanual manipulation tasks show higher post-adaptation task success and lower operator-control time than manual intervention. Videos and additional results are available at https://aus.bot/research/autointervene/.

## Metadata
- **Published**: 2026-08-07T10:14:29Z
- **Authors**: Jinhe Tang, Weiming Zhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07065v1)