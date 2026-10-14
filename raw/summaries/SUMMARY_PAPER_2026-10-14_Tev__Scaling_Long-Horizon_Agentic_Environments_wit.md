---
title: Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards
url: http://arxiv.org/abs/2610.18868v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_17-59-51Z_Tev_ScalingLong_HorizonAgenticEnvironmentswithDens.md
generated_at: 2026-10-14 00:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Tev-Gym, the first long-horizon agent training dataset featuring verifiable, dense, progressive rewards across 1,170 task environments spanning seven domains, built through a novel "latent-world-first" construction methodology. The authors then develop a training recipe called progress-potential reward shaping (PPRS) that converts task progress into dense per-step rewards, enabling efficient training of long-horizon agents. The resulting model, Tev-27B, achieves competitive performance on the Agents' Last Exam computing and math sciences benchmarks, matching frontier closed models like GPT-6 Astra and Claude Opus 5 at Pass@5, while generalizing to unseen terminal-bench evaluation suites.

## Key Takeaways
- Tev-Gym addresses the critical data bottleneck for long-horizon agent training by constructing a complete hidden specification of each task domain, workflow, and expected state before rendering it into an agent-facing environment. This latent-world-first approach enables controllable task complexity and a natural progress metric, producing 1,170 verified environments across seven domains with dense, progressive rewards rather than the sparse terminal rewards typical of existing benchmarks.
- Progress-potential reward shaping (PPRS) transforms the latent-world progress metric into a dense per-step reward signal, making otherwise-intractable long-horizon tasks trainable and significantly improving training efficiency. This recipe converts the fundamental challenge of sparse rewards in long-horizon tasks into a tractable optimization problem.
- Tev-27B, trained exclusively on ALE-related data, demonstrates strong generalization: it matches GPT-6 Astra and Claude Opus 5 on ALE-CM at Pass@5, surpasses GLM 5.2 and Gemini 3.7 Flash on Terminal-Bench 3.0 and 4.0 subsets, and reaches Claude Opus 4.8-level performance on middle-horizon tasks such as TB 2.1, showing that dense reward shaping can unlock capabilities competitive with much larger closed models.

## Context
Long-horizon autonomous agents operating over hours to days are widely regarded as a prerequisite for automated scientific discovery and recursive self-improvement, yet open-source models have lagged far behind closed frontier models on such tasks. The core obstacles have been twofold: the scarcity of verifiable, complex training environments and the difficulty of providing meaningful learning signals when rewards are only available at task completion. This paper directly targets both gaps simultaneously by coupling a new data-generation methodology with a reward-shaping training recipe, positioning itself at the intersection of agent benchmarking, reinforcement learning, and open-model development.

## Implications
For practitioners building open-source agentic systems, Tev-Gym and PPRS offer a reproducible recipe for training long-horizon agents without relying on proprietary closed-model data or prohibitively expensive human curation, potentially lowering the barrier for research groups to develop competitive autonomous agents. For the broader field, the latent-world-first construction paradigm suggests a scalable path toward generating verifiable, progressively complex environments that could accelerate progress toward recursive self-improvement and automated discovery pipelines, while the demonstrated generalization from ALE to Terminal-Bench indicates that dense progress rewards may transfer across task domains more broadly than previously assumed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18868v1)
