---
title: HARDE: Optimizing Agent Harnesses for Runtime Risk Detection and Execution Control
published: 2026-09-29T17:23:37Z
authors: Zhuo Liu, Moxin Li, Zhixin Ma, Wentao Shi, Wenjie Wang, Fuli Feng
url: http://arxiv.org/abs/2609.38291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HARDE: Optimizing Agent Harnesses for Runtime Risk Detection and Execution Control

## Abstract
Large language model (LLM) agents are vulnerable to safety risks such as injected malicious instructions or misleading information, motivating runtime defenses that prevent unsafe action in execution across diverse risks while preserving benign-task utility. Existing system-level defenses either focus on risk detection rather than timely prevention or rely on predefined rules with limited flexibility across diverse risks. We propose a risk-aware harness that integrates LLM-based monitoring for flexible risk detection and structures monitor-guided execution around three core modules: trigger, monitor, and feedback, enabling targeted safety interventions while limiting disruption to benign task execution. To adapt the harness to different risks and deployment settings, we introduce HARDE, a two-stage harness optimization framework that first performs isolated probing of each module to derive an optimization guide, then uses this guide to iteratively optimize the harness based on safety and utility feedback. Experiments across three attack benchmarks show that HARDE improves runtime safety while preserving utility, outperforming manually designed harnesses and naive optimization baselines. Our analysis shows that effective runtime defense benefits from complementary safety mechanisms, attack-aware harness optimization, and harness designs matched to monitor capabilities. Our code is available at https://github.com/Liuz233/HARDE.

## Metadata
- **Published**: 2026-09-29T17:23:37Z
- **Authors**: Zhuo Liu, Moxin Li, Zhixin Ma, Wentao Shi, Wenjie Wang, Fuli Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38291v1)