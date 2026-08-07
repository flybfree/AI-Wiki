---
title: TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions
url: http://arxiv.org/abs/2608.05975v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_12-53-33Z_TRACE_LearnedProprioceptiveOdometryforLeggedRobots.md
generated_at: 2026-08-06 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TRACE, a learned proprioceptive odometry estimator for legged robots that works when contact is unreliable. It predicts displacement and rotation from IMU and joint data using attention over tokenized inputs. The method is fully end‑to‑end, requiring no handcrafted thresholds.

## Key Takeaways
- The foot‑aware cross‑attention module automatically weights IMU and leg tokens without predefined thresholds, making the estimator robust under slip or loss of contact.
- Direct supervision combined with kinematic consistency and reliable leg information losses trains the network to produce accurate relative pose estimates.
- Policy randomization during simulation training mitigates sim‑to‑real overfitting, enabling effective fine‑tuning of the temporal encoder.

## Context
Learning based odometry for legged robots is crucial because conventional filters fail when contact is uncertain. This work advances perception‑driven navigation by integrating proprioceptive data directly into motion planning pipelines.

## Implications
Robust odometry reduces reliance on external sensors, lowering hardware costs and complexity. Practitioners can deploy more reliable autonomous platforms in real‑world environments where contact conditions vary.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05975v1)
