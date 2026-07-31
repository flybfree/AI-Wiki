---
title: Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control
published: 2026-07-30T09:28:37Z
authors: Takumi Shioda, Kohei Terashima, Tatsuo Nagai
url: http://arxiv.org/abs/2607.27914v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control

## Abstract
Multi-zone variable-air-volume control must balance thermal comfort, indoor air quality, and electricity use across several continuous actuators. Model predictive control and reinforcement learning are widely studied, but deployment typically requires building-specific modeling or training, limiting scalability. We first test whether a frontier reasoning model (an LLM trained to use additional inference-time computation) can achieve competitive VAV control from text without building-specific training. With that capability established, we then test whether TD3-guided reinforcement fine-tuning (RFT) can transfer control knowledge into a locally deployable open-weight model. Five controllers are evaluated over three summer days in a physics-based four-zone emulator. Relative to a Guideline 36-based baseline, TD3 reduced HVAC electricity by 4.5% while improving temperature and CO$_2$ compliance. Without building-specific training, GPT-5 achieved the largest reduction (6.2%) but reduced the ventilation margin. For RFT, deterministic rollouts restore a saved state, apply one candidate, and follow TD3 to score each action. Auditing a learned critic against these rollouts exposed a failure hidden by its near-perfect across-time correlation ($r=0.9998$): within-state ranking was unreliable; the critic selected the rollout-best candidate in only 5 of 10 states. Even with the rollout verifier, 200 RFT steps produced no sustained improvement in sampled-action return; the open-weight controller used more electricity than the baseline before and after training, and its five-minute predictions remained worse than persistence. GPT-5 predicted transitions far better. Exact rollout scores rank sampled actions but reveal neither next-state effects nor an improvement direction. The unchanged transition errors motivate transition-focused supervised fine-tuning before value-based RFT.

## Metadata
- **Published**: 2026-07-30T09:28:37Z
- **Authors**: Takumi Shioda, Kohei Terashima, Tatsuo Nagai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27914v1)