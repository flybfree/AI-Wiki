---
title: Harness-Zero: Harness Distillation via Agent-as-Harness
url: http://arxiv.org/abs/2609.24974v1
type: paper-summary
date: 2026-09-21
source_paper: 2026-09-21_17-55-20Z_Harness_Zero_HarnessDistillationviaAgent_as_Harnes.md
generated_at: 2026-09-21 23:12
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces Harness-Zero, a novel method for distilling the performance gains provided by specialized agent harnesses into the weights of large language models (LLMs). By utilizing an "agent-as-harness" to bridge the gap between different action spaces and information environments, the researchers enable models to internalize complex behaviors so that they can be executed under a single, fixed target harness.

## Key Takeaways
- The primary challenge in agent harness distillation is that specialized harnesses often operate within unique action spaces and have access to specific information that differs from the target environment, making direct supervision impossible.
- Harness-Zero addresses this by using a harnessing agent to translate guidance from an optimized harness into the target's action space, effectively converting external assistance into high-quality training demonstrations for fine-tuning.
- Empirical evaluations across knowledge work, tool use, and science domains demonstrate that Harness-Zero improves macro-average task success from 23.3% to 44.3%, even surpassing the performance achieved when the specialized harness is still attached.
- The method successfully recovers 82.3% of the specific behaviors induced by specialized harnesses across 28 distinct patterns, proving that the model can internalize complex reasoning and interaction strategies.

## Context
As AI agents become more sophisticated, their success often relies on "harnesses"—external systems that manage environment interactions and provide scaffolding. However, these gains are currently tied to specific environments, meaning a general-purpose agent must either use a suboptimal universal harness or navigate an unmanageable number of specialized ones. This paper addresses the critical need for portable intelligence where the model itself learns to perform complex tasks without requiring heavy external scaffolding at inference time.

## Implications
For researchers and practitioners, this work suggests that we can move toward "scaffold-free" AI by using distillation techniques to bake expert behaviors into model weights. By enabling the removal of specialized harnesses during deployment, Harness-Zero provides a pathway for creating more portable, efficient, and scalable AI agents that maintain high performance across diverse domains like science and tool use without requiring massive infrastructure overhead at inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.24974v1)
