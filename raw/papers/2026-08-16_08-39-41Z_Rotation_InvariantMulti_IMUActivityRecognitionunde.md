---
title: Rotation-Invariant Multi-IMU Activity Recognition under Independent Per-Location Orientation Shifts
published: 2026-08-16T08:39:41Z
authors: Seungyeol Baek, Yoonbyung Chai, Yonghyeon Lee, Sungjoon Choi, Sungho Suh
url: http://arxiv.org/abs/2608.15621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rotation-Invariant Multi-IMU Activity Recognition under Independent Per-Location Orientation Shifts

## Abstract
Human Activity Recognition (HAR) with self-administered wearables, such as at-home rehabilitation and exercise monitoring, often requires reattaching inertial measurement units (IMUs) across sessions. In multi-IMU settings, this can induce independent orientation offsets across body locations, a deployment shift that conventional scalar HAR models do not structurally handle. Existing remedies rely on rotation augmentation, whose robustness depends on sampled transformations, or calibration and orientationnormalization pipelines requiring additional reference-frame assumptions or explicit procedures. We present Truly Rotation-Invariant HAR (TRI-HAR), a rotation-invariant framework that makes robustness to independent per-location IMU orientation offsets a structural model property. TRI-HAR reshapes accelerometer and gyroscope streams into triaxial vectors, applies a shared SO(3)-equivariant backbone and invariant projection to each IMU location, and fuses the resulting invariant features for activity classification. Across four multi-IMU benchmarks, TRI-HAR preserves macro-F1 under fixed independent per-location SO(3) rotations and outperforms rotation-augmented baselines under this target shift without requiring rotational augmentation.

## Metadata
- **Published**: 2026-08-16T08:39:41Z
- **Authors**: Seungyeol Baek, Yoonbyung Chai, Yonghyeon Lee, Sungjoon Choi, Sungho Suh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15621v1)