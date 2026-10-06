---
title: Grounded Joint-Attention Other-Play for Zero-Shot Coordination
url: http://arxiv.org/abs/2610.06025v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_09-23-11Z_GroundedJoint_AttentionOther_PlayforZero_ShotCoord.md
generated_at: 2026-10-05 22:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MATE (Mutual Attention for zero-shot TEaming), a multi-agent reinforcement learning method inspired by the human cognitive ability of joint attention, designed to enable zero-shot coordination between unfamiliar AI agents. Rather than relying on arbitrary partner-specific conventions learned during training, MATE encourages agents to coordinate by aligning their visual attention on scene-salient objects during interaction. Experiments across three benchmarks demonstrate that this joint-attention-inspired signal consistently improves coordination with unknown partners, surpassing traditional symmetry-breaking approaches.

## Key Takeaways
- MATE replaces brittle, partner-dependent conventions with an environment-grounded coordination signal: agents align their visual attention on salient objects in the shared environment, creating a naturally shared reference point that does not depend on prior training with a specific partner. This fundamentally differs from symmetry-breaking methods, which merely prevent undesirable conventions from forming but do not actively promote coordination through a shared perceptual mechanism.
- The method was evaluated on three distinct benchmarks: a custom Card Alignment Game specifically designed to isolate brittle convention formation, the Level-Based Foraging benchmark, and the more complex OvercookedV2 benchmark. Across all three environments, the joint-attention-inspired signal improved zero-shot coordination performance, suggesting the mechanism generalizes beyond narrow experimental setups.
- The work draws a direct parallel between human joint attention—the ability to share a common visual or cognitive focus with others—and machine coordination, proposing that grounding coordination in shared perceptual attention to the environment provides a more robust and transferable coordination mechanism than convention-based approaches.

## Context
Zero-shot coordination—where agents trained independently must cooperate with previously unseen partners without any fine-tuning—remains a central challenge in multi-agent reinforcement learning. Existing solutions such as Other-Play and symmetry-breaking methods attempt to prevent agents from learning brittle, partner-specific conventions during training, but they do not provide a positive mechanism for establishing shared understanding at interaction time. This paper addresses that gap by borrowing from cognitive science, specifically the concept of joint attention studied in developmental psychology and human-robot interaction, to propose a principled alternative grounded in shared environmental perception.

## Implications
For practitioners building multi-agent systems in robotics, game AI, or autonomous coordination tasks, MATE offers a coordination mechanism that does not require retraining when new partners or environments are introduced, reducing deployment costs and brittleness. The findings suggest that future multi-agent systems should incorporate shared perceptual grounding rather than relying solely on convention-avoidance strategies, potentially influencing how researchers design cooperative agents for open-world, dynamic environments. This work also bridges cognitive science and machine learning, pointing toward a broader class of human-inspired coordination mechanisms that could make AI agents more robust and generalizable in collaborative settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06025v1)
