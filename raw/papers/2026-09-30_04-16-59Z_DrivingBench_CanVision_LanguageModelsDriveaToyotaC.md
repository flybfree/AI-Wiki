---
title: DrivingBench: Can Vision-Language Models Drive a Toyota Corolla?
published: 2026-09-30T04:16:59Z
authors: Aditya Ramabadran, Simon Mahns, Tobias Gessler
url: http://arxiv.org/abs/2609.38948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DrivingBench: Can Vision-Language Models Drive a Toyota Corolla?

## Abstract
Frontier models excel at many digital benchmarks, yet their ability to drive a real car, an everyday human skill, remains largely untested. We present DrivingBench, to our knowledge the first benchmark where general-purpose vision-language models must drive a real car. Through three tools, the models see camera frames from a Toyota Corolla and directly command its steering and velocity around a parking lot cone course at low speeds. The car may continue moving while the model thinks and new commands replace the currently running one, so inference latency is part of the task, testing the models' abilities to observe, act, monitor, recover, and complete a long-horizon objective under such constraints. We benchmark GPT-6 Astra, Claude Fable 5.1, GPT-5.6 Sol, and Grok 4.6 in vendor-native harnesses (Codex, Claude Code, Cursor) with up to three attempts each in one conversation; Astra is the only model to finish the course, on its second attempt, with no other attempt passing 50% of the course. Two of the four models improved materially across attempts with retained context. We also detail the design principles behind our action interface, and show how the tool output format and the framing of the task combined to determine whether models would drive at all or refuse. We release our harness, prompts, course map, and traces with video and telemetry for reproducibility.

## Metadata
- **Published**: 2026-09-30T04:16:59Z
- **Authors**: Aditya Ramabadran, Simon Mahns, Tobias Gessler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38948v1)