---
title: More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents
url: http://arxiv.org/abs/2610.33684v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_14-03-20Z_More_Mode_OptimizedReasoningwithSelf_AdaptiveEffor.md
generated_at: 2026-10-26 20:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MORE (Mode-Optimized Reasoning with Self-Adaptive Effort), a self-evolving training framework that enables agents to adaptively select both their reasoning mode (direct answering, short chain-of-thought, long chain-of-thought, or code-based reasoning) and the computational effort (token expenditure) allocated to each task. The framework uses a two-stage training paradigm combining a compact prior over reasoning modes with a self-evolving reinforcement learning stage (MATE-PPO) on verifiable task streams, achieving consistent performance gains across coding, mathematics, and general-reasoning benchmarks while producing shorter, more efficient inference responses.

## Key Takeaways
- MORE addresses a critical inefficiency in self-evolving training: the uniform application of costly deliberation across all tasks. By learning mode selection and token expenditure jointly, the framework allocates concise reasoning to simpler tasks while retaining extended deliberation only where it is genuinely useful, reducing unnecessary computational overhead without sacrificing accuracy.
- The two-stage training paradigm first establishes a compact prior over four reasoning modes (direct answering, short CoT, long CoT, and code-based reasoning) in Stage 1, then self-evolves this prior in Stage 2 using Mode-Adaptive and Test-time Effort PPO (MATE-PPO) on generated, verifiable task streams without requiring curated training data, making the approach scalable and data-efficient.
- Empirical results demonstrate consistent performance gains on both Base and Coder model backbones across scales from 3B to 14B parameters, with inference-time improvements including higher accuracy, markedly shorter response lengths, and reduced inference time, showing that adaptive reasoning allocation outperforms fixed-length deliberation strategies.

## Context
Self-evolving training methods such as RLHF and reinforcement learning from verifiable rewards have become central to improving large language model agents on complex reasoning tasks. However, existing approaches typically apply a fixed reasoning budget—always generating long chain-of-thought or always using a specific mode—regardless of task difficulty. This paper sits at the intersection of efficient inference, adaptive reasoning, and self-improving agent training, addressing a growing concern in the field about the computational cost of deliberative reasoning and the need for agents that can calibrate their own effort dynamically.

## Implications
For practitioners deploying LLM-based agents in production environments, MORE offers a pathway to reduce inference costs and latency while maintaining or improving task accuracy, which is critical for scaling agent systems economically. For the research community, the framework demonstrates that mode selection and effort allocation can be learned jointly through self-evolving training without curated supervision, suggesting a more general recipe for building efficient, self-improving agents that adapt their reasoning strategy to the demands of each task rather than applying a one-size-fits-all deliberation policy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33684v1)
