---
title: TCPO: Turn-Level Credit Policy Optimization
published: 2026-08-03T04:01:36Z
authors: Sicong Liao, Zhi Chen, Yaohua Tang
url: http://arxiv.org/abs/2608.01667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TCPO: Turn-Level Credit Policy Optimization

## Abstract
Verifier-guided reinforcement learning has become a powerful paradigm for improving LLM reasoning. In multi-turn settings, models receive a verifier score after each turn and iteratively refine their outputs. Although such scores provide dense feedback, they do not directly provide dense credit: a score measures the quality of the current output, while credit should measure how the current turn changes the refinement trajectory. We propose TCPO, a turn-level credit assignment method for verifier-guided multi-turn RL. TCPO casts credit assignment as score-to-credit conversion and constructs turn-level advantages through reference-based comparisons: retrospective credit captures immediate progress and regression relative to the best prior state; hindsight delayed credit identifies non-improving turns with later payoff; and selective fixed-history counterfactual estimation refines high-surprisal turns under the same history. Experiments on math reasoning, code generation, and AppWorld agent tasks show that TCPO improves or matches the strongest baselines across model scales, task domains, and verifier types. TCPO achieves the best or tied-best best-turn Pass@8 on Qwen3-4B and DeepSeek-R1-Distill-Llama-8B, reduces turns to success, and improves multi-turn agent performance. These results highlight score-to-credit conversion as a central ingredient for verifier-guided multi-turn policy optimization.

## Metadata
- **Published**: 2026-08-03T04:01:36Z
- **Authors**: Sicong Liao, Zhi Chen, Yaohua Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01667v1)