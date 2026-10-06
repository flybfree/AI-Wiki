---
title: Benchmarking Jailbreak Guardrails for Embodied Agents
published: 2026-10-05T10:56:18Z
authors: Xunguang Wang, Qingyue Wang, Yuguang Zhou, Zongjie Li, Wenxuan Wang, Shuai Wang
url: http://arxiv.org/abs/2610.06122v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Jailbreak Guardrails for Embodied Agents

## Abstract
Embodied agents powered by large language models and vision-language models are increasingly deployed in physical environments, but jailbreak attacks can induce these agents to perform physically harmful actions. A growing number of guardrail methods have been proposed to intercept dangerous behavior before it is executed, yet existing safety benchmarks evaluate the embodied models themselves, leaving it unclear how well these guardrails actually defend an embodied agent in practice. We present the first systematic evaluation of jailbreak guardrails for embodied agents. To compare guardrails under identical conditions, we build a pluggable evaluation framework that treats the embodied agent as a fixed backend and each guardrail as a module that can intervene at the perception, planning, or control stage. We subject six representative guardrails to template-based and automated jailbreak attacks as well as safe instructions, and assess them at the system level along three dimensions: defense effectiveness, measured by the bypass rate and the hazard success rate in the simulator; usability, measured by the false-positive rate and the task completion rate on safe instructions; and efficiency, measured by the latency overhead added at runtime. Experiments on guardrails that span different intervention stages, decision mechanisms, and input modalities reveal a clear trade-off among the three dimensions, and show that no single guardrail dominates in all settings. We further analyze how intervention stage, decision mechanism, and input modality shape safety outcomes, and we offer practical guidance for selecting and designing guardrails for embodied agents.

## Metadata
- **Published**: 2026-10-05T10:56:18Z
- **Authors**: Xunguang Wang, Qingyue Wang, Yuguang Zhou, Zongjie Li, Wenxuan Wang, Shuai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06122v1)