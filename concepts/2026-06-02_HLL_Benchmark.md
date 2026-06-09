---
title: HLL Benchmark
type: concept
tags: [CAPTCHA, agent-evaluation, multimodal-agents, human-substitution, GUI-agents, benchmark]
sources:
  - arxiv: 2606.02449
  - code: https://github.com/XinhaoS0101/HLL
---

# HLL Benchmark

**Humanity's Last Line of Verification (HLL)** is a benchmark introduced in [2606.02449](arxiv:2606.02449) that evaluates whether multimodal agents can cross CAPTCHA verification boundaries through grounded, human-like interaction.

## Core Idea

CAPTCHAs represent a deliberate human-verification barrier. HLL tests whether agents can pass this barrier not just through recognition, but through full interactive solving with valid action traces.

## Key Findings

- Current frontier agents remain brittle at the human-substitution boundary
- Performance varies sharply across CAPTCHA types
- Realistic interface conditions (clutter, harder variants) degrade performance
- Requiring valid action traces further reduces success rates
- Exposes gaps in: localization, action calibration, state tracking, process consistency

## Related Concepts

- [[GUI Agents]]
- [[Agent Evaluation]]
- [[Multimodal Agents]]
- [[Human-in-the-Loop]]
