---
title: Learning to Modulate, Not to Cycle: Soft Actor---Critic Recovers Inverter-Style Heat-Pump Control
published: 2026-08-10T11:24:29Z
authors: Faizan Ahmed, Aniket Dixit, James Brusey
url: http://arxiv.org/abs/2608.09453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Modulate, Not to Cycle: Soft Actor---Critic Recovers Inverter-Style Heat-Pump Control

## Abstract
On--off cycling is the main cause of compressor wear in residential heat pumps, yet reinforcement learning (RL) controllers for buildings typically optimise only energy cost and thermal comfort, ignoring how much the learned policy cycles. We add a levelised compressor-wear term to the control reward and study how the resulting behaviour depends on the RL algorithm. Training Soft Actor---Critic (SAC) and Proximal Policy Optimisation (PPO) on an identical Markov decision process for the BOPTEST bestest hydronic heat pump case, we find that SAC learns a continuous modulation policy that keeps the compressor permanently engaged---the operating principle of an inverter-driven heat pump---achieving zero start-ups per day, whereas PPO collapses to bang-bang control that cycles more than the baseline. On the BOPTEST emulator the SAC policy cuts thermal discomfort by up to 90.7% for an 11.5% cost increase, while eliminating all baseline cycling.

## Metadata
- **Published**: 2026-08-10T11:24:29Z
- **Authors**: Faizan Ahmed, Aniket Dixit, James Brusey
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09453v1)