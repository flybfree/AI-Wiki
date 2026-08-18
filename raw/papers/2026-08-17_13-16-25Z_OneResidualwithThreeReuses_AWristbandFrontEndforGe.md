---
title: One Residual with Three Reuses: A Wristband Front End for Gesture Sensing
published: 2026-08-17T13:16:25Z
authors: Sam Rifaki
url: http://arxiv.org/abs/2608.16542v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Residual with Three Reuses: A Wristband Front End for Gesture Sensing

## Abstract
Continuous wrist-worn hand sensing for gesture interfaces and motor symptom monitoring needs an always-on front end that fits inside a coin-cell power budget while pairing a micro-electro-mechanical-systems (MEMS) inertial measurement unit (IMU) with a 60 GHz frequency-modulated continuous-wave (FMCW) radar to stay robust under occlusion and on-body drift. We present a design study of such a wristband front end in which classifier wake-up gating, mmWave versus IMU routing, and innovation-based EKF measurement reweighting share a single on-chip residual generator. The shared generator occupies 14.4 KB of program memory and 278 B of state and runs at 110K multiply-accumulates (MACs) per frame on an Ambiq Apollo4 Blue Plus class edge microcontroller unit (MCU). Across four public sensor data corpora (IPN Hand, SHREC 2021, MiliPoint 60 GHz FMCW radar, EAT-Radar) the front end reaches detection probability $P_D = 0.72/0.80$ at a 1% false-alarm rate, sustains a 47% classifier invocation energy reduction at 90% gesture detection recall, and lowers pose tracking root-mean-square error by $4.6\times$ under measurement bias drift relative to an adaptive Kalman with $R$-inflation baseline. Measured silicon power and on-body capture are deferred to follow-on hardware; the contribution here is a design study.

## Metadata
- **Published**: 2026-08-17T13:16:25Z
- **Authors**: Sam Rifaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16542v1)