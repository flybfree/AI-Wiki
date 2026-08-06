---
title: Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning
published: 2026-08-05T10:21:11Z
authors: Aaditya Mehta, Arya Shah
url: http://arxiv.org/abs/2608.04663v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning

## Abstract
Cooperative multi-agent reinforcement learning often adds social terms to individual rewards, yet the scale of those terms is usually chosen by hand. We ask whether a guilt signal can instead be calibrated from human neural and behavioural data and transferred to artificial agents. Using the public SoDec responsibility fMRI dataset (40 participants), we fit a subject-fixed-effects regression of momentary-happiness changes on outcome-type counts and recover a guilt weight as the Partner-negative minus Social-negative contrast ($\hat{w}=1.118$, Cohen's $d=0.214$). We embed this weight in a two-agent Social Lottery environment and train independent Proximal Policy Optimization actor-critics under four shaping regimes: neurally calibrated, uniform constant, zero (selfish), and a unit-coefficient oracle. Across 1{,}000 evaluation episodes per condition, the calibrated agents track the human Social safe-choice rate most closely ($0.459$ vs.\ human $0.484$; $\mathrm{KL}=0.0012$), while the other three conditions deviate by one to three orders of magnitude in KL. Human neurobehavioural priors can therefore act as quantitative constraints on prosocial reward shaping.

## Metadata
- **Published**: 2026-08-05T10:21:11Z
- **Authors**: Aaditya Mehta, Arya Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04663v1)