---
title: Think or Remember: The Exchange Rate of Agentic Inference
url: http://arxiv.org/abs/2611.10982v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-07_21-45-35Z_ThinkorRemember_TheExchangeRateofAgenticInference.md
generated_at: 2026-11-11 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper formalizes the cost structure of agentic inference systems built on reasoning models, where agents resend their growing transcript at every call. The authors define a precise cost model matching an instrumented engine, introducing an "exchange rate" P* = c/β that partitions agent behavior into a thinking regime (below P*, where per-token processing dominates) and a memory regime (above P*, where attention over cached reasoning dominates). Empirically, they show that server-side serving decisions—such as whether earlier reasoning states are reused—can flip which context-management policy is cheaper, and that dropping earlier reasoning degrades task accuracy by 9–23 percentage points on HotpotQA across four models.

## Key Takeaways
- The authors define a cost model with two parameters: $c per token processed and β per pair attended, whose ratio P* = c/β acts as an exchange rate between thinking and remembering. Below P*, processing costs dominate (a "thinking regime"); above P*, attention costs dominate (a "memory regime"). This provides a principled threshold for when agents should rely on cached reasoning versus fresh computation.
- A policy change (e.g., dropping earlier reasoning from the transcript) incurs both a mechanical cost—charged even if the agent writes identical tokens—and a behavioral cost, because the agent writes different tokens, altering both cost and outcome. On recorded Qwen3-8B ScienceWorld runs, dropping earlier reasoning costs 1.74× keeping it when the server reuses generated states, but only 0.34× when it reuses nothing, demonstrating that serving architecture alone can invert the economic calculus.
- In live reruns on HotpotQA, dropping earlier reasoning cuts correct answers by 9–23 percentage points across four models, even at lower point-estimate cost. This shows that cheaper serving configurations can silently degrade agent performance, and that comparing context policies requires comparing the full system—architecture, serving, and induced behavioral changes—rather than token counts in isolation.

## Context
As reasoning-augmented agents become standard in production AI systems, the economics of long-context inference have become a critical bottleneck. Prior work has treated context management as a purely algorithmic or prompt-engineering problem, without modeling how server-side caching and attention mechanics interact with client-side transcript editing to determine true cost. This paper bridges that gap by grounding cost analysis in an instrumented engine and formalizing the interaction between client policy and server serving, a distinction that existing literature on KV-cache optimization and prompt compression has largely overlooked.

## Implications
For practitioners deploying agentic systems, this work demonstrates that cost savings from aggressive context pruning can be illusory: the apparent savings depend entirely on whether the serving infrastructure reuses generated reasoning states, and the behavioral degradation in task accuracy can be substantial. For the industry, it argues that infrastructure decisions—cache policies, attention scheduling, and transcript retention—are not merely engineering details but first-order determinants of agent capability and cost, meaning that benchmarking agent policies without specifying the serving stack yields misleading comparisons.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10982v1)
