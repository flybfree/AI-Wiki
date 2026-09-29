---
title: Self-Adapting Group of Experts for Multi-Agent Reasoning
url: http://arxiv.org/abs/2609.35412v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_15-29-08Z_Self_AdaptingGroupofExpertsforMulti_AgentReasoning.md
generated_at: 2026-09-29 01:54
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces SAGE, a training-free framework for multi-agent reasoning that dynamically adapts agent strategies based on initial performance rather than relying on fixed system prompts or context modifications. By identifying a superior "strategy donor" through answer agreement, prefix consistency, and peer review, SAGE transfers effective reasoning patterns to other agents while maintaining their distinct roles, followed by information routing via a dynamic sparse directed acyclic graph. Experiments demonstrate that SAGE consistently outperforms existing baselines in accuracy across various agent backbones and reasoning benchmarks.

## Key Takeaways
- SAGE addresses the limitation of fixed prompts by enabling dynamic strategy transfer; it selects a high-performing agent as a donor using metrics like answer agreement and prefix consistency, then propagates that agent's reasoning strategy to peers without altering their core roles or requiring access to the problem details during adaptation.
- The framework operates entirely training-free and relies solely on original system prompts for strategy transfer, ensuring that agents can adopt new reasoning approaches without needing retraining, fine-tuning, or exposure to the specific problem instance or generated solutions during the adaptation phase.
- Following strategy adaptation, SAGE employs a dynamic sparse directed acyclic graph to facilitate communication, routing information from higher-scoring agents to lower-scoring ones, which leads to measurable improvements in average accuracy compared to baseline methods across diverse benchmarks and model backbones.

## Context
Multi-agent systems are increasingly

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35412v1)
