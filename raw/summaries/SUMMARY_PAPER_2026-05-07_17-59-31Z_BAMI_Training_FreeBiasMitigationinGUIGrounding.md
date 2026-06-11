---
title: BAMI: Training-Free Bias Mitigation in GUI Grounding
url: http://arxiv.org/abs/2605.06664v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-07_17-59-31Z_BAMI_Training_FreeBiasMitigationinGUIGrounding.md
generated_at: 2026-06-11 10:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces BAMI a training-free bias mitigation method for GUI grounding tasks. It addresses errors caused by high image resolution and ambiguous interface elements. Experiments show improved accuracy on the ScreenSpot-Pro benchmark.

## Key Takeaways
- The method identifies precision bias from high image resolution as a main source of errors.
- It also recognizes ambiguity bias arising from intricate interface elements that confuse grounding models.
- Applying BAMI to TianXi-Action-7B raises accuracy from 51.9% to 57.8% on the benchmark.

## Context
GUI grounding enables agents to interact with graphical interfaces by locating and selecting UI components. Current models often fail in complex scenes where resolution varies or elements overlap, limiting practical deployment. These biases are common across many vision-based grounding systems that rely solely on pixel-level analysis.

## Implications
BAMI offers a lightweight correction that can be applied without retraining models, making it attractive for real-time applications. Practitioners can adopt this approach to boost reliability of GUI agents across diverse screen conditions. The approach also reduces the need for extensive dataset augmentation, simplifying model deployment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.06664v1)
