---
title: Self-Designed Evaluators and Warm Memory for Long-Horizon Agents
published: 2026-09-27T16:19:10Z
authors: Saeid Asgari, Emre Kiciman, Leonardo de Oliveira Nunes, Ranveer Chandra
url: http://arxiv.org/abs/2609.33717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Designed Evaluators and Warm Memory for Long-Horizon Agents

## Abstract
A tool-using language-model agent deployed over a long stream of tasks receives no reward, so it cannot tell whether it succeeded, cannot safely retry, and cannot label the experience it needs to improve. We present SelfSuite, in which the agent's own base model, given only the world's public materials, designs a small evaluation suite of weighted judges and grounded per-task briefs, freezes it, and uses it to gate a keep-best retry and to label a typed, outcome-tracked memory. On matched five-repeat benchmarks over tau2-bench and AppWorld, SelfSuite scores above the plain agent without any labels, matches methods given ten expert labels on tau2-bench, and trails Agentic Context Engineering (ACE) on AppWorld, where code execution gives a direct success signal. In an ablation campaign run on the same tasks, it is above label-free ACE in every repeat, and the gated second attempt is the only component whose removal hurts in every repeat. We also simulate a subject-matter expert who grades ten onboarding tasks per world. Using those labels to calibrate SelfSuite's evaluator gives a small, consistent gain, and using them to warm up ACE's memory lifts ACE to tie calibrated SelfSuite. A single-run study on a second model family shows the same ordering.

## Metadata
- **Published**: 2026-09-27T16:19:10Z
- **Authors**: Saeid Asgari, Emre Kiciman, Leonardo de Oliveira Nunes, Ranveer Chandra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33717v1)