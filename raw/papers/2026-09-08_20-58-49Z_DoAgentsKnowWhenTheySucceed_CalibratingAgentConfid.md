---
title: Do Agents Know When They Succeed? Calibrating Agent Confidence from Internal Representations
published: 2026-09-08T20:58:49Z
authors: Priyanka Mary Mammen, Emil Joswin, Srujananjali Medicherla
url: http://arxiv.org/abs/2609.09448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Agents Know When They Succeed? Calibrating Agent Confidence from Internal Representations

## Abstract
As agentic systems getting adopted rapidly in safety critical applications, it is vital to measure the confidence associated with the agentic actions. In comparison to the traditional machine learning systems, agentic workflows have complex failure modes with planning, tool invocation and dynamic environment interactions. In this paper, we investigate whether model's internal representations provide stronger signals of eventual task success in multi-turn agentic setups. We introduce two complementary methods: Latent Trajectory Dynamics (LTD), which summarizes changes in residual-stream representations across an an interaction trajectory, and the Action Representation Probe (ARP), which predicts success from representations formed at action decisions. Across three interactive benchmarks (Bash, SQL, Python) and three model families (Qwen14B, Qwen7B, DeepSeek6.7B), our methods consistently outperform surface level generation and sequence-based calibration baselines providing a zero-overhead reliability monitor that requires neither prompt alterations nor multi-sample rollouts.

## Metadata
- **Published**: 2026-09-08T20:58:49Z
- **Authors**: Priyanka Mary Mammen, Emil Joswin, Srujananjali Medicherla
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09448v1)