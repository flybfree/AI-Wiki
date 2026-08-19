---
title: Digital Twin-Based Intrusion Detection for Vehicle Powertrain CAN Bus Systems
published: 2026-08-17T20:00:21Z
authors: Araf Rahman, M Sabbir Salek, Mashrur Chowdhury
url: http://arxiv.org/abs/2608.17093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Digital Twin-Based Intrusion Detection for Vehicle Powertrain CAN Bus Systems

## Abstract
Existing automotive intrusion detection systems (IDSs) for the Controller Area Network (CAN) largely target discrepancies in message timing, frequency, or sequencing and cannot detect attacks that preserve these properties while manipulating the payload. Digital twins (DTs) have been used to emulate CAN traffic and generate attack scenarios for IDS evaluation, but their use for intrusion detection remains unexplored. This study develops a DT-based IDS that jointly models physical relationships among decoded powertrain signals and identifies attacks through residuals between predicted and observed behavior. A shared-encoder LSTM DT was trained on 17 decoded signals from a real Hyundai/Kia CAN log to jointly predict seven numeric and two categorical gear signals over a 24-step window. A timestep is flagged when a residual exceeds a calibrated threshold, while adaptive rollout protects the twin's input history from sustained contamination. Four attacks (plateau, continuous drift, masquerade, and gear masquerade) were evaluated against the twin and a range-and-plausibility baseline. The DT outperformed the baseline across all attacks, achieving detection rates of 94.6% for continuous drift and 89.2% for masquerade, while the baseline detected almost none of the fabricated payload attacks. These results demonstrate that learning coupled vehicle dynamics enables detection of stealthy payload manipulations that preserve normal CAN communication patterns. False positive rates reached 39.6%, highlighting the need for improved robustness under sustained attacks. The DT-based IDS shows promise for detecting stealthy payload-level CAN attacks that preserve normal communication patterns, supporting behavior-based cybersecurity for connected and automated vehicles.

## Metadata
- **Published**: 2026-08-17T20:00:21Z
- **Authors**: Araf Rahman, M Sabbir Salek, Mashrur Chowdhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17093v1)