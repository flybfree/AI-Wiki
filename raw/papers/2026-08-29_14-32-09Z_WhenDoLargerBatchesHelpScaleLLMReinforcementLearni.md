---
title: When Do Larger Batches Help Scale LLM Reinforcement Learning?
published: 2026-08-29T14:32:09Z
authors: Ziniu Li, Jinbo Wang, Guanhua Huang, Feiyuan Zhang, Pengbo Li, Alex Chen
url: http://arxiv.org/abs/2608.29296v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Larger Batches Help Scale LLM Reinforcement Learning?

## Abstract
Larger batches reduce the variance of stochastic gradients per update and are therefore often expected to accelerate training. Yet whether this statistical benefit translates into lower wall-clock time-to-target remains unclear, because each update consumes more samples and may take longer to execute. We study this tradeoff in reinforcement learning for large language models. We separate its algorithmic and systems effects by comparing learning and execution along their natural axes. At the algorithmic level, we compare configurations at equal cumulative sample counts while retuning batch-dependent hyperparameters. Over a bounded range of batch sizes, this procedure yields an approximately batch-size-invariant family whose members follow similar sample-indexed learning trajectories. At the systems level, we exploit the computational asymmetry between rollout generation and training: autoregressive generation is often memory-bandwidth-bound at low concurrency, whereas training work scales approximately with the number of processed tokens. Combining these two views yields a direct decision rule: a larger-batch configuration reduces time-to-target only when its throughput gain exceeds its samples-to-target penalty. Experiments with GRPO and PPO support both sides of this decomposition. At the algorithmic level, square-root learning-rate scaling with Adam produces approximately batch-size-invariant learning curves over a bounded range of batch sizes. At the systems level, larger batches improve generation throughput by up to 2.29x on fixed hardware. In GRPO, combining higher throughput with learning-rate retuning reduces time-to-target by up to 29%, whereas increasing the batch without retuning is slower despite its higher throughput.

## Metadata
- **Published**: 2026-08-29T14:32:09Z
- **Authors**: Ziniu Li, Jinbo Wang, Guanhua Huang, Feiyuan Zhang, Pengbo Li, Alex Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29296v1)