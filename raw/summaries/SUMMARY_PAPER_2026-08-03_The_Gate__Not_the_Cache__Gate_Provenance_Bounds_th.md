---
title: The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping
url: http://arxiv.org/abs/2608.00391v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_01-59-12Z_TheGate_NottheCache_GateProvenanceBoundstheClosed_.md
generated_at: 2026-08-03 23:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the source of a gate signal affects closed-loop reliability in training-free vision‑language‑action (VLA) models that use token skipping. It shows that when gates are harvested from previous accelerated steps, tokens skipped at one step become least visible to later gates, causing performance collapse even though the skip ratio is high. The authors introduce an actuation‑slack refresh mechanism that supplies a clean gate and fresh key‑value base between steps, restoring reliability while preserving speed.

## Key Takeaways
- At a 0.9 skip ratio on LIBERO‑Object, using self‑harvested gates causes collapse to 0.31 performance versus dense 1.00, indicating that the mechanism (reuse or deletion) matters less than gate provenance.
- The damage is invisible to action‑level detectors because it occurs before detection thresholds are crossed.
- An unconditional actuation‑slack refresh repairs both mechanisms, recovering to near‑dense speed (0.98) and reducing latency by 18–22 % compared with dense execution.

## Context
Training‑free acceleration in VLA systems relies on token skipping guided by gates, yet the reliability of closed‑loop control is often overlooked. This work highlights that the provenance of gate signals—whether computed from a fully dense forward or from an accelerated one—can silently degrade performance across episodes.

## Implications
Practitioners can integrate actuation‑slack refresh into existing caching and pruning pipelines to maintain high inference speed without sacrificing task success, especially in real robotics where latency is critical. The insight that gate origin, not token skipping itself, governs reliability offers a universal fix for any training‑free VLA deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00391v1)
