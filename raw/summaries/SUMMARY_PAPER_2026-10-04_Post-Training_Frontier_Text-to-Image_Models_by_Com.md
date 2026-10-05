---
title: Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards
url: http://arxiv.org/abs/2610.02967v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_08-05-34Z_Post_TrainingFrontierText_to_ImageModelsbyComposin.md
generated_at: 2026-10-04 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a post-training recipe for open-domain text-to-image generation models that combines complementary reward signals to overcome the limitation of single-reward optimization. The authors develop a system pairing a preference reward trained on human aesthetic data with rubric-based rewards evaluating prompt faithfulness, and propose a reward composition strategy that outperforms naive weighted averaging. Their RL-trained Flux2dev and post-trained Ideogram-4 achieve state-of-the-art results on the Arena text-to-image leaderboard, with Elo gains of 69 points and an overall rating of 1223.5 respectively.

## Key Takeaways
- The reward system is composed of two heterogeneous components: a preference reward trained via a Bradley-Terry objective on large-scale human preference data to capture overall aesthetic and perceptual judgments, and rubric-based rewards that explicitly evaluate prompt faithfulness and other desirable properties while acting as safeguards against reward hacking. This dual approach addresses the fundamental challenge that no single reward signal can capture the full range of human preferences for image generation.
- A naive weighted average of these heterogeneous reward signals leads to suboptimal optimization behavior during reinforcement learning training. The authors propose a simple reward composition strategy that more effectively balances preference optimization with rubric satisfaction, suggesting that the architecture of reward combination is as critical as the rewards themselves for achieving strong post-training performance.
- The authors release Arena-T2I-Training, a 1,000-sample subset of their training data that recovers some gains of full-scale training, providing a reproducible resource for the research community to facilitate future work on post-training for text-to-image models without requiring access to the full proprietary dataset.

## Context
Post-training with reinforcement learning has become a dominant paradigm for aligning large language models, but its application to text-to-image generation remains underdeveloped due to the difficulty of defining comprehensive reward signals for visual quality. This paper addresses a critical gap by demonstrating that effective reward design for generative image models requires broad coverage of user intent and robustness against exploitation during optimization. The work builds on the growing ecosystem of open-source image generation models like Flux2dev and Ideogram-4, showing that principled post-training can unlock substantial performance gains without architectural changes.

## Implications
For practitioners and model developers, this work provides a practical and transferable recipe for improving text-to-image models through post-training, demonstrating that composing multiple reward signals with a carefully designed combination strategy can yield significant Elo improvements on competitive leaderboards. The release of a 1K training subset lowers the barrier for academic and smaller-scale researchers to explore post-training techniques for image generation, potentially accelerating progress across the open-source model ecosystem. The findings also signal that future frontier model development will require increasingly sophisticated reward engineering rather than relying on any single optimization objective.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02967v1)
