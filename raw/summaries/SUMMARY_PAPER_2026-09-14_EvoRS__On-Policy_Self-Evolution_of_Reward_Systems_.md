---
title: EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning
url: http://arxiv.org/abs/2609.12459v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-11_05-40-59Z_EvoRS_On_PolicySelf_EvolutionofRewardSystemsforOpe.md
generated_at: 2026-09-14 15:10
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces EvoRS, a reinforcement learning framework designed to resolve the inherent instability of fixed reward systems in open-ended generation tasks. By dynamically evolving the reward mechanism through on-policy experience and an agentic designer, the method successfully mitigates reward hacking while maintaining discriminative signal quality throughout training. Empirical evaluations demonstrate that this self-evolving approach significantly outperforms static baselines across writing and roleplay benchmarks.

## Key Takeaways
- Fixed rubric-based rewards degrade over time as policies optimize them, leading to reward hacking and reduced response discriminability in open-ended domains.
- EvoRS represents the reward system as an executable Reward-DAG that is continuously updated by an agentic designer using on-policy rollouts and reward traces to ensure train-time reliability.
- The framework achieves superior quality across multiple judges, outperforming baseline policies by 2.107 and 4.767 points in writing and roleplay tasks while reducing coverage failures and preserving informative signals.

## Context
As generative AI models tackle increasingly complex open-ended tasks, traditional reward modeling struggles to adapt to evolving policy behaviors during training. This research addresses a critical gap in reinforcement learning alignment by shifting from static evaluation metrics to adaptive, self-correcting reward architectures. The work aligns with growing academic and industry efforts to develop more robust, scalable alignment methods that can keep pace with rapid model capability growth.

## Implications
Practitioners developing open-ended generation models can leverage self-evolving reward systems to prevent performance degradation and mitigate adversarial optimization during training cycles. The proposed Reward-DAG structure offers a practical blueprint for building resilient evaluation pipelines that automatically adapt alongside model capabilities. Ultimately, this approach could standardize dynamic alignment strategies across AI

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.12459v1)
