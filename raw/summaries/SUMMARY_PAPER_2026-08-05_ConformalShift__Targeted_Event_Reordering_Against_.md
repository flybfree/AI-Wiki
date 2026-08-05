---
title: ConformalShift: Targeted Event Reordering Against Adaptive ECG Monitoring
url: http://arxiv.org/abs/2608.03628v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-14-47Z_ConformalShift_TargetedEventReorderingAgainstAdapt.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ConformalShift, a bounded event‑reordering attack that manipulates the timing of authentic ECG events to suppress ventricular class predictions without altering waveforms, labels, classifier scores, or the multiset of events. On MIT‑BIH and INCART datasets, the attack reduced eligible target suppression rates from 4.4 % (Extra Trees) to 66.7 % and from 12.0 % to 60.0 %, demonstrating that adaptive monitors can be compromised solely through event ordering.

## Key Takeaways
- ConformalShift exploits the dependency of adaptive conformal prediction on the order of preceding events, allowing it to lower ventricular thresholds before a target is evaluated without changing any input data.
- The attack achieves high suppression (60–67 %) across two classifiers while keeping all original event attributes intact, showing that timing alone can degrade clinical relevance.
- Reduced displacement budgets weaken the attack, indicating sensitivity to computational constraints and highlighting the need for robust scheduling policies.

## Context
Adaptive conformal prediction aims to provide reliable uncertainty estimates in healthcare AI by reordering events based on classifier scores. This work reveals a vulnerability: the same algorithmic framework can be gamed by adversarial permutations that preserve all observable data, underscoring the importance of considering temporal dynamics beyond static feature sets.

## Implications
For practitioners deploying adaptive ECG monitors, this research calls for safeguards against timing attacks and suggests monitoring not only event content but also scheduling policies. The findings have broader implications for any system where order influences decision quality, prompting a shift toward holistic security assessments that include temporal manipulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03628v1)
