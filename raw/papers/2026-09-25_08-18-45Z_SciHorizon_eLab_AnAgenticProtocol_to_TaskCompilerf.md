---
title: SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents
published: 2026-09-25T08:18:45Z
authors: Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu
url: http://arxiv.org/abs/2609.30971v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents

## Abstract
Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executable and verifiable embodied tasks at scale. To address this challenge, we introduce SciHorizon-eLab, an agentic protocol-to-task compiler that formulates scientific embodied task construction as a compilation problem. Given a natural-language protocol of scientific experiments, SciHorizon-eLab progressively compiles laboratory protocols into semantic-preserving embodied tasks through semantic grounding, executable task synthesis, and multi-stage simulation-based certification. The system generates semantically grounded environments, executable manipulation programs, and step-level success specifications, while enabling reproducible generation of expert demonstrations and execution traces. Using this pipeline, we further construct \BenchName, a ready-to-use benchmark comprising 300 certified tasks across diverse laboratory operations. It supports HIL task execution, reproducible expert-demonstration generation, and ordered step-level evaluation. Across representative tasks, the strongest policy attains an average success rate of only 49.7%, with further evaluations revealing pronounced weaknesses in human and embodied agent coordination. We publicly release the code, benchmark data, and evaluation toolkit at https://github.com/SciHorizon-elab/SciHorizon-elab.

## Metadata
- **Published**: 2026-09-25T08:18:45Z
- **Authors**: Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30971v1)