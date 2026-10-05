---
title: Positive-Unlabeled Learning for Agent Safety False Alarm Auditing
published: 2026-10-02T07:16:33Z
authors: Xichen Yan, Chongyang Gao, Kezhen Chen, Guangyi Zhang, Jiaqi Wu, Lixu Wang
url: http://arxiv.org/abs/2610.02925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Positive-Unlabeled Learning for Agent Safety False Alarm Auditing

## Abstract
Safety monitors help safeguard language-model agents interacting with external tools and environments, but conservative monitoring can generate many false alarms, consuming extensive review resources and weakening trust in alerts. Because false and genuine alarms often remain interleaved in native monitor scores, obtaining a reliable cutoff still requires substantial manual verification. In practice, a small set of verified-safe non-alarmed trajectories may be available while alarms remain unlabeled, naturally casting false-alarm auditing as a positive-unlabeled (PU) ranking problem. The key challenge is monitor-induced selection, since observed safe references are accepted by the monitor, while the hidden safe alarms of interest are precisely those it incorrectly flags, making the observed positives poorly representative of the positives to be recovered. To address this challenge, we propose a two-stage framework in which Trust-aware PU Supervision adapts safe references toward the alarm domain and protects plausible false alarms from excessive negative pressure, while Reliability-gated Rank Distillation consolidates consistent ordering preferences from multiple PU reference models into a single student. Consensus-guided Structural Refinement then improves the student ranking using hierarchical safe-reference support, alarm relations, and predicted reference consensus. The framework requires no alarm safety labels for fitting and leaves the underlying monitor unchanged. Across mainstream safety monitors, our method achieves a macro AUPRC of $0.6444$, outperforming eight evaluated PU baselines by 5.27--16.98 absolute percentage points; compared with PULDA, the strongest evaluated PU baseline, it recovers 33.3% more false alarms at a 5% review budget.

## Metadata
- **Published**: 2026-10-02T07:16:33Z
- **Authors**: Xichen Yan, Chongyang Gao, Kezhen Chen, Guangyi Zhang, Jiaqi Wu, Lixu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02925v1)